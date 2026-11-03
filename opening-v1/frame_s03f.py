import sys
sys.argv = ['gen.py', 'noop']
exec(open('gen.py').read().split("if __name__ == '__main__':")[0])
s = [x for x in SHOTS if x['key'] == 'S03f'][0]
p = ("Image 1 shows this woman and her place in the scene; image 2 is her identity and costume reference; image 3 is ONLY a colour, saturation, contrast and light reference: match its warm, clear, fully saturated look exactly and ignore its people and framing. "
     + s['frame'] + SHE + ' ' + STYLE)
print(image('S03f', [V / 'frames/S03d.png', MAISIE, V / 'frames/S08e.png'], p))
