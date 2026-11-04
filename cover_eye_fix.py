"""封面 C1 女主大小眼（Vicky 11-03：画面左边那只眼再大一点点，两眼一致；先改成画面右边那只，她说改错了）。只在那只眼睛周围做局部放大变形，其余像素不动。
用法：python cover_eye_fix.py <放大倍数> <输出>（需要 cv2）"""
import sys, cv2, numpy as np
SRC = 'cover-pick/cover_C1.jpg'
im = cv2.imread(SRC); h, w = im.shape[:2]
cx, cy = 600.0, 594.0          # 画面左边那只眼的虹膜中心，941x1672 坐标（从未修过的 C1 原图改）
rx, ry = 38.0, 26.0            # 影响范围（横、竖半径）
k = float(sys.argv[1])         # 中心处放大倍数
yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
dx, dy = xx - cx, yy - cy
r = np.sqrt((dx / rx) ** 2 + (dy / ry) ** 2)
s = np.where(r < 1, 1 + (k - 1) * (1 - r ** 2) ** 2, 1.0).astype(np.float32)  # 中心放大、边缘平滑回到 1
sy = 1 + (s - 1) * 1.6          # 竖向多放：主要是上眼皮压得低、睁得不够开
mapx = (cx + dx / s).astype(np.float32); mapy = (cy + dy / sy).astype(np.float32)
out = cv2.remap(im, mapx, mapy, cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
cv2.imwrite(sys.argv[2], out, [cv2.IMWRITE_JPEG_QUALITY, 92])
