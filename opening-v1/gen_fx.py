# -*- coding: utf-8 -*-
"""V5 动作与表情音效（Vicky：女主惊讶要有声音，表情/动态都要有对应音效）。原生音轨已有的不重做。"""
import subprocess, os, concurrent.futures
from pathlib import Path
os.environ['PATH'] = '/Users/vicky/.local/bin:/Users/vicky/.waku/bin:/opt/homebrew/bin:' + os.environ['PATH']
D = Path(__file__).resolve().parent / 'sound/fx'
FX = {
 'creak': ("an old wooden sign creaking gently on small iron chains in a light sea breeze, outdoors, sparse", 3),
 'can_lift': ("a metal watering can lifted by its handle: small handle creak and a little water sloshing inside, close, short", 1.2),
 'can_tap': ("a metal watering can handle softly clinks once, tiny, close", .6),
 'rustle_j': ("soft suede jacket sleeve rustle from one arm movement, close, short, quiet", .7),
 'rustle_f': ("soft cotton puff sleeve fabric rustle from one quick movement, close, short, quiet", .6),
 'wood_set': ("a wooden board set down and leaned against a stone wall: soft wooden knock and small scrape, outdoors", 1),
 'wood_shift': ("a wooden board shifting in two hands, small wooden creak, close", .7),
 'pocket': ("two hands sliding into jacket pockets, soft fabric rustle, close", .7),
 'step': ("a single soft shoe step backward on cobblestone, outdoors", .5),
 'f_exhale': ("a young woman's short amused exhale through the nose, a stifled laugh with closed lips, no words, dry close recording", .8),
 'f_hm': ("a young woman's very short sceptical hm through closed lips, no words, dry close recording", .7),
 'm_chuckle': ("a young man's soft short self-mocking breathy chuckle through the nose with closed lips, no words, dry close recording", 1.2),
 'm_inhale': ("a young man's short soft delighted intake of breath, no words, dry close recording", .6),
 'm_huff': ("a young man's short relieved huff of breath out, no words, dry close recording", .7),
}
def one(k):
    p, d = FX[k]; out = D / f'{k}.mp3'
    if out.exists() and out.stat().st_size > 1000: return k, 'cached'
    r = subprocess.run(['waku', 'gen', 'sfx', p, '--duration', str(d), '--out', str(out)], capture_output=True, text=True, timeout=500)
    return k, 'ok' if out.exists() else 'FAIL ' + (r.stdout + r.stderr)[-200:]
with concurrent.futures.ThreadPoolExecutor(5) as e:
    for k, s in e.map(one, FX): print(k, s, flush=True)
