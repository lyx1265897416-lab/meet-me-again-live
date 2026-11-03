# -*- coding: utf-8 -*-
"""第三批音色：Vicky 说前两批（minimax/voice-design）太人机，要真实自然。按路子横向比：Seedance 原生演出、Seed Audio、Eleven v4 预置音色、Gemini 3.8 导演式、双人对戏。"""
import json, subprocess, os, sys, concurrent.futures, hashlib, time
from pathlib import Path
D = Path(__file__).resolve().parent; O = D.parent / 'opening-v1'
os.environ['PATH'] = '/Users/vicky/.local/bin:/Users/vicky/.waku/bin:/opt/homebrew/bin:' + os.environ['PATH']
FF = '/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1'
TM = "This? Your toes might have a problem with that. Okay. Just so we are clear, I am not waterproof. Bad introduction. Want me to start over?"
TF = "Put it down. The sign. Put it down, and take a step back. You don't look like someone I hired."
TME = "[amused] This? Your toes might have a problem with that. [short pause] Okay. Just so we are clear, [deadpan] I am not waterproof. [short pause] [laughs at himself] Bad introduction. Want me to start over?"
TFE = "[firm] Put it down. [impatient] The sign. Put it down, and take a step back. [dry, unimpressed] You don't look like someone I hired."
REAL = "A real person talking off the cuff, not a voice actor and not reading: uneven thought-led rhythm, words running together, little breaths where a person would really breathe, pitch that moves with the thought, nothing polished. Ordinary conversational volume, General American."
STYLE_M = "Playful, quick and a little self-mocking, trying to make a wary stranger smile. " + REAL
STYLE_F = "Wary and dry, not shouting, holding a watering can like a weapon at a stranger; a little amused despite herself by the end. " + REAL
def waku(args, t=560):
    p = subprocess.run(['waku'] + args, capture_output=True, text=True, timeout=t); return p
def audio(k, model, params):
    out = D / 'audio' / f'{k}.mp3'
    if out.exists() and out.stat().st_size > 3000: return k, 'cached'
    p = waku(['gen', 'run', model, '--capability', 'multimodal.generate.audio', '--params', json.dumps(params, ensure_ascii=False), '--wait', '--out', str(out)])
    (D / 'receipts' / f'{k}.json').write_text(p.stdout + '\n--\n' + p.stderr)
    return k, 'ok' if out.exists() and out.stat().st_size > 3000 else 'FAIL ' + (p.stdout + p.stderr)[-220:]
def upload(path):
    sha = hashlib.sha256(Path(path).read_bytes()).hexdigest(); rec = O / 'inputs' / (sha + '.json')
    if rec.exists(): return json.loads(rec.read_text())['url']
    p = waku(['persist', str(path)]); u = json.loads(p.stdout[p.stdout.find('{'):])['url']; rec.write_text(json.dumps(dict(url=u))); return u
def seedance(k, frame, who, voice, line, dur):
    out = D / 'audio' / f'{k}.mp3'; vid = D / 'video' / f'{k}.mp4'
    if out.exists(): return k, 'cached'
    prompt = f'Fixed camera. {who} speaks aloud on camera, in English, exactly these words once each, in order, with natural pauses and real acting: "{line}" {voice} Only this one person speaks. No music, no background voices. Natural breathing, small head and shoulder movement with the words. Keep the same face, hair, clothes and rendering as the first frame.'
    p = waku(['gen', 'run', 'bytedance/seedance-2.5/image-to-video', '--capability', 'multimodal.generate.video', '--params', json.dumps(dict(image=upload(O / 'frames' / frame), prompt=prompt, duration=dur, resolution='720p', generate_audio=True)), '--wait', '--out', str(vid)], 590)
    (D / 'receipts' / f'{k}.json').write_text(p.stdout + '\n--\n' + p.stderr)
    if not vid.exists(): return k, 'FAIL ' + (p.stdout + p.stderr)[-220:]
    subprocess.run([FF, '-y', '-v', 'error', '-i', str(vid), '-vn', '-c:a', 'libmp3lame', '-b:a', '160k', str(out)], check=True); return k, 'ok'
