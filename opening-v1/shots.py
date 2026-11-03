# -*- coding: utf-8 -*-
"""今天，再喜欢我一次 · 第三人称开场 V1：海边温室院门，清晨。12 镜，轴线固定：她在画左（院内），他在画右（院外）。"""
FR = "/Users/vicky/Interactive storyline/output/meet-me-third-live-v1/opening-v1/frames/"
R = "/Users/vicky/Interactive storyline/projects/meet-me-again-deepspace-20261013/storyboard-v1/references/"
ROWAN, CANON, MAISIE, BAG, S01 = R+"rowan.png", R+"CANON-rowan-ep1.png", R+"maisie.png", R+"BAG-canon.png", R+"S01-original.png"

STYLE = ("Refined 2.5D-leaning-3D romance game CG, exactly the rendering of the character reference images: soft natural skin, fine hair strands, detailed fabric. "
         "Warm clear morning daylight, natural saturation. Not a photograph, not flat anime, not oily or plastic, no heavy contrast, no sharpening, no text, no watermark. 9:16 vertical.")
PLACE = ("PLACE: a seaside greenhouse garden gate on a sunny morning. A low weathered sage-green wooden garden gate of two leaves, closed, reaching waist height, set between dry-stone pillars in a low stone wall with white flowers and lavender. "
         "The garden and glass greenhouse with wisteria are on the LEFT side of the gate; the cobbled lane is on the RIGHT side; beyond them a calm blue bay with a rocky headland and small grey-roofed white cottages.")
HE = ("ROWAN, 27, the man in the Rowan reference: same face as the reference (long lean face, soft brown eyes, straight nose), messy wavy chestnut-brown hair falling over his forehead. Lean long build. "
      "WARDROBE, never changes: the exact jacket of the second man reference: warm medium-brown weathered suede zip jacket with a collar, worn open, soft matte texture, NOT dark chocolate, NOT near-black, NOT orange tan; cream cable-knit crew sweater; dark charcoal wool trousers with a black belt. No jeans, no rings, no watch.")
SHE = ("MAISIE, 25, the woman in the Maisie reference: same face as the reference (long oval face, clear green eyes, soft freckles across nose and cheeks, faint natural blush), long wavy warm-brown hair with a small braid at one side and a gold leaf hair pin, gold leaf drop earrings. "
       "WARDROBE, never changes: cream puff-sleeve blouse with a lace square neckline, moss-olive embroidered laced bodice with leaf embroidery. Modest, no extra necklace, no rings.")
AXIS = ("AXIS LOCK: Maisie is on the garden side and faces screen right; Rowan is on the lane side and faces screen left. They stay on their own side of the closed gate. Nobody crosses.")
PROPS = ("PROPS: there is exactly one grey galvanised watering can and it is only ever in Maisie's hands. There is exactly one wooden sign, a short wide weathered board about 60 cm wide with no writing visible, and it is only where this shot says: no sign hanging on any bracket, none on the gate, none leaning anywhere else. The one dark-brown leather flap tool bag rests on top of the stone pillar next to the gate and is the only bag.")
ONLY2 = "Only the people named in this shot are in the picture, nobody else: no other person, no shoulder or arm at the frame edge, no extra hands."
SILENT = ("Everyone keeps their lips softly closed and jaw still for the whole shot, no talking, no mouth movement (the voices are dubbed later); faces and bodies still act with eyes, brows, breath and posture.")
GUARD = ("One single continuous camera take: no cut, no dissolve, no morph, no zoom unless written. Faces, hair, clothes and props keep exactly the first frame's shape, colour and rendering in every frame. Natural weight and timing, not slow motion. No music, no speech.")

PLATES = {
 'P_TWO': ("Image 1 shows this place from the front. Create the empty set from a completely different angle: the camera stands right on top of the line of the low stone wall, at chest height, looking straight along the wall. The wall runs away from the camera straight down the MIDDLE of the frame, dividing the picture into two halves. The closed sage-green gate is part of that wall, seen exactly EDGE-ON: we see only its narrow top rail as a short thin line along the wall line in the lower centre, with a stone pillar in front of it and another behind it, we do NOT see the face of the gate. LEFT half: the garden side with flowers, pots and the corner of the glass greenhouse. RIGHT half: the cobbled lane. Far behind: calm blue bay, headland and small grey-roofed cottages. No people, no sign, no watering can. " + STYLE, [S01, CANON]),
 'P_HER': ("Image 1 shows this place. Create the empty background seen from the lane looking into the garden over the closed gate: soft focus glass greenhouse door with wisteria and hanging pots, flowers, cream stone cottage wall at the left, warm morning sun. The top of the closed sage-green gate crosses the very bottom edge. No people. " + STYLE, [S01]),
 'P_HIM': ("Keep the background of image 1 exactly (sea, headland, cottages, steps, flowers, lantern) and the closed sage-green gate at the bottom, and remove the man completely so the set is empty. Keep the tool bag on the stone pillar at the left edge. " + STYLE, [CANON]),
}

