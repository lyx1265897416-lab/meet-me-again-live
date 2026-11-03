# -*- coding: utf-8 -*-
"""合成：按 shots.py 的 take 窗口剪，对白用原 D1/B，环境声+音效+配乐分轨，字幕不烧进画面。"""
import json, subprocess
from pathlib import Path
V = Path(__file__).resolve().parent
exec((V / 'shots.py').read_text())
import sys
import numpy as np
MODE = sys.argv[1] if len(sys.argv) > 1 else 'raw'; TAG = 'V12A' if MODE == 'raw' else 'V12B'
WORDS = json.load(open(V / 'qa/native_words.json'))
import importlib.util as _iu
_sp = _iu.spec_from_file_location('grade', V / 'grade.py'); GRADE = _iu.module_from_spec(_sp); _sp.loader.exec_module(GRADE)
GP = {k: v for k, v in json.load(open(V / 'qa/grade.json')).items() if not k.startswith('_')}
FF = '/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1'
MUSIC = '/Users/vicky/Interactive storyline/projects/meet-me-again-deepspace-20261013/interactive-video-v1/voices/music/daylight.mp3'
E = V / 'edit'; E.mkdir(exist_ok=True)
def ff(*a): subprocess.run([FF, '-y', '-v', 'error', *map(str, a)], check=True)
parts, t, cues, dlg, starts = [], 0.0, [], [], {}
wins = {}
for s in SHOTS:
    a, b = NWIN.get(s['key'], s['take']); starts[s['key']] = t
    src = V / 'takes' / (s.get('src', s['key']) + ('_n' if s['lines'] else '') + '.mp4')  # dialogue shots are native performances (V3), no lipsync
    o = E / f"{s['key']}.mp4"
    SC = 'scale=720:1280:force_original_aspect_ratio=increase:flags=lanczos,crop=720:1280,fps=24,'
    ENC = ['-c:v', 'libx264', '-preset', 'slow', '-crf', 17, '-bf', 0, '-r', 24]
    if s.get('fast') or s.get('head'):  # (split, speed): one side plays faster so the beat stays quick and the shot still meets its pinned frame
        x, sp = s.get('fast') or s['head']; sa, sb = (1, sp) if s.get('fast') else (sp, 1)
        dur = (x - a) / sa + (b - x) / sb; nf = round(dur * 24); dur = nf / 24
        ff('-i', src, '-an', '-filter_complex', f'[0:v]{SC}split[p][q];[p]trim=start={a}:end={x},setpts=(PTS-STARTPTS)/{sa}[p1];[q]trim=start={x}:end={b},setpts=(PTS-STARTPTS)/{sb}[q1];[p1][q1]concat=n=2:v=1:a=0,fps=24,tpad=stop_mode=clone:stop=4,setsar=1,format=yuv420p[v]', '-map', '[v]', '-frames:v', nf, *ENC, o)
    else:
        nf = round((b - a) * 24); dur = nf / 24
        ff('-i', src, '-an', '-vf', SC + f'trim=start_frame={round(a*24)},setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop=4,setsar=1,format=yuv420p', '-frames:v', nf, *ENC, o)
    if GP.get(s['key']):  # V8: grade every shot to the S08e look (grade.py)
        g = E / f"{s['key']}_g.mp4"; GRADE.apply(o, g, GP[s['key']]); o = g
    parts.append(o)
    wins[s['key']] = (a, t)
    if s['lines']:
        k = s['lines'][0][0]; sid, x, y, who, en, zh = LINES[k]; w = WORDS[s['key']]['words']
        dlg.append((V / 'audio' / f"{'vc' if MODE == 'vc' else 'raw'}-{s['key']}.wav", a, dur + s.get('atail', 0), t, 1.0, max(0, w[0][1] - a - .12)))
        cues.append(dict(s=round(t + w[0][1] - a, 2), e=round(t + w[-1][2] - a, 2), who=who, en=en, zh=zh))
    else:  # V5: native sound of the take stays (her gasp, the catch, the sign falling, breaths)
        tail = {'S02b': .35}.get(s['key'], 0); gain = {'S04a': .7, 'S02b': .8, 'S03f': 1.6}.get(s['key'], 1.0)
        dlg.append((src, a, dur + tail, t, gain, 0))
    t += dur
