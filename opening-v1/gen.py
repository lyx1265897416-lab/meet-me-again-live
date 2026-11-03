# -*- coding: utf-8 -*-
"""usage: gen.py plates | frames [key..] | takes [key..] | lip [key..]"""
import json, subprocess, sys, time, hashlib, os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
V = Path(__file__).resolve().parent
sys.path.insert(0, str(V))
sys.path.insert(0, '/Users/vicky/Interactive storyline/projects/meet-me-again-deepspace-20261013/interactive-video-v1/tools')
exec((V / 'shots.py').read_text())
os.environ['PATH'] = '/Users/vicky/.local/bin:/Users/vicky/.waku/bin:/opt/homebrew/bin:' + os.environ['PATH']
def cli(a, t=600):
    p = subprocess.run(['waku'] + a, capture_output=True, text=True, timeout=t)
    try: return json.loads(p.stdout[p.stdout.find('{'):])
    except Exception: return dict(_err=(p.stdout + p.stderr)[-200:])
def upload(path):
    sha = hashlib.sha256(Path(path).read_bytes()).hexdigest(); rec = V / 'inputs' / (sha + '.json')
    if rec.exists(): return json.loads(rec.read_text())['url']
    for k in range(4):
        d = cli(['persist', str(path)], 400)
        if d.get('url'): rec.write_text(json.dumps(dict(url=d['url']))); return d['url']
        time.sleep(4)
    import mcp_upload
    for k in range(5):
        try: u = mcp_upload.upload(str(path)); rec.write_text(json.dumps(dict(url=u))); return u
        except Exception:
            if k == 4: raise
            mcp_upload._mcp = None; time.sleep(5 * (k + 1))
def run(name, model, cap, params, out):
    rec = V / 'jobs' / f'{name}.json'
    if out.exists() and out.stat().st_size > 30000: return name, 'cached'
    r = json.loads(rec.read_text()) if rec.exists() else None
    if not r or not r.get('job_id') and not r.get('asset_url'):
        d = cli(['gen', 'run', model, '--capability', cap, '--params', json.dumps(params, ensure_ascii=False)])
        r = dict(model=model, params=params, job_id=d.get('job_id'), asset_url=d.get('asset_url')); rec.write_text(json.dumps(r, ensure_ascii=False))
        if not r['job_id'] and not r['asset_url']: rec.unlink(); return name, 'SUBMIT FAIL ' + str(d)[:200]
    url = r.get('asset_url')
    for _ in range(200):
        if url: break
        x = cli(['gen', 'result', r['job_id'], '--refresh'], 120)
        url = x.get('asset_url') or x.get('result_url')
        if x.get('status') in ('failed', 'cancelled'): rec.unlink(); return name, 'FAILED ' + str(x.get('error'))[:200]
        if not url: time.sleep(10)
    if not url: return name, 'pending'
    r['asset_url'] = url; rec.write_text(json.dumps(r, ensure_ascii=False))
    tmp = out.with_suffix('.part' + out.suffix)
    for _ in range(8):
        if subprocess.run(['curl', '-fsSL', '-C', '-', '--retry', '3', '--max-time', '900', url, '-o', str(tmp)]).returncode == 0: break
        time.sleep(5)
    tmp.rename(out); return name, 'ok'
def image(name, refs, prompt):
    return run(name, 'openai/gpt-image-2/edit', 'multimodal.generate.image', dict(images=[upload(p) for p in refs], prompt=prompt, aspect_ratio='9:16'), V / 'frames' / f'{name}.png')
def axis(s):  # solo shots never name the absent person: naming them draws them into the picture
    if MAISIE in s['refs'] and ROWAN in s['refs']: return AXIS
    return 'She faces screen right and is the only person in the picture.' if MAISIE in s['refs'] else 'He faces screen left and is the only person in the picture.'