SHOTS = [
 dict(key='S01', plate=None, refs=[S01], dur=5, take=(.3,1.65), lines=[],
  frame="Wide empty establishing view of the place in image 1 on a sunny morning, composed for a 9:16 frame: the greenhouse with wisteria, the low green gate and stone wall, the hanging wooden sign on its iron bracket at the left, the bay beyond. No people, no watering can anywhere, no tool bag. ",
  act="A slow gentle camera drift to the right. Leaves and wisteria stir in the sea breeze; the hanging wooden sign on its iron bracket sways a little on one loose hook. No people."),
 dict(key='S02', plate=None, refs=[S01], dur=4, take=(.35,1.25), lines=[],
  frame="Close view from below of a weathered wooden signboard hanging from a dark iron bracket by two small chains, against bright sky and wisteria; only its plain back is seen, no writing. One chain hook is half out of its eye. No people. ",
  act="Locked-off camera. The loose hook slips out of its eye; the board drops at one end, swings once, and falls out of the bottom of the frame. The bracket and chain keep swinging. No people, no hands."),
 dict(key='S03b', plate='P_HER', refs=[MAISIE], dur=4, take=(.1,1.1), lines=[], frame="(same frame as S03) ",
  act="Fixed camera. Fast and sudden: right at the very first instant she flinches hard, shoulders jumping, gasping with her lips parted, the watering can jerking so the water stops; her head snaps up to look high toward the upper right of the frame, eyes wide with alarm. All within the first second, then she stays frozen looking up to the upper right. Real-time speed, sudden, not slow motion."),
 dict(key='S04c', plate='P_HIM', refs=[ROWAN, CANON, FR+'S04.png'], dur=4, take=(.3,4.0), fast=(1.6,2.6), lines=[], last='S04', frame="Rowan alone, waist-up, behind the closed gate, 3/4 view facing screen left, looking sharply upward with a startled face, both arms thrown up above his head with open hands, about to catch the wooden board which is falling flat just above his hands at the very top of the frame. The last reference image shows the exact board and its size. No watering can. ",
  act="Fast and sudden, real-time speed. In the first half second the falling wooden board drops into his raised hands; he catches it with a jolt, his arms and knees absorbing the weight, and in one quick motion brings it down to chest height, breathing out, ending exactly as the last frame. Fixed camera. Natural weight, not slow motion."),
 dict(key='S04', plate='P_HIM', refs=[ROWAN, CANON, BAG], dur=5, take=(0,4.3), head=(1.4,3.0), lines=[],
  frame="Rowan alone, waist-up, behind the closed gate in 3/4 view facing screen left, holding the fallen short wide wooden board in both hands at chest height, its plain back to the camera; he has just caught it, hair a little disordered. The bag sits on the pillar at the left edge. ",
  act="He steadies the board, breathing out, and looks up toward screen left. On seeing her his whole face lights up with delighted recognition, like he has been waiting for this; his lips part a little as if about to say something. Then his eyes drop a little and the smile stops halfway, wary and amused. Fixed camera."),
 dict(key='S05', plate='P_HER', refs=[MAISIE], dur=4, take=(.5,3.2), lines=[('F1',1.2)], frame="Maisie alone, close chest-up framing like a portrait, her head in the upper third, 3/4 view facing screen right, looking off screen right; both hands raise the grey galvanised watering can to chest height, spout toward screen right; guarded, chin level. Bright warm morning light, sage-green gate top at the very bottom edge. No sign in the picture. ",
  act="Locked-off camera, no push-in. She lifts the can a little higher, spout aimed at screen right, and stares off screen right, level and wary. Small breath. Same bright warm light in every frame."),
 dict(key='S06', plate='P_HIM', refs=[ROWAN, CANON, FR+'S04.png'], dur=6, take=(.4,5.2), lines=[('M1',1.2)], frame="Rowan alone, chest-up, 3/4 view facing screen left, looking off screen left with a wary half smile, holding the wooden board in both hands at lower chest height. The last reference image shows the exact board and how big it is against his body: the same board, the same size, narrower than his shoulders, plain back to the camera, fully inside the frame. No watering can. ",
  act="Rowan glances down at the board in his hands, then back up just left of camera with a half smile, one eyebrow lifting: a dry joke. He lifts the board a few centimetres to show its weight. Fixed camera."),
 dict(key='S07', plate='P_HER', refs=[MAISIE], dur=5, take=(.4,4.3), lines=[('F2',.6)], frame="Maisie alone, chest-up, 3/4 view facing screen right, can held up at chest height; firmer, jaw set, a small crease between her brows. ",
  act="She gives one small downward nod toward off screen right, then a tiny tilt of the chin, patient but firm. Fixed camera."),
 dict(key='S08', plate='P_HIM', refs=[ROWAN, CANON, BAG], dur=8, take=(.3,7.95), lines=[('M2',3.7)], frame="Rowan alone, waist-up, behind the closed gate in 3/4 view facing screen left, holding the short wooden board in both hands at chest height, plain back to the camera; amused and careful. Bag on the pillar at the left edge. No watering can in the picture. ",
  last='S10', act="Locked-off camera, the framing never changes. He slowly lowers the board straight down in front of himself until it passes below the top of the gate and out of sight on his own side, bending his knees a little, and lets go of it down there, so the board stays hidden behind the gate. He straightens with empty hands, opens both palms once at chest height, then slides his hands into his jacket pockets, ending exactly as the last frame. The board never rests on top of the gate and he never leans over the gate. Nothing lies on top of the gate."),
 dict(key='S09', plate='P_HER', refs=[MAISIE], dur=4, take=(.4,2.4), lines=[], frame="Maisie alone, close-up, 3/4 view facing screen right, looking off screen right, not laughing. No can on the ground, no sign. ",
  act="She does not laugh. One corner of her mouth almost moves and she stops it; her eyes narrow slightly, curious despite herself. Fixed camera."),
 dict(key='S10', plate='P_HIM', refs=[ROWAN, CANON], dur=5, take=(.4,4.0), lines=[('M3',.9)], frame="Rowan alone, chest-up, 3/4 view facing screen left, hands in his jacket pockets, a warm open expression, looking just left of camera. He is completely alone in the shot: no woman, no other person, no hair or shoulder at the frame edge. No watering can, no sign in the picture. ",
  act="Warm and open, he gives a small easy nod, eyes staying just left of camera. Fixed camera."),
 dict(key='S11', plate='P_HER', refs=[MAISIE], dur=4, take=(.4,3.0), lines=[('F3',.9)], frame="Maisie alone, chest-up, 3/4 view facing screen right, can lowered to waist height but still in hand; alone in the shot, looking off screen right, sceptical. No other person, nothing at the frame edge. ",
  act="Her eyes travel once slowly down and back up, looking off screen right, sceptical, head very slightly tilted back. Fixed camera."),
 dict(key='S13', plate='P_HIM', refs=[ROWAN, CANON], dur=5, take=(.3,4.6), lines=[('M4',1.0)], frame="(same frame as S10) ",
  act="Locked-off camera. Hands stay in his jacket pockets. He raises one eyebrow with a self-mocking smile and tips his head very slightly, then holds a hopeful little grin, eyes staying just left of camera. His face stays toward the camera in 3/4 view. Fixed camera."),
 dict(key='S12', plate='P_TWO', refs=[ROWAN, CANON, MAISIE, BAG], dur=8, take=(3.2,7.4), lines=[], frame="Two-shot across the wall: keep image 1's set, with the wall and the edge-on gate running down the middle of the frame between them. Maisie stands in the LEFT half on the garden side, Rowan stands in the RIGHT half on the lane side, facing each other across the gate line, about one metre apart, the camera is close: the frame cuts both of them at the waist, their heads fill the upper half of the frame, no legs or knees visible, both turn their bodies and faces well toward the camera in a 3/4 front view with both eyes of each person clearly visible (not pure profile), both faces large and clear, Rowan's whole shoulders and arms inside the frame, not cut by the right edge. Maisie holds the grey can at waist height, sceptical. Rowan has empty hands in his jacket pockets. The bag rests on the near stone pillar at the lower centre between them; no sign in the picture. They are clearly NOT on the same side of the gate. ",
  act="Across the wall, Rowan raises one eyebrow with a self-mocking smile, leaning in a little toward her without crossing, hands staying in his pockets. He holds her gaze, waiting for her answer with a hopeful little grin. Maisie keeps looking at him; her grip on the can loosens a touch; she has not decided. Both keep their faces toward each other. Fixed camera."),
]
LINES = {  # 原 D1/B 配音：(源片, 入, 出, 角色, 英, 中)
 'F1': ('01-02', .40, 1.20, 'Maisie', 'Put it down.', '放下。'),
 'M1': ('01-02', 2.84, 5.66, 'Rowan', 'This? Your toes might have a problem with that.', '这个？放了可真要砸脚。'),
 'F2': ('01-02', 5.80, 8.90, 'Maisie', 'The sign. Put it down, and take a step back.', '我是说，放下招牌，后退一点。'),
 'M2': ('01-03', 4.54, 8.76, 'Rowan', 'Okay. Just so we are clear, I am not waterproof.', '好吧。先说清楚，我可不防水。'),
 'M3': ('01-04', .18, 2.76, 'Rowan', "I'm Rowan. Here to fix the sign.", '我是洛温。来修招牌的。'),
 'F3': ('01-04', 3.45, 5.22, 'Maisie', "You don't look like someone I hired.", '你看着不像我叫来的。'),
 'M4': ('01-04', 7.88, 10.80, 'Rowan', 'Bad introduction. Want me to start over?', '那我介绍得不够好。需要重来吗？'),
}

