# S12: only Rowan speaks but lipsync picks the frontal face (Maisie). Lip-sync a crop that contains only him, then paste it back with a soft edge.
import sys, numpy as np, cv2, subprocess
sys.argv = ['gen.py', 'noop']
src = open('gen.py').read().split("if __name__ == '__main__':")[0]
exec(src)
print(run('lip-S12crop', 'sync/lipsync-3', 'multimodal.generate.video', dict(video=upload(V / 'takes/S12crop.mp4'), audio=upload(V / 'audio/dub-S12.wav')), V / 'takes/S12crop_ls.mp4'))
a, b = cv2.VideoCapture('takes/S12.mp4'), cv2.VideoCapture('takes/S12crop_ls.mp4')
x0, y0, w, h = 370, 60, 350, 440
m = np.zeros((h, w), np.float32); cv2.ellipse(m, (w // 2 + 20, h // 2 - 20), (120, 150), 0, 0, 360, 1, -1); m = cv2.GaussianBlur(m, (0, 0), 18)[..., None]
out = cv2.VideoWriter('takes/S12_tmp.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 24, (720, 1280)); n = 0
while True:
    ok, f = a.read()
    if not ok: break
    ok2, g = b.read()
    if ok2:
        if g.shape[:2] != (h, w): g = cv2.resize(g, (w, h))
        r = f[y0:y0 + h, x0:x0 + w].astype(np.float32); f[y0:y0 + h, x0:x0 + w] = (r * (1 - m) + g.astype(np.float32) * m).astype(np.uint8)
    out.write(f); n += 1
out.release(); print('frames', n)
subprocess.run(['/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1', '-y', '-v', 'error', '-i', 'takes/S12_tmp.mp4', '-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', 'takes/S12_ls.mp4'], check=True)
