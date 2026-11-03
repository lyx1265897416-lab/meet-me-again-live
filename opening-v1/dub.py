# -*- coding: utf-8 -*-
"""从原片取 D1/B 台词，按每镜的开口时间排成对口型用的配音轨。"""
import subprocess
from pathlib import Path
V = Path(__file__).resolve().parent
exec((V / 'shots.py').read_text())
P = Path('/Users/vicky/Interactive storyline/projects/meet-me-again-deepspace-20261013/interactive-video-v1/media')
FF = '/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1'
SRC = {'01-02': '01-02-01.mp4', '01-03': '01-03-01.mp4', '01-04': '01-04-01.mp4'}
for k, (sid, a, b, *_ ) in LINES.items():
    subprocess.run([FF, '-y', '-v', 'error', '-ss', str(a), '-t', str(b - a), '-i', str(P / SRC[sid]), '-vn', '-ac', '2', '-ar', '48000',
                    '-af', 'afade=t=in:st=0:d=0.02,afade=t=out:st=%.3f:d=0.04' % (b - a - .04), str(V / 'audio' / f'{k}.wav')], check=True)
for s in SHOTS:
    if not s['lines']: continue
    k, off = s['lines'][0]
    subprocess.run([FF, '-y', '-v', 'error', '-f', 'lavfi', '-t', str(s['dur']), '-i', 'anullsrc=r=48000:cl=stereo', '-i', str(V / 'audio' / f'{k}.wav'), '-filter_complex',
                    '[1:a]adelay=%d|%d[d];[0:a][d]amix=inputs=2:duration=first:dropout_transition=0,volume=2[a]' % (off * 1000, off * 1000), '-map', '[a]', str(V / 'audio' / f"dub-{s['key']}.wav")], check=True)
print('ok')