NDUR = {'S05': 4, 'S06': 6, 'S07': 6, 'S08': 9, 'S10': 5, 'S11': 4, 'S13': 6}  # native takes need room for the line itself
for _s in SHOTS:
    if _s['key'] in NDUR: _s['ndur'] = NDUR[_s['key']]

NWIN = {'S05': (.9, 3.4), 'S06': (1.0, 5.3), 'S07': (2.1, 5.9), 'S08': (.3, 8.25), 'S10': (.9, 4.2), 'S11': (.6, 3.3), 'S13': (1.0, 4.7)}

# ---------- V4 (Vicky: opening motion is not natural; do not end on the two-shot) ----------
_by = {x['key']: x for x in SHOTS}
S02B = dict(key='S02b', plate=None, refs=[S01], dur=4, take=(.45,2.25), lines=[],
  frame="Tight low-angle close-up looking up at a weathered wooden signboard hanging from a dark iron bracket by two short chains. Only the board, the bracket, wisteria and bright blue sky are in the picture: no gate, no wall, no ground, no buildings, no people. Only its plain back is seen, no writing. One chain hook is half out of its eye. ",
  act="Locked-off camera. The loose hook snaps out of its eye. The board drops at once under its real weight: it swings down on the other chain for an instant, tears free and falls straight down out of the bottom of the frame, fast, accelerating under gravity, without floating or turning over. The chains whip and keep swinging. No people, no hands. Real-time speed.")
