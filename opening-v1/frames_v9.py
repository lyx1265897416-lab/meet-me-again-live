import sys
sys.argv = ['gen.py', 'noop']
exec(open('gen.py').read().split("if __name__ == '__main__':")[0])
def one(s):
    if s['cu'] == 'F':
        refs = [V / 'frames/REF_HER.png', MAISIE, V / 'frames/REF_COLOR.png']
        head = ("Image 1 is the approved close-up of this exact woman: keep her face exactly (long oval face, clear green eyes, soft freckles, faint blush, same nose, lips and brows), her hair, gold leaf pin, earrings, blouse and bodice, and its rendering. Image 2 is her costume and identity reference. Image 3 is ONLY the colour, light and saturation reference; ignore its people and framing. ")
        who = SHE
    else:
        refs = [ROWAN, CANON, V / 'frames/REF_COLOR.png'] + ([FR + 'S04.png'] if 'board' in s['frame'] else [])
        head = ("Image 1 and image 2 are this exact man: keep his face, hair and clothes exactly. Image 3 is ONLY the colour, light and saturation reference; ignore its framing. " + ("The last image shows the exact wooden board and its size. " if 'board' in s['frame'] else ''))
        who = HE
    return image(s['key'], refs, head + s['frame'] + (EYE_HIM if s['cu'] == 'M' else EYE_HER) + LOOKS + who + ' ' + STYLE)
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(one, [s for s in SHOTS if s.get('cu')]): print(*r, flush=True)
