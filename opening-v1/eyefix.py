# V7: new first frames = the approved V6 frames with only his eye line changed.
import sys
sys.argv = ['gen.py', 'noop']
exec(open('gen.py').read().split("if __name__ == '__main__':")[0])
with ThreadPoolExecutor(4) as ex:
    fs = [ex.submit(image, s['key'], [V / 'frames' / f"{s['eyefix']}.png"], EYE_EDIT + ' ' + STYLE) for s in SHOTS if s.get('eyefix')]
    for f in fs: print(*f.result(), flush=True)