S04N = dict(key='S04n', plate='P_HIM', refs=[ROWAN, CANON, FR+'S04.png'], dur=8, take=(.1,6.6), lines=[], atk=None,
  frame="Rowan alone, close chest-up framing, 3/4 view facing screen left, the gate and everything below his chest are outside the frame. Caught mid-reaction: his chin has just lifted, startled, both forearms coming up in front of his chest with open palms facing up. The bottom edge of the falling wooden board has just entered at the very top of the frame, in front of him and closer to the camera than his face, so it will come down in front of his chest and not over his face. The last reference image shows the exact board and its size. No watering can, no bag. ",
  act="One unbroken real-time take, locked-off camera with the same close chest-up framing the whole time; the gate never comes into view. In the first second the wooden board falls from above, in front of his body, never passing through or covering his face, and lands in his open hands at chest height: it hits his palms with a jolt, his arms give and his shoulders dip, and he catches his balance. He huffs out a breath of relief, a small laugh in his shoulders, glancing down at the board. Only then he looks up toward screen left. On seeing her his whole face lights up with delighted recognition, as if he has been waiting for this; his lips part a little as if about to say something. Then his eyes drop a little and the smile stops halfway, wary and amused. The board stays the same size in his hands the whole time. No words, only breath.")
_new = []
for x in SHOTS:
    if x['key'] == 'S02': _new.append(S02B)
    elif x['key'] == 'S04c': _new.append(S04N)
    elif x['key'] == 'S04': continue
    elif x['key'] == 'S12': continue
    elif x['key'] == 'S13': _new += [dict(_by['S12'], take=(3.2,4.8)), x]  # short two-shot beat before his last line, then stop on him
    else: _new.append(x)
