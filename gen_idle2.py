"""待机循环 V2：Vivix 首尾锁同一帧会在中间换衣服换背景（qa/IDLE0-vivix-morph.mp4），改用 Seedance 2.5 只给首帧，生成 5 秒几乎不动的画面，再正放 + 倒放拼成无缝循环。"""
import subprocess, sys
from pathlib import Path
D = Path(__file__).resolve().parent; O = D / 'opening-v1'
sys.argv = ['gen.py', 'noop']; G = {'__file__': str(O / 'gen.py'), '__name__': 'genlib'}
exec(open(O / 'gen.py').read().split("if __name__ == '__main__':")[0], G)
P = ('Locked-off tripod camera, one continuous take, the framing never changes, no zoom, no cut. The same young man, same face, hair, warm brown suede jacket and cream cable-knit sweater as the first frame, '
     'quietly waiting for the woman\'s answer: his eyes stay open and on her, just left of the camera; a small hopeful smile; only subtle natural breathing in his shoulders, one natural blink, hair stirring slightly in the sea breeze. '
     'Lips closed, no speaking, no gestures, no head turn. The soft out-of-focus strands of her hair at the left edge stay still. Same background, colours and warm sunlight as the first frame in every frame. No music.')
print(G['run']('idle-loop', 'bytedance/seedance-2.5/image-to-video', 'multimodal.generate.video', dict(image=G['upload'](O / 'frames/IDLEK.png'), prompt=P, duration=5, resolution='720p', generate_audio=False), D / 'qa/idle_raw.mp4'))
FF = '/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1'
subprocess.run([FF, '-y', '-v', 'error', '-i', str(D / 'qa/idle_raw.mp4'), '-filter_complex', '[0:v]trim=0:3.6,setpts=PTS-STARTPTS,scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,fps=24,split[a][b];[b]reverse[r];[a][r]concat=n=2:v=1:a=0,format=yuv420p[v]',
                '-map', '[v]', '-an', '-c:v', 'libx264', '-crf', '19', '-movflags', '+faststart', str(D / 'docs/media/IDLE0.mp4')], check=True)
print('idle ok')
