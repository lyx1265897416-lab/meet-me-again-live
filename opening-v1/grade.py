# -*- coding: utf-8 -*-
"""V8 色调统一：以 S08e（Vicky 指定的图 2）为准，逐镜在 LAB 里调饱和度（色度倍数）、白平衡（a/b 平移）和亮度（L 的 gamma）。
统计时去掉过肩镜的前景人物（她的镜头去右侧 30%，他的镜头去左侧 30%）；每项都有上限，只统一、不改画风。"""
import cv2, numpy as np, json, sys, subprocess
from pathlib import Path
V = Path(__file__).resolve().parent
exec((V / 'shots.py').read_text())
REF = 'S08e'
def region(s, f):
    w = f.shape[1]
    if s.get('ots'): return f[:, :int(w * .7)] if 'HER' in s['frame'][:0] or s.get('plate') == 'P_HER' else f[:, int(w * .3):]
    return f
def sample(s, n=8):
    src = V / 'takes' / (s.get('src', s['key']) + ('_n' if s['lines'] else '') + '.mp4')
    a, b = NWIN.get(s['key'], s['take']); c = cv2.VideoCapture(str(src)); fps = c.get(5); out = []
    for t in np.linspace(a + .1, b - .1, n):
        c.set(1, int(t * fps)); ok, f = c.read()
        if ok: out.append(region(s, cv2.resize(f, (360, 640))))
    return out
def stats(fs):
    lab = np.concatenate([cv2.cvtColor(f, cv2.COLOR_BGR2LAB).reshape(-1, 3).astype(float) for f in fs])
    hsv = np.concatenate([cv2.cvtColor(f, cv2.COLOR_BGR2HSV).reshape(-1, 3).astype(float) for f in fs])
    L = lab[:, 0] * 100 / 255; a = lab[:, 1] - 128; b = lab[:, 2] - 128; m = L > 35  # leave out dark clothes and shadows
    return dict(L=float(np.median(L[m])), a=float(a[m].mean()), b=float(b[m].mean()), S=float(hsv[m, 1].mean()))
def face_L(s):
    if s['key'] in ('S01', 'S02b'): return None
    box = {'P_HER': (.08, .55), 'P_HIM': (.42, .88)}.get(s.get('plate') if s.get('ots') else '', (.25, .75))
    vals = []
    for f in sample(dict(s, ots=False), 6):
        h, w = f.shape[:2]; c = f[int(h * .1):int(h * .42), int(w * box[0]):int(w * box[1])]
        L = cv2.cvtColor(c, cv2.COLOR_BGR2LAB)[..., 0].astype(float) * 100 / 255; vals.append(np.percentile(L, 75))  # skin and hair highlights, not background
    return float(np.median(vals))
def params():
    by = {s['key']: s for s in SHOTS}; by.setdefault(REF, V7[REF]); r = stats(sample(by[REF])); P = {}
    for s in SHOTS:
        st = stats(sample(s)); k = s['key']
        if k == 'S02b':  # sky close-up: its colour statistics are content, not grading
            P[k] = dict(sat=1.0, da=0.0, db=0.0, gamma=1.0, why='sky shot, left as is', before=st); continue
        sat = float(np.clip(r['S'] / st['S'], .97, 1.3))  # perceived saturation (HSV); never wash a shot out
        da = float(np.clip(r['a'] - st['a'], -3, 3)) * .5; db = float(np.clip(r['b'] - st['b'], -3, 3)) * .5
        fl, rl = face_L(s), face_L(by[REF])  # brightness follows the face the viewer is watching
        gamma = 1.0 if fl is None else float(np.clip(np.log(rl / 100) / np.log(fl / 100), .9, 1.1))
        P[k] = dict(sat=round(sat, 3), da=round(da, 2), db=round(db, 2), gamma=round(gamma, 3), before=st)
    P['_ref'] = r; return P
def apply(src, dst, p):
    c = cv2.VideoCapture(str(src)); fps = c.get(5); w, h = int(c.get(3)), int(c.get(4))
    lut = np.clip(100 * (np.arange(256) * 100 / 255 / 100) ** p['gamma'] * 255 / 100, 0, 255).astype(np.uint8)
    pr = subprocess.Popen(['/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{w}x{h}', '-r', '24', '-i', '-',
                           '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-bf', '0', str(dst)], stdin=subprocess.PIPE)
    while True:
        ok, f = c.read()
        if not ok: break
        lab = cv2.cvtColor(f, cv2.COLOR_BGR2LAB).astype(np.float32)
        lab[..., 0] = cv2.LUT(lab[..., 0].astype(np.uint8), lut)
        lab[..., 1] = (lab[..., 1] - 128 + p['da']) * p['sat'] + 128; lab[..., 2] = (lab[..., 2] - 128 + p['db']) * p['sat'] + 128
        pr.stdin.write(cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR).tobytes())
    pr.stdin.close(); pr.wait()
if __name__ == '__main__':
    P = params(); json.dump(P, open(V / 'qa/grade.json', 'w'), indent=1)
    for k, p in P.items():
        if k != '_ref': print(k, {x: p[x] for x in ('sat', 'da', 'db', 'gamma')}, p.get('why', ''))