SHOTS = _new
NWIN['S13'] = (1.0, 6.0)  # hold on him after the line; the opening ends here

# V4 edit: catch -> her frozen reaction -> him looking up. The cutaway skips the 2 s he stares at the board, with no speed change and no jump cut.
_e = []
for x in SHOTS:
    if x['key'] == 'S04n':
        _e += [dict(x, key='S04a', src='S04n', take=(0, 1.3)), dict(_by['S03b'], key='S03c', src='S03b', take=(1.3, 2.0)), dict(x, key='S04b', src='S04n', take=(3.75, 6.4))]
    else: _e.append(x)
SHOTS = _e

# ---------- V6 (Vicky 11-02): her relief looks DOWN at his hands; S08 brisk and natural; no smiling sound on her;
# they stand on the two sides of the gate, so the dialogue is shot/reverse-shot over the shoulder, and the far two-shot is dropped.
OTS_HER = ("Over-the-shoulder shot across the closed waist-high sage-green garden gate. In the RIGHT foreground, very close to the camera and soft out of focus: Rowan seen from behind, only the back of his head with messy chestnut-brown hair and his shoulder in the warm medium-brown suede jacket, filling the right quarter of the frame; his face is never visible. "
           "Maisie stands just across the gate from him, about an arm's length away, chest-up, sharp focus, her body and face turned in a 3/4 front view toward screen right, looking at him (just right of the camera), her face large and clear. The top rail of the closed gate runs across the lower part of the frame between them. ")
OTS_HIM = ("Over-the-shoulder shot across the closed waist-high sage-green garden gate. In the LEFT foreground, very close to the camera and soft out of focus: Maisie seen from behind, only the back of her head with long wavy warm-brown hair, a small braid and a gold leaf hair pin, and her shoulder in the cream puff sleeve, filling the left quarter of the frame; her face is never visible. "
           "Rowan stands just across the gate from her, about an arm's length away, chest-up, sharp focus, his body and face turned in a 3/4 front view toward screen left, looking at her (just left of the camera), his face large and clear. The top rail of the closed gate runs across the lower part of the frame between them. ")
FG = "The person in the foreground stays seen from behind and out of focus the whole time, never turns around, never shows a face, and does not speak. "
_old = {x['key']: x for x in SHOTS}
def _o(key, plate, base, lines, ndur, frame, act, last=None):
    d = dict(key=key, plate=plate, refs=[ROWAN, CANON, MAISIE] + ([FR + 'S04.png'] if 'board' in frame else []), dur=ndur, ndur=ndur, take=(0, ndur), lines=lines, frame=frame, act=FG + act, ots=True)
    if last: d['last'] = last
    return d
