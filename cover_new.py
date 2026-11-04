"""新封面候选（Vicky 11-03：重画的封面还是不好，重新出几张让她选）。参考全用她确认过的定妆：CANON-rowan-ep1 + rowan.png（他）、maisie.png + she-full（她）、WARDROBE-canon（他的穿着）、S01（院门和海湾）。
用法：python3 cover_new.py [N1 N2 ...] → opening-v1/frames/CV_N1.png ……（gpt-image-2/edit，复用 opening-v1/gen.py）"""
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
D = Path(__file__).resolve().parent; O = D / 'opening-v1'
R = Path('/Users/vicky/Interactive storyline/projects/meet-me-again-deepspace-20261013/storyboard-v1/references')
WANT = sys.argv[1:]; sys.argv = ['gen.py', 'noop']; G = {'__file__': str(O / 'gen.py'), '__name__': 'genlib'}
exec(open(O / 'gen.py').read().split("if __name__ == '__main__':")[0], G)
REFS = [R / 'CANON-rowan-ep1.png', R / 'rowan.png', R / 'WARDROBE-canon.png', R / 'maisie.png', D / 'masters/she-full.png', R / 'S01-original.png']
HEAD = ('Images 1–3 are ROWAN (image 1 is the approved look: face, hair, smile and render style; image 2 is his face close-up; image 3 is his outfit). Images 4–5 are MAISIE (image 4 her face, hair and earrings; image 5 her full outfit). '
        'Image 6 is the place: the seaside cottage garden with the low dry-stone wall, sage-green wooden gate, glass greenhouse with wisteria and the blue bay. They are references only: do not copy white backgrounds. ')
HE = ('ROWAN, 27: exactly the man in images 1–2 — long gentle face, defined jaw, straight nose, warm light-brown eyes, soft wavy chestnut-brown hair falling over the forehead, clean-shaven, warm easy smile; '
      'warm medium-brown suede zip jacket with collar worn open, cream cable-knit crew sweater, dark charcoal trousers with black belt. No rings, no watch, no necklace. ')
SHE = ('MAISIE, 25: exactly the woman in image 4 — soft oval face, clear green eyes, soft freckles, faint natural blush, very long wavy warm-brown hair with a thin side braid and a small gold leaf hair pin, gold leaf drop earrings; '
       'cream puff-sleeve blouse with lace-trimmed square neckline under a moss-olive laced bodice embroidered with leaves, long olive skirt. ')
STYLE = ('Vertical 9:16 movie poster for a romance drama. Both faces large, sharp and clearly visible, both in the upper half of the frame; the lower third is calm garden and soft shadow for a title (no text in the image). '
         'Refined realistic 3D CG romance game render exactly like image 1: soft natural skin, fine hair strands, detailed fabric, warm golden morning light, full natural saturation, cinematic depth of field. '
         'Not anime, not a photograph, not plastic. No text, no letters, no logo, no watermark. Only these two people. Adults.')
COMP = {
 'A': 'Two-shot across the closed waist-high sage-green garden gate: ROWAN outside on the left, forearms resting on top of the gate, leaning in with a warm teasing smile, looking at her; MAISIE inside on the right, hugging a grey galvanised watering can, one eyebrow raised, sceptical but curious, looking back at him. Three-quarter views, waist-up, the bay and greenhouse behind.',
 'B': 'The moment they meet: a blank weathered wooden shop sign has just fallen from the gate post and ROWAN, on the left, has caught it one-handed at chest height, grinning at her; MAISIE, on the right behind the gate, startled, lips parted, holding a grey watering can raised like a shield. Dynamic, waist-up, three-quarter views.',
 'C': 'MAISIE in the foreground on the right, chest-up, three-quarter view, turning her head to look past the viewer with a guarded, searching look, as if she almost remembers something; ROWAN behind her on the left on the other side of the gate, waist-up, slightly softer focus but his face still clear, smiling at her tenderly. The mystery of a stranger who already knows her.',
 'D': 'ROWAN in the foreground on the left, chest-up, facing the camera in three-quarter view with the warm smile of image 1, a little wistful; MAISIE behind him on the right at the greenhouse doorway framed by wisteria, waist-up, looking at him with quiet suspicion. Soft focus on her but her face readable.',
 'E': 'Inside the sunlit glass greenhouse with hanging wisteria: MAISIE on the right, standing at an old oak table, one hand resting on a closed green cloth notebook, looking up at him, uncertain; ROWAN on the left, across the corner of the table, leaning slightly toward her with a gentle hopeful smile. Waist-up two-shot, three-quarter views, warm light through the glass.',
 'F': 'Romantic close two-shot at the gate: they stand very close on either side of the open gate, faces about a hand apart, ROWAN on the left looking down at her with a soft smile, MAISIE on the right looking up at him, half wary, half drawn in. Chest-up, both faces in three-quarter view, golden morning backlight in their hair, the bay glowing behind.',
}
C_KEEP = ('Image 1 is the chosen cover: keep its composition, framing, background (gate, stone wall, greenhouse with wisteria, bay), light and colours, and keep ROWAN exactly as he is in image 1 — same face, hair, smile, jacket, pose and position behind her on the left. '
          'Images 2–3 are ROWAN references, images 4–5 are MAISIE references (face, hair, earrings, outfit). Change only MAISIE in the foreground on the right: ')
CPOSE = {
 'C1': 'she now faces the camera straight on, chest-up, looking directly into the lens with a soft, guarded, curious gaze, lips slightly parted; one hand gracefully tucks a long wavy strand behind her ear, a light sea breeze lifting the ends of her hair.',
 'C2': 'she now faces the camera straight on, chest-up, looking directly into the lens with a faint uncertain smile; her body turns slightly as if she has just turned round, hair still swinging naturally from the turn, one hand resting lightly at her collarbone.',
 'C3': 'she now faces the camera straight on, waist-up, looking directly into the lens, calm and a little wistful; both hands loosely hold a small bunch of lavender at her waist, shoulders relaxed, a gentle breeze moving her hair and puff sleeves.',
}
def one(k):
    if k in CPOSE:
        return G['image']('CV_' + k, [str(O / 'frames/CV_C.png'), str(R / 'CANON-rowan-ep1.png'), str(R / 'rowan.png'), str(R / 'maisie.png'), str(D / 'masters/she-full.png')],
                          C_KEEP + CPOSE[k] + ' Natural, graceful, relaxed body language, not stiff, not posed like a mannequin; her face, freckles, green eyes, braid, gold leaf pin and earrings and her outfit exactly as image 4–5. ' + HE + SHE + STYLE)
    return G['image']('CV_' + k, [str(x) for x in REFS], HEAD + COMP[k] + ' ' + HE + SHE + STYLE)
with ThreadPoolExecutor(6) as ex:
    for r in ex.map(one, WANT or list(COMP)): print(*r, flush=True)
