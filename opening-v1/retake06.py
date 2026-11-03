import sys
sys.argv = ['gen.py', 'noop']
exec(open('gen.py').read().split("if __name__ == '__main__':")[0])
import shutil
for s in V11: shutil.copy(V / 'frames/S06c.png', V / 'frames' / f"{s['key']}.png")
with ThreadPoolExecutor(2) as ex:
    for r in ex.map(native, V11): print(*r, flush=True)