V6 = [
 dict(key='S03d', plate=None, refs=[MAISIE], dur=4, take=(1.65, 3.25), lines=[], frame='(frame taken from S03b at 1.1 s)',
      act="Fixed camera, real-time speed. She stays where she is. Her eyes drop quickly from high up to low toward screen right, following the falling board down to the man's hands just across the gate at waist height (out of frame, lower right). Seeing it caught, her shoulders sink and she lets out one audible breath of relief through parted lips, then keeps looking low at his hands. She does not smile. The watering can stays in her hand."),
 _o('S05o', 'P_HER', 'S05', [('F1', 1.0)], 4, OTS_HER + "Both her hands raise the grey galvanised watering can to chest height with the spout pointing toward him; guarded, chin level. ",
    "She lifts the can a little higher, spout aimed at him, and says her line, level and wary."),
 _o('S06o', 'P_HIM', 'S06', [('M1', 1.0)], 6, OTS_HIM + "He holds the short wide wooden board horizontally in both hands at lower chest height, plain back toward her; the last reference image shows the exact board and its size. A wary, amused half smile. ",
    "He glances down at the board in his hands, then back up at her with a half smile and one eyebrow lifting, and says his line as a dry joke, lifting the board a few centimetres to show its weight."),
 _o('S07o', 'P_HER', 'S07', [('F2', .8)], 6, OTS_HER + "She holds the watering can at chest height; firmer, jaw set, a small crease between her brows. ",
    "She gives one small downward nod toward the board in his hands, then a tiny tilt of the chin, patient but firm, and says her line."),
 _o('S08o', 'P_HIM', 'S08', [('M2', 1.6)], 8, OTS_HIM + "He holds the short wide wooden board horizontally in both hands at lower chest height; the last reference image shows the exact board and its size. Amused and careful. ",
    "Brisk, natural real-time movement, not slow. In one smooth quick motion within the first second he bends his knees and lowers the board straight down behind the gate on his own side, out of sight, lets go and straightens up with empty hands. Without a pause he opens both palms once at chest height and says his line easily, then slides his hands into his jacket pockets. One single continuous take with the same over-the-shoulder framing from start to end: no cut, no camera jump. He never leans over the gate; the board never rests on the gate."),
 _o('S09o', 'P_HER', 'S09', [], 4, OTS_HER + "She holds the watering can a little lower now; she is not laughing. ",
    "She does not laugh and makes no sound. One corner of her mouth almost moves and she stops it; her eyes narrow slightly, curious despite herself. Silent."),
 _o('S10o', 'P_HIM', 'S10', [('M3', .9)], 5, OTS_HIM + "His empty hands are in his jacket pockets; a warm open expression. No board in the picture. ",
    "Warm and open, he gives a small easy nod and introduces himself, eyes staying on her."),
 _o('S11o', 'P_HER', 'S11', [('F3', .8)], 4, OTS_HER + "She holds the watering can lowered to waist height; she looks him up and down, sceptical. ",
    "Her eyes travel once quickly down him and back up to his face, sceptical, head very slightly tilted back, and she says her line."),
 _o('S13o', 'P_HIM', 'S13', [('M4', 1.0)], 6, OTS_HIM + "His empty hands are in his jacket pockets; a self-mocking smile. No board in the picture. ",
    "He raises one eyebrow with a self-mocking smile and says his line, then holds a hopeful little grin, eyes on her, waiting for her answer."),
]
SHOTS = [x for x in SHOTS if x['key'] in ('S01', 'S02b', 'S03b', 'S04a', 'S04b')]
SHOTS = SHOTS[:4] + [V6[0]] + SHOTS[4:] + V6[1:]
import json as _json, os as _os
_wf = FR.replace('frames/', 'qa/native_words.json')
if _os.path.exists(_wf):  # windows from the real word timings of each native take
    _W = _json.load(open(_wf))
    _RULE = {'S05o': (.7, .45), 'S06o': (.6, .45), 'S07o': (.6, .45), 'S08o': (None, .5), 'S10o': (.5, .45), 'S11o': (.5, .4), 'S13o': (.6, 1.8)}
    for _k, (_lead, _tail) in _RULE.items():
        if _k in _W and _W[_k]['words']:
            _w = _W[_k]['words']; NWIN[_k] = (0.15 if _lead is None else max(0, _w[0][1] - _lead), min(_W[_k]['dur'] - .05, _w[-1][2] + _tail))

for _x in SHOTS:
    if _x['key'] == 'S09o': _x['take'] = (.4, 2.4)

# ---------- V7 (Vicky 11-02): his eyes must be on her. In the V6 takes his eyes drifted down, squinted shut when smiling and wandered off. ----------
EYE = ("EYE LINE: he keeps steady eye contact with her the whole time. Her face is just behind the back of her head in the left foreground, at the same height as his eyes; "
       "his eyes stay open and his pupils point straight at her face (just left of the camera). He never closes his eyes, never looks down or away, never looks into the camera, "
       "and when he smiles or laughs his eyes stay open and on her. ")
EYE_EDIT = ("Edit image 1 only. Change nothing except his eyes and the angle of his head: his eyes are open and look straight at the woman's face in the left foreground "
            "(her face is just behind the back of her head there, at the same height as his eyes), clear eye contact, pupils turned toward her; his head turns a little toward her. "
            "Keep his face, expression, hair, clothes, hands, the board if any, the woman in the foreground, the gate, background, light and rendering exactly as they are.")
_v6 = {x['key']: x for x in SHOTS}
V7 = {}
for _k, _n, _extra in [('S06o', 'S06e', "He may glance down at the board once, quickly, then his eyes come straight back to her. "),
                       ('S08o', 'S08e', "Only while he bends to put the board down may his eyes leave her; as soon as he straightens up his eyes go straight back to her face and stay there. "),
                       ('S10o', 'S10e', ""), ('S13o', 'S13e', "")]:
    _d = dict(_v6[_k], key=_n, act=_v6[_k]['act'] + ' ' + _extra + EYE, eyefix=_k)
    V7[_n] = _d