TOTAL = t
ff(*sum([['-i', p] for p in parts], []), '-filter_complex', ''.join(f'[{i}:v]' for i in range(len(parts))) + f'concat=n={len(parts)}:v=1:a=0,fps=24[v]', '-map', '[v]', '-c:v', 'libx264', '-preset', 'slow', '-crf', 16, '-pix_fmt', 'yuv420p', '-bf', 0, E / 'video.mp4')
def bed(items, out):
    a = ['-f', 'lavfi', '-t', TOTAL, '-i', 'anullsrc=r=48000:cl=stereo']; ch = []; lb = ['[0:a]']
    for i, (p, at, gain) in enumerate(items, 1):
        a += ['-i', p]; ch.append(f'[{i}:a]aresample=48000,volume={gain}dB,adelay={int(at*1000)}|{int(at*1000)}[d{i}]'); lb.append(f'[d{i}]')
    ff(*a, '-filter_complex', ';'.join(ch + [''.join(lb) + f'amix=inputs={len(lb)}:duration=first:normalize=0[o]']), '-map', '[o]', '-ac', 2, '-ar', 48000, out)
segs = []
for i, (p, a, d, at, g, gate) in enumerate(dlg):  # V12: gate = silence before the first word of a dialogue shot; light denoise on every native track
    fade = f'afade=t=in:st={gate:.3f}:d=0.08' if gate else 'afade=t=in:d=0.02'
    o = E / f'dlg{i}.wav'; ff('-ss', a, '-t', d, '-i', p, '-vn', '-af', f'afftdn=nf=-30,volume={g},{fade},afade=t=out:st={d-.04:.3f}:d=0.04', '-ac', 2, '-ar', 48000, o); segs.append((o, at, 0))
def fx(n, peak):
    q = subprocess.run([FF, '-v', 'error', '-i', V / 'sound/fx' / f'{n}.mp3', '-ac', '1', '-f', 'f32le', '-'], capture_output=True).stdout
    return V / 'sound/fx' / f'{n}.mp3', 20 * np.log10(peak / max(1e-4, float(np.abs(np.frombuffer(q, np.float32)).max())))
def T(key, src_t): return wins[key][1] + src_t - wins[key][0]
def N(n, peak, at): f, g = fx(n, peak); return (f, at, round(float(g), 1))
def Tin(key, src_t):  # only beats that fall inside the shot's window
    a0, t0 = wins[key]; d = NWIN.get(key, dict((x['key'], x['take']) for x in SHOTS)[key]); return t0 + src_t - a0 if d[0] <= src_t < d[1] else None
END13 = WORDS['S13c']['words'][-1][2]
EFFORT = [N('m_huff', .22, starts['S04a'] + .85), N('m_chuckle', .2, T('S13c', END13 + .25))]  # V6: her smiling sounds removed
segs += EFFORT
bed(segs, E / 'dialogue.wav')
ff('-stream_loop', -1, '-i', V / 'sound/amb.mp3', '-t', TOTAL, '-af', f'aresample=48000,volume=-14dB,afade=t=in:st=0:d=1,afade=t=out:st={TOTAL-1.2:.2f}:d=1.2', '-ac', 2, E / 'ambience.wav')
BEATS = [N('creak', .07, .15),
 (V / 'sound/sfx_water.mp3', starts['S03b'], -16),
 N('rustle_f', .12, T('S03b', .3)), N('can_tap', .14, T('S03b', .45)),
 N('rustle_j', .12, starts['S04a'] + .3), N('wood_shift', .12, starts['S04a'] + .55),
 N('wood_shift', .1, T('S04b', 1.9)),
 N('can_lift', .2, Tin('S05c', .3)),
 N('wood_shift', .14, Tin('S06c', 4.6)),
 N('wood_set', .12, Tin('S08c', .9)),
]
BEATS = [x for x in BEATS if x[1] is not None]
bed(BEATS, E / 'sfx.wav')
ff('-i', MUSIC, '-t', TOTAL, '-af', f'aresample=48000,volume=-20dB,afade=t=in:st=0:d=2.5,afade=t=out:st={TOTAL-3:.2f}:d=3', '-ac', 2, E / 'bgm.wav')
ff('-i', E / 'video.mp4', '-i', E / 'dialogue.wav', '-i', E / 'ambience.wav', '-i', E / 'sfx.wav', '-i', E / 'bgm.wav', '-filter_complex',
   '[4:a][1:a]sidechaincompress=threshold=0.03:ratio=8:attack=25:release=500[b];[1:a]volume=1.0[d];[d][2:a][3:a][b]amix=inputs=4:duration=first:normalize=0,alimiter=limit=0.95[a]',
   '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', V / f'delivery/MMA3P_OPENING_{TAG}.mp4')
def ts(x): return '%02d:%02d:%06.3f' % (x // 3600, x // 60 % 60, x % 60)
(V / f'delivery/MMA3P_OPENING_{TAG}.zh-en.vtt').write_text('WEBVTT\n\n' + ''.join(f"{ts(c['s'])} --> {ts(c['e'])}\n{c['zh']}\n{c['en']}\n\n" for c in cues))
(V / f'delivery/cues-{TAG}.json').write_text(json.dumps(cues, ensure_ascii=False, indent=1))
print('TOTAL', round(TOTAL, 2), starts)
