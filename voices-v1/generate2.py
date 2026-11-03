# -*- coding: utf-8 -*-
"""第二批男主音色：Vicky 选 M5 的方向（清亮利落、喜剧节奏），保留它的底子，每个候选只往一个方向变。女主已定 F5。"""
import json, subprocess, os, uuid, concurrent.futures
from pathlib import Path
D = Path(__file__).resolve().parent
os.environ['PATH'] = '/Users/vicky/.local/bin:/Users/vicky/.waku/bin:/opt/homebrew/bin:' + os.environ['PATH']
TM = "This? Your toes might have a problem with that. ... Okay. Just so we are clear, I am not waterproof. ... I'm Rowan. Here to fix the sign. ... Bad introduction. Want me to start over?"
COM = " Native everyday American English. Spontaneous conversation at a garden gate, as if finding the words in the moment: fluid connected speech, contractions, small meaningful pauses, softened unstressed words. Clean dry recording. Avoid radio-host delivery, audiobook narration, robotic even timing, theatrical seduction, exaggerated breathing, music."
BASE = "An original young adult male voice, perceived age 26 to 28. A clear crisp youthful voice with lively rhythm and bounce, quick comic timing, charming and quick-witted, conversational. "
C = [
 ('M7', '更暖一点', 'warmer', "Same lively clarity but warmer and rounder in tone, a real smile you can hear, friendly more than clever."),
 ('M8', '更低一点', 'a little lower', "Pitched a little lower, a light baritone with fuller chest resonance, keeping the same quick bounce and clean consonants, more grown-up."),
 ('M9', '更年轻活泼', 'younger, livelier', "A touch younger and higher, more playful energy, wide expressive rises and falls, delighted by his own jokes without being silly."),
 ('M10', '更松更懒', 'more laid-back', "Same crisp diction but more laid-back timing, an easy unbothered charm, jokes dropped casually and slightly behind the beat."),
 ('M11', '带点颗粒', 'a little texture', "A faint natural grain at the ends of phrases, slightly lived-in texture without any forced rasp, still clear and quick, a little more masculine."),
 ('M12', '更真诚', 'more sincere', "Quick and funny on the surface, but with an earnest, open sincerity underneath; the last question lands genuinely hopeful, as if her answer really matters to him."),
]
def run(c):
    k, zh, en, extra = c
    prompt = BASE + extra + COM
    params = dict(custom_voice_id=f'MeetMe{k}V2{uuid.uuid4().hex[:6]}', prompt=prompt, text=TM)
    out = D / 'audio' / f'{k}.mp3'
    p = subprocess.run(['waku', 'gen', 'run', 'minimax/voice-design', '--capability', 'multimodal.generate.audio', '--params', json.dumps(params), '--wait', '--out', str(out)], capture_output=True, text=True, timeout=540)
    (D / 'receipts' / f'{k}.json').write_text(p.stdout + '\n--\n' + p.stderr)
    print(k, p.returncode, out.exists() and out.stat().st_size, flush=True)
    return dict(key=k, role='Rowan', zh=zh, en=en, voice_id=params['custom_voice_id'], prompt=prompt, text=TM, file=f'audio/{k}.mp3')
with concurrent.futures.ThreadPoolExecutor(3) as e: new = list(e.map(run, C))
m = json.load(open(D / 'manifest.json')); m = [x for x in m if x['key'] not in {c[0] for c in C}] + new
(D / 'manifest.json').write_text(json.dumps(m, ensure_ascii=False, indent=1))