SHOTS = [V7.get({'S06o': 'S06e', 'S08o': 'S08e', 'S10o': 'S10e', 'S13o': 'S13e'}.get(x['key'], ''), x) for x in SHOTS]
if _os.path.exists(_wf):
    for _k, (_lead, _tail) in {'S06e': (.6, .45), 'S08e': (None, .5), 'S10e': (.5, .45), 'S13e': (.6, 1.8)}.items():
        if _k in _W and _W[_k]['words']:
            _w = _W[_k]['words']; NWIN[_k] = (0.15 if _lead is None else max(0, _w[0][1] - _lead), min(_W[_k]['dur'] - .05, _w[-1][2] + _tail))

# ---------- V8 (Vicky 11-02): the relief beat becomes a close-up of her alone (no board, no hands); whole film graded to the S08e look ----------
S03F = dict(key='S03f', plate=None, refs=[MAISIE], dur=4, take=(.3, 2.3), lines=[],
  frame="Close-up of Maisie alone, head and shoulders, 3/4 view facing screen right, same garden and greenhouse softly out of focus behind her, warm clear morning sun. She has just seen the board caught: her eyes are lowered toward the lower right, lips parted mid-breath, brows starting to relax. Only her face, hair and shoulders are in the picture: no board, no hands, no watering can, no other person. ",
  act="Fixed camera, real-time speed, a close-up of her alone. She lets out one audible breath of relief through parted lips; her shoulders sink and her brows relax while her eyes stay lowered toward the lower right where the board was caught; then her eyes lift slightly back toward screen right. She does not smile. No other person, no board, no hands in the picture. No music, no speech.")
SHOTS = [S03F if x['key'] == 'S03d' else x for x in SHOTS]

# ---------- V9 (Vicky 11-02): his OTS eyeline still drifts -> frontal close-ups with the eyes right beside the lens; her OTS shots lost her face and the colour -> rebuilt from the approved close-up. ----------
CU_HIM = ("Close-up of Rowan, head and chest, his face large and centred, turned almost straight to the camera (very slight 3/4 toward screen left). At the very LEFT edge only a thin soft-focus sliver of her long wavy warm-brown hair is visible, very close to the camera, showing she stands right in front of him; nothing else of her. "
          "Behind him, softly out of focus: the cobbled lane, flowers, small white cottages and the blue bay in warm morning sun. ")
CU_HER = ("Close-up of Maisie, head and chest, her face large and centred, turned almost straight to the camera (very slight 3/4 toward screen right). At the very RIGHT edge only a thin soft-focus sliver of his warm-brown suede jacket shoulder is visible, very close to the camera, showing he stands right in front of her; nothing else of him. "
          "Behind her, softly out of focus: the glass greenhouse with wisteria, flowers and a stone cottage wall in warm morning sun. ")
EYE_HIM = ("EYE CONTACT: he is talking face to face with her. His eyes are open and look at her, aimed just to the LEFT of the camera lens, almost into the lens, at his own eye height; this eye line holds through the whole shot. He never looks down at the ground, never looks off to the side, never closes his eyes, and when he smiles or laughs his eyes stay open and on her. ")
EYE_HER = ("EYE CONTACT: she is talking face to face with him. Her eyes look at him, aimed just to the RIGHT of the camera lens, almost into the lens, slightly upward because he is a little taller; this eye line holds through the whole shot. She never looks off to the side and never closes her eyes. ")
LOOKS = ("Keep the exact warm, clear, fully saturated colour, contrast and sunlight of the colour reference image: rich warm skin, golden hair highlights, deep blue sea and sky, never greyish, never washed out, never desaturated. ")
def _c(key, who, lines, ndur, frame, act, take=None):
    d = dict(key=key, plate=None, refs=([ROWAN, CANON] if who == 'M' else [MAISIE]), dur=ndur, ndur=ndur, take=take or (0, ndur), lines=lines,
             frame=frame, act=act + ' ' + (EYE_HIM if who == 'M' else EYE_HER) + LOOKS, cu=who)
    return d
