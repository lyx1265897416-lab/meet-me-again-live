# -*- coding: utf-8 -*-
"""原生演出后处理：取每镜声音 → chatterbox 变声到选定的 R1/W2 → 校验节奏没变（包络相关度）。结果在 audio/vc-<镜>.wav。"""
import json, subprocess, sys, os
from pathlib import Path
import numpy as np
src = open('gen.py').read().split("if __name__ == '__main__':")[0]
exec(src)
FF = '/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1'
VO = V.parent / 'voices-v2'
REF = {'Rowan': VO / 'audio/R1.mp3', 'Maisie': VO / 'audio/W2.mp3'}
def env(path):
    p = subprocess.run([FF, '-v', 'error', '-i', str(path), '-ac', '1', '-ar', '8000', '-f', 'f32le', '-'], capture_output=True)
    y = np.frombuffer(p.stdout, np.float32); n = 80
    return np.sqrt(np.convolve(y ** 2, np.ones(n) / n, 'valid'))[::n]
def one(s):
    key = s['key']; who = LINES[s['lines'][0][0]][3]
    raw = V / 'audio' / f'raw-{key}.wav'; out = V / 'audio' / f'vc-{key}.wav'
    subprocess.run([FF, '-y', '-v', 'error', '-i', str(V / 'takes' / f'{key}_n.mp4'), '-vn', '-ac', '2', '-ar', '48000', str(raw)], check=True)
    if not out.exists():
        tmp = V / 'audio' / f'vc-{key}.mp3'
        n, st = run('vc-' + key, 'chatterbox/speech-to-speech', 'multimodal.generate.audio', dict(audio=upload(raw), reference_audio=upload(REF[who])), tmp)
        if 'FAIL' in st: return key, st
        subprocess.run([FF, '-y', '-v', 'error', '-i', str(tmp), '-ac', '2', '-ar', '48000', str(out)], check=True)
    a, b = env(raw), env(out); m = min(len(a), len(b)); c = np.corrcoef(a[:m], b[:m])[0, 1]
    return key, f'env corr {c:.2f}, raw {len(a)/100:.2f}s vc {len(b)/100:.2f}s'
if __name__ == '__main__':
    only = sys.argv[1:]
    sel = [s for s in SHOTS if s['lines'] and (not only or s['key'] in only)]
    with ThreadPoolExecutor(4) as ex:
        for k, r in ex.map(one, sel): print(k, r, flush=True)
