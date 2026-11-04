"""封面男主一致性重做（Vicky 11-03：封面男主和定妆不一致）：保留原封面构图、她和场景，只按 rowan.png 重画他的脸和头发。
用法：python3 cover_regen.py → opening-v1/frames/COVER_a.png、COVER_b.png（gpt-image-2/edit，复用 opening-v1/gen.py）"""
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
D = Path(__file__).resolve().parent; O = D / 'opening-v1'
REF = Path('/Users/vicky/Interactive storyline/projects/meet-me-again-deepspace-20261013/storyboard-v1/references')
WANT = sys.argv[1:]; sys.argv = ['gen.py', 'noop']; G = {'__file__': str(O / 'gen.py'), '__name__': 'genlib'}
exec(open(O / 'gen.py').read().split("if __name__ == '__main__':")[0], G)
KEEP = ('Image 1 is the finished cover: keep it exactly — same composition and framing, same pose, same positions (him on the left, her on the right), same garden gate, stone pillar, leather bag, watering can, '
        'flowers, greenhouse, sea and light, and keep HER completely unchanged (face, hair, braid, gold leaf pin and earrings, blouse, olive bodice and skirt). ')
FACE = ('Change only the man: redraw his face and hair so he is clearly the same person as image 2 — long gentle face, defined jaw, straight nose, warm light-brown eyes under soft brows, '
        'soft wavy chestnut-brown hair falling over the forehead (neat soft waves, not spiky, not windswept), clean-shaven, 27 years old, rendered in the same refined realistic 3D CG style as image 2, not anime, not a teenage boy. '
        'Keep his expression: a small warm smile, looking at her. Keep his outfit exactly as in image 1: warm medium-brown suede zip jacket with collar, cream cable-knit sweater, dark trousers with black belt. '
        'Refined 2.5D-leaning-3D romance game CG, warm clear light, full natural saturation. No text, no logo, no watermark. Only these two people.')
TURN = ' Turn his head slightly toward the camera into a three-quarter view so his face is clearly visible with both eyes showing, still looking at her with a small warm smile; his body pose stays the same.'
JOBS = {'COVER_c': [D / 'opening-v1/frames/COVER_b.png', REF / 'rowan.png', D / 'masters/he-upper.png'],
        'COVER_a': [D / 'docs/media/poster.jpg', REF / 'rowan.png'],
        'COVER_b': [D / 'docs/media/poster.jpg', REF / 'rowan.png', D / 'masters/he-upper.png']}
def one(k):
    extra = ' Image 3 is the same man in his outfit, for identity and style.' if len(JOBS[k]) > 2 else ''
    return G['image'](k, [str(x) for x in JOBS[k]], KEEP + FACE + extra + (TURN if k == 'COVER_c' else ''))
with ThreadPoolExecutor(2) as ex:
    for r in ex.map(one, [k for k in (WANT or JOBS)]): print(*r, flush=True)