V9 = [
 _c('S05c', 'F', [('F1', 1.0)], 4, CU_HER + "Both her hands raise the grey galvanised watering can to just below her chin, spout pointing toward screen right; guarded, chin level. ",
    "She lifts the can a little higher, spout aimed toward him, and says her line, level and wary."),
 _c('S06c', 'M', [('M1', 1.0)], 6, CU_HIM + "He holds the short wide weathered wooden board horizontally in both hands at chest height, its top edge at the bottom of the frame; a wary, amused half smile. ",
    "He gives the board in his hands one quick glance, then his eyes come straight back to her and he says his line as a dry joke, lifting the board a few centimetres to show its weight, one eyebrow lifting."),
 _c('S07c', 'F', [('F2', .8)], 6, CU_HER + "She holds the watering can at chest height at the bottom of the frame; firmer, jaw set, a small crease between her brows. ",
    "She gives one small downward nod toward the board he holds, then looks straight back at him with a tiny tilt of the chin, patient but firm, and says her line."),
 _c('S08c', 'M', [('M2', 1.6)], 8, CU_HIM + "He holds the short wide wooden board horizontally in both hands at chest height at the bottom of the frame; amused and careful. ",
    "Brisk, natural real-time movement, not slow. Within the first second he lowers the board straight down out of the bottom of the frame on his own side of the gate and straightens with empty hands, eyes coming straight back to her. He opens both palms once at chest height and says his line easily, then slides his hands into his jacket pockets. One single continuous take, same framing from start to end, no cut."),
 _c('S09c', 'F', [], 4, CU_HER + "Her hands are out of the frame; she is not laughing, lips closed. ",
    "She does not laugh and makes no sound. She keeps looking at him; one corner of her mouth almost moves and she stops it; her eyes narrow slightly, curious despite herself. Silent."),
 _c('S10c', 'M', [('M3', .9)], 5, CU_HIM + "His hands are in his jacket pockets, out of the frame; a warm open expression. No board in the picture. ",
    "Warm and open, he gives a small easy nod and introduces himself, eyes on her."),
 _c('S11c', 'F', [('F3', .8)], 4, CU_HER + "Her hands are out of the frame; sceptical. ",
    "Her eyes travel once quickly down him and straight back up to his face, sceptical, head very slightly tilted back, and she says her line."),
 _c('S13c', 'M', [('M4', 1.0)], 6, CU_HIM + "His hands are in his jacket pockets, out of the frame; a self-mocking smile. No board in the picture. ",
    "He raises one eyebrow with a self-mocking smile and says his line, then holds a hopeful little grin, eyes on her, waiting for her answer."),
]
_V9 = {x['key'][:3]: x for x in V9}
SHOTS = [_V9.get(x['key'][:3], x) if x['key'][:3] in ('S05', 'S06', 'S07', 'S08', 'S09', 'S10', 'S11', 'S13') else x for x in SHOTS]
for _x in SHOTS:
    if _x['key'] == 'S09c': _x['take'] = (.4, 2.4)
if _os.path.exists(_wf):
    _W = _json.load(open(_wf))
    for _k, (_lead, _tail) in {'S05c': (.7, .45), 'S06c': (.6, .45), 'S07c': (.6, .45), 'S08c': (None, .5), 'S10c': (.5, .45), 'S11c': (.5, .4), 'S13c': (.6, 1.8)}.items():
        if _k in _W and _W[_k]['words']:
            _w = _W[_k]['words']; NWIN[_k] = (0.15 if _lead is None else max(0, _w[0][1] - _lead), min(_W[_k]['dur'] - .05, _w[-1][2] + _tail))
for _x in SHOTS:  # V9 retakes: pin a same-framing last frame so the model cannot pull back or cut mid-take
    if _x['key'] == 'S08c': _x['last'] = 'S10c'
    if _x['key'] == 'S11c': _x['last'] = 'S09c'
# S08c: the take snaps a little closer at 5.42 s, mid-line. Picture cuts to her listening (S09c) at 5.38 and his line finishes over her face.
if _os.path.exists(_wf) and 'S08c' in NWIN:
    NWIN['S08c'] = (NWIN['S08c'][0], 5.38)
    for _x in SHOTS:
        if _x['key'] == 'S08c': _x['atail'] = 1.3
# V10 (Vicky 11-03): her relief and his recognition were slow and mechanical -> real-time retakes (react.py), picked take 2 of each.
for _x in SHOTS:
    if _x['key'] == 'S03f': _x.update(src='S03g2', take=(.1, 1.45))
    if _x['key'] == 'S04b': _x.update(src='S04r2', take=(1.75, 3.6))
# V11 (Vicky 11-03): S06c showed her raised hands and watering can at the bottom edge -> retake with nothing entering the frame.
NOHANDS = ("Nothing enters the frame from the bottom or the sides at any moment: no watering can, no other hands or arms; the only hands in the picture are his own two hands holding the board. ")
for _x in SHOTS:
    if _x['key'] == 'S06c': _S06 = _x
V11 = [dict(_S06, key=k, act=NOHANDS + _S06['act'] + ' ' + NOHANDS) for k in ('S06d1', 'S06d2')]
