# -*- coding: utf-8 -*-
"""第三人称开场音色候选 V1：minimax/voice-design 按描述新设计。男 6、女 6，每位念本剧开场自己的台词。"""
import json, subprocess, os, uuid, concurrent.futures
from pathlib import Path
D = Path(__file__).resolve().parent
os.environ['PATH'] = '/Users/vicky/.local/bin:/Users/vicky/.waku/bin:/opt/homebrew/bin:' + os.environ['PATH']
TM = "This? Your toes might have a problem with that. ... Okay. Just so we are clear, I am not waterproof. ... I'm Rowan. Here to fix the sign. ... Bad introduction. Want me to start over?"
TF = "Put it down. ... The sign. Put it down, and take a step back. ... You don't look like someone I hired. ... We'll see how you do."
COM = " Native everyday American English. Spontaneous conversation at a garden gate, as if finding the words in the moment: fluid connected speech, contractions, small meaningful pauses, softened unstressed words. Clean dry recording. Avoid radio-host delivery, audiobook narration, robotic even timing, theatrical seduction, exaggerated breathing, music."
MALE = "An original young adult male voice, perceived age 26 to 28. "
FEM = "An original young adult female voice, perceived age 24 to 26. "
C = [
 ('M1', 'Rowan', '明亮暖男', 'bright warm, smile in the voice', MALE + "A warm bright baritenor with an audible smile, open and sunny. A playful rom-com lead who teases kindly, quick on the joke, then sincere." + COM, TM),
 ('M2', 'Rowan', '邻家清爽', 'light boy-next-door tenor', MALE + "A light clean tenor, boy-next-door, breezy and friendly, slightly nervous energy hidden behind good humour, youthful and unforced." + COM, TM),
 ('M3', 'Rowan', '松弛低调', 'mellow relaxed baritone', MALE + "A mellow medium baritone, relaxed and low-key, dry understated humour with a deadpan edge, never pushing a joke, warm underneath." + COM, TM),
 ('M4', 'Rowan', '微哑慵懒', 'slightly husky, unhurried', MALE + "A warm slightly husky mid-range voice, unhurried, a gentle natural grain without forced rasp, teasing softly, confident without being smug." + COM, TM),
 ('M5', 'Rowan', '清亮利落', 'crisp and lively', MALE + "A clear crisp youthful voice with lively rhythm and bounce, quick comic timing, expressive rises and falls, charming and quick-witted, energetic but conversational." + COM, TM),
 ('M6', 'Rowan', '温柔克制', 'soft-spoken, tender', MALE + "A soft-spoken gentle warm voice, intimate speaking volume but not whispering, careful and tender under the jokes, as if he already knows her and is hiding it." + COM, TM),
 ('F1', 'Maisie', '清冷警惕', 'clear, cool, guarded', FEM + "A clear mid-range voice, cool and guarded at first, dry and level, firm without shouting, intelligence and a hint of humour underneath." + COM, TF),
 ('F2', 'Maisie', '低沉微哑', 'warm alto, slight husk', FEM + "A warm low-mid alto with a slight natural husk, grounded and unimpressed, wry, relaxed authority, not sultry." + COM, TF),
 ('F3', 'Maisie', '清甜有力', 'bright sweet but firm', FEM + "A bright sweet light voice with a firm backbone, youthful and clear, trying hard to sound stern and almost succeeding, charming without being childish." + COM, TF),
 ('F4', 'Maisie', '温柔谨慎', 'soft, careful', FEM + "A soft gentle voice, careful and a little uncertain, quiet but steady, tender tone with a thread of wariness, normal speaking volume, not breathy." + COM, TF),
 ('F5', 'Maisie', '干脆利落', 'crisp, sharp humour', FEM + "A crisp confident voice, quick and direct, sharp dry humour, clean consonants, a young woman who runs her own business and does not suffer fools." + COM, TF),
 ('F6', 'Maisie', '自然邻家', 'natural girl-next-door', FEM + "A natural easygoing girl-next-door voice, warm and unpolished, ordinary and real, cautious right now but ready to laugh." + COM, TF),
]
def run(c):
    k, role, zh, en, prompt, text = c
    params = dict(custom_voice_id=f'MeetMe{k}V1{uuid.uuid4().hex[:6]}', prompt=prompt, text=text)
    out = D / 'audio' / f'{k}.mp3'
    p = subprocess.run(['waku', 'gen', 'run', 'minimax/voice-design', '--capability', 'multimodal.generate.audio', '--params', json.dumps(params), '--wait', '--out', str(out)], capture_output=True, text=True, timeout=500)
    (D / 'receipts' / f'{k}.json').write_text(p.stdout + '\n--\n' + p.stderr)
    print(k, p.returncode, out.exists() and out.stat().st_size, flush=True)
    return dict(key=k, role=role, zh=zh, en=en, voice_id=params['custom_voice_id'], prompt=prompt, text=text, file=f'audio/{k}.mp3')
with concurrent.futures.ThreadPoolExecutor(4) as e: rec = list(e.map(run, C))
(D / 'manifest.json').write_text(json.dumps(rec, ensure_ascii=False, indent=1))
