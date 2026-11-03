# V10 (Vicky 11-03): her relief and his recognition were slow and mechanical. Real-time, quick, natural reactions; two takes each.
import sys
sys.argv = ['gen.py', 'noop']
exec(open('gen.py').read().split("if __name__ == '__main__':")[0])
REAL = ("Real people reacting live, at real-time speed, quick and spontaneous, like candid footage of a real moment: NOT slow motion, no slow blinks, no held poses, no posing. "
        "Natural quick blinks only; eyes never close slowly or stay closed. Small natural head, shoulder and breathing movement all the time. ")
HER = (REAL + "Close-up of the young woman alone. At the very start her eyes are already down at the lower right, on his hands where the falling wooden board has just been caught. "
       "Straight away, within half a second, she lets out one short quick 'phew' of relief through parted lips (an audible breath, no words), her shoulders drop once and her head gives a tiny relieved shake; "
       "a beat later her eyes flick up to his face, just to the right of the camera, and her look tightens back to wary. Only she is in the picture: no board, no hands, no other person. No music, no words. "
       + SHE + ' ' + LOOKS + STYLE)
HIM = (REAL + "Rowan alone, close chest-up, holding the wooden board against his chest. He blows out one short relieved breath with a small laugh and shifts his grip on the board, "
       "and his eyes snap up to her (toward screen left, at her face slightly below his eye level) in under a second. The instant he sees her his whole face lights up with surprised, delighted recognition, eyebrows lifting, a quick open smile, "
       "as if he knows her; then the smile catches and settles into a wary, amused half smile. After he looks up his eyes stay open and on her. The board stays the same size in his hands. No music, no words, only breath. "
       + HE + ' ' + LOOKS + STYLE)
J = [('S03g1', 'S03g', HER), ('S03g2', 'S03g', HER), ('S04r1', 'S04r', HIM), ('S04r2', 'S04r', HIM)]
def one(j):
    k, f, p = j
    return run('take-' + k, 'bytedance/seedance-2.5/image-to-video', 'multimodal.generate.video', dict(image=upload(V / 'frames' / f'{f}.png'), prompt=p, duration=4, resolution='720p', generate_audio=True), V / 'takes' / f'{k}.mp4')
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(one, J): print(*r, flush=True)