def seed(k, direction, text): return audio(k, 'bytedance/seed-audio-1.0', dict(prompt=f'{direction} {REAL} Say exactly, once: "{text}"', output_format='mp3'))
def eleven(k, voice, text): return audio(k, 'elevenlabs/eleven-v4', dict(text=text, voice_id=voice, stability=.3, similarity=.75))
def gem(k, voice, text, style): return audio(k, 'google/gemini-3.8-flash/text-to-speech', dict(text=text, voice=voice, style_instructions=style))
JOBS = [
 (seedance, 'R1', 'S10.png', 'The young man', 'A warm, natural young American male voice, relaxed and amused, a smile in it.', TM, 9),
 (seedance, 'R2', 'S10.png', 'The young man', 'A natural medium-low young American male voice, dry and easygoing, understated.', TM, 9),
 (seed, 'R3', 'A fictional American man aged twenty-seven. Warm buoyant light baritone, relaxed smiling phrasing, comfortable everyday conversation.', TM),
 (seed, 'R4', 'A fictional American man aged twenty-seven. Clear casual mid voice with a slight husk, dry humour, quick and unforced.', TM),
 (eleven, 'R5', 'Will', TME), (eleven, 'R6', 'Liam', TME), (eleven, 'R7', 'Chris', TME),
 (gem, 'R8', 'Zubenelgenubi', TM, STYLE_M), (gem, 'R9', 'Achird', TM, STYLE_M),
 (seedance, 'W1', 'S07.png', 'The young woman', 'A natural young American female voice, clear and dry, wary and firm without shouting.', TF, 7),
 (seedance, 'W2', 'S07.png', 'The young woman', 'A natural warm low-mid young American female voice, unimpressed, quietly sharp.', TF, 7),
 (seed, 'W3', 'A fictional American woman aged twenty-five. Crisp confident mid voice, runs her own shop, direct and dry, everyday conversation.', TF),
 (seed, 'W4', 'A fictional American woman aged twenty-five. Warm natural voice with a little grain, cautious and wry, everyday conversation.', TF),
 (eleven, 'W5', 'Jessica', TFE), (eleven, 'W6', 'Sarah', TFE), (eleven, 'W7', 'Matilda', TFE),
 (gem, 'W8', 'Callirrhoe', TF, STYLE_F), (gem, 'W9', 'Kore', TF, STYLE_F),
]
S0, S1 = 'A', 'B'
TURNS = [(S1, 'Put it down.'), (S0, 'This? Your toes might have a problem with that.'), (S1, 'The sign. Put it down, and take a step back.'), (S0, 'Okay. Just so we are clear, I am not waterproof.'), (S0, "I'm Rowan. Here to fix the sign."), (S1, "You don't look like someone I hired."), (S0, 'Bad introduction. Want me to start over?')]
def duo_gem(k, vm, vf):
    return audio(k, 'google/gemini-3.8-flash/text-to-speech', dict(text='', speakers=[dict(speaker_id='Rowan', voice=vm), dict(speaker_id='Maisie', voice=vf)], turns=[dict(speaker_id='Rowan' if a == 'A' else 'Maisie', text=t) for a, t in TURNS], style_instructions='Two strangers at a garden gate, overlapping energy, quick natural turn-taking, real people not voice actors. He is playful and self-mocking, she is wary and dry. ' + REAL))
def duo_vibe(k, vm, vf):
    return audio(k, 'microsoft/vibevoice', dict(prompt='\n'.join(('Speaker 0: ' if a == 'A' else 'Speaker 1: ') + t for a, t in TURNS), speaker_1=vm, speaker_2=vf))
JOBS += [(duo_gem, 'D1', 'Zubenelgenubi', 'Callirrhoe'), (duo_vibe, 'D2', 'en-Carter_man', 'en-Maya_woman'), (duo_vibe, 'D3', 'en-Frank_man', 'en-Alice_woman')]
only = set(sys.argv[1:])
with concurrent.futures.ThreadPoolExecutor(5) as e:
    fs = [e.submit(j[0], *j[1:]) for j in JOBS if not only or j[1] in only]
    for f in concurrent.futures.as_completed(fs): print(*f.result(), flush=True)