def frame(s):
    if s.get('cu'): return s['key'], 'cached'
    if s['key'] == 'S03d': return 'S03d', 'cached'
    who = (SHE if MAISIE in s['refs'] else '') + ' ' + (HE if ROWAN in s['refs'] else '')
    refs = ([str(V / 'frames' / (s['plate'] + '.png'))] if s['plate'] else []) + s['refs']  # plate first; for him rowan.png then CANON
    head = 'Image 1 is the empty location plate of this exact set: keep its background, architecture, colours and light. The other images are identity and costume references only; do not copy their white background or framing. ' if s['plate'] else ''
    who_p = (axis(s) + ' ' + PROPS + ' ' + ONLY2) if who.strip() else ''
    return image(s['key'], refs, head + s['frame'] + PLACE + ' ' + who + ' ' + who_p + ' ' + STYLE)
def take(s):
    who = (SHE if MAISIE in s['refs'] else '') + ' ' + (HE if ROWAN in s['refs'] else '')
    p = s['act'] + ' ' + PLACE + ' ' + who + (' ' + axis(s) + ' ' + PROPS + ' ' + ONLY2 if who.strip() else '') + ' ' + (SILENT + ' ' if who.strip() else '') + GUARD + ' ' + STYLE
    return run('take-' + s['key'], 'bytedance/seedance-2.5/image-to-video', 'multimodal.generate.video', dict(image=upload(V / 'frames' / f"{s['key']}.png"), prompt=p, duration=s['dur'], resolution='720p', generate_audio=True, **({'last_image': upload(V / 'frames' / f"{s['last']}.png")} if s.get('last') else {})), V / 'takes' / f"{s['key']}.mp4")
VOICE = {'M': 'A warm, natural young American male voice, relaxed and amused, a smile in it.', 'F': 'A natural warm low-mid young American female voice, unimpressed, quietly sharp.'}
def native(s):
    # 11-02 Vicky chose R1/W2 (Seedance native): the shot is acted and spoken in one take; no silent take + lipsync.
    k, _ = s['lines'][0]; who, line = LINES[k][3], LINES[k][4]; male = who == 'Rowan'
    say = (f'{"He" if male else "She"} says aloud, in English, exactly these words once, in order, with real acting and natural timing: "{line}" {VOICE["M" if male else "F"]} Only {"he" if male else "she"} speaks, only that line. Lips move with the words and close when finished; natural breathing, small head and shoulder movement with the words. No music, no other voices.')
    people = (SHE + ' ' + HE) if s.get('ots') else (SHE if not male else HE)
    if s.get('cu'): people += ' The thin soft-focus sliver of the other person at the frame edge stays still and out of focus, never turns, never shows a face and does not speak.'
    body = s['act'] + ' ' + say + ' ' + people + ' ' + axis(s) + ' ' + PROPS + ' ' + ONLY2 + ' One single continuous camera take: no cut, no dissolve, no morph, no zoom. Faces, hair, clothes and props keep exactly the first frame shape, colour and rendering in every frame. ' + STYLE
    return run('native-' + s['key'], 'bytedance/seedance-2.5/image-to-video', 'multimodal.generate.video', dict(image=upload(V / 'frames' / f"{s['key']}.png"), prompt=body, duration=s['ndur'], resolution='720p', generate_audio=True, **({'last_image': upload(V / 'frames' / f"{s['last']}.png")} if s.get('last') else {})), V / 'takes' / f"{s['key']}_n.mp4")
def lip(s):
    return run('lip-' + s['key'], 'sync/lipsync-3', 'multimodal.generate.video', dict(video=upload(V / 'takes' / f"{s['key']}.mp4"), audio=upload(V / 'audio' / f"dub-{s['key']}.wav")), V / 'takes' / f"{s['key']}_ls.mp4")
if __name__ == '__main__':
    cmd, only = sys.argv[1], sys.argv[2:]
    sel = [s for s in SHOTS if not only or s['key'] in only]
    with ThreadPoolExecutor(6) as ex:
        if cmd == 'plates': fs = [ex.submit(image, k, v[1], v[0]) for k, v in PLATES.items() if not only or k in only]
        elif cmd == 'frames': fs = [ex.submit(frame, s) for s in sel]
        elif cmd == 'takes': fs = [ex.submit(take, s) for s in sel]
        elif cmd == 'native': fs = [ex.submit(native, s) for s in sel if s['lines']]
        elif cmd == 'lip': fs = [ex.submit(lip, s) for s in sel if s['lines']]
        for f in fs: print(*f.result(), flush=True)
