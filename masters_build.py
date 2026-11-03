"""母版：身份图和合成母版上传 Vivix，写 masters/urls.json。
用法：python3 masters_build.py gen    生成白底服装图、全身图、站位图、第 1 轮关键帧、小摩托（gpt-image-2/edit，复用 opening-v1/gen.py 的生成和上传）
      python3 masters_build.py upload 裁头像、拼她的合图、取开场末帧，全部上传 Vivix"""
import json, shutil, subprocess, sys
from pathlib import Path
from PIL import Image
D = Path(__file__).resolve().parent; M = D / 'masters'; F = M / 'urls.json'; O = D / 'opening-v1'
REF = Path('/Users/vicky/Interactive storyline/projects/meet-me-again-deepspace-20261013/storyboard-v1/references')
NORA = Path('/Users/vicky/Interactive storyline/projects/meet-me-again-deepspace-20261013/storyboard-images-v1/characters/nora-style-v2.png')
FF = '/Users/vicky/Interactive storyline/.media-runtime/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1'
OPEN = O / 'delivery/MMA3P_OPENING_确认版.mp4'
STYLE = ('Refined 2.5D-leaning-3D romance game CG, exactly the rendering of the reference images: soft natural skin, fine hair strands, detailed fabric. '
         'Warm clear light, full natural saturation. Not a photograph, not flat anime, not oily or plastic. No text, no logo, no watermark. Adults.')
HE = ('ROWAN, 27: exactly the face and hair of the man in image 1 (long gentle face, warm light-brown eyes, soft messy wavy chestnut-brown hair over the forehead, clean-shaven). '
      'Outfit: warm medium-brown weathered matte suede zip jacket with a collar worn open (not dark chocolate, not black), cream cable-knit crew sweater, dark charcoal wool trousers with a black belt, dark brown lace-up leather boots. No tattoos, no chain, no watch, no rings.')
SHE = ('MAISIE, 25: exactly the face and hair of the woman in her reference (soft oval face, clear green eyes, soft freckles, faint natural blush, very long wavy warm-brown hair with a thin side braid and a small gold leaf hair pin, gold leaf drop earrings). '
       'Outfit: cream puff-sleeve blouse with a lace-trimmed square neckline under a moss-olive laced bodice embroidered with leaves, a long olive skirt, light brown low-heeled ankle boots. Short nude nails, no rings, no necklace.')
JOBS = {
 'he-upper': ([REF / 'rowan.png', O / 'frames/REF_COLOR.png'],
   'Image 1 is his face and identity; image 2 shows his exact outfit colours (ignore its background and the woman). Waist-up portrait of him alone on a plain white studio background, front view, arms relaxed at his sides, a warm small smile. ' + HE + ' ' + STYLE),
 'she-full': ([REF / 'maisie.png', O / 'frames/S03b.png'],
   'Image 1 is her face and identity; image 2 shows her outfit including the long olive skirt (ignore its background, the can and the gate). Full-body portrait of her alone on a plain white studio background, front view, standing naturally, hands relaxed, head to toe in frame including her boots. ' + SHE + ' ' + STYLE),
 'staging': ([REF / 'rowan.png', REF / 'maisie.png', O / 'frames/REF_COLOR.png'],
   'Full-body two-shot on a plain mid-grey studio background. Image 1 is his identity, image 2 is hers, image 3 shows his outfit colours. ROWAN on the LEFT of the frame, MAISIE on the RIGHT, standing facing each other half an arm apart, both in three-quarter view toward each other, both faces clearly visible, head to toe in frame. ' + HE + ' ' + SHE + ' ' + STYLE),
 'open-key': ([O / 'frames/REF_COLOR.png', REF / 'rowan.png', O / 'frames/REF_HER.png', REF / 'S01-original.png'],
   'Image 1 shows his exact outfit, colours and the warm morning light; image 2 is his identity; image 3 is her identity; image 4 is this place. '
   'A two-shot at the closed waist-high sage-green wooden garden gate, camera standing on the line of the low dry-stone wall: the wall and the closed gate run between them. '
   'ROWAN on the LEFT of the frame, on the cobbled-lane side, with the calm blue bay, rocky headland and small grey-roofed cottages behind him; MAISIE on the RIGHT of the frame, on the garden side, with flowers and the glass greenhouse with wisteria behind her. '
   'They stand facing each other across the gate, about an arm\'s length apart, both waist-up, both in three-quarter view toward each other with both faces clearly visible and large. '
   'He has his hands in his jacket pockets and a hopeful little grin; she holds one grey galvanised watering can lowered at her waist, sceptical, not yet decided. A dark-brown leather flap tool bag rests on top of the stone pillar of the gate. Warm clear morning sun. Only these two people. '
   + HE + ' ' + SHE + ' ' + STYLE),
 'vehicle': ([REF / 'S01-original.png'],
   'Use image 1 only as the place and the light. Product-style picture of exactly one mint-green vintage scooter with a round headlight and a cream seat, parked on the cobbled lane by the low stone wall, side view, whole scooter in frame. No people, no text, no logo, no number plate. ' + STYLE),
}
if sys.argv[1] == 'gen':
    sys.argv = ['gen.py', 'noop']; G = {'__file__': str(O / 'gen.py'), '__name__': 'genlib'}
    exec(open(O / 'gen.py').read().split("if __name__ == '__main__':")[0], G)
    from concurrent.futures import ThreadPoolExecutor
    def one(k):
        refs, p = JOBS[k]; r = G['image']('M_' + k, [str(x) for x in refs], p)
        shutil.copy(O / 'frames' / f'M_{k}.png', M / f'{k}.png'); return r
    with ThreadPoolExecutor(5) as ex:
        for r in ex.map(one, [k for k in JOBS if not (M / f'{k}.png').exists()]): print(*r, flush=True)
elif sys.argv[1] == 'upload':
    def crop(src, out, top, bot, left=0.0, right=1.0):
        im = Image.open(src).convert('RGB'); W, H = im.size; im.crop((int(W * left), int(H * top), int(W * right), int(H * bot))).save(out, quality=93)
    crop(REF / 'rowan.png', M / 'he-head.jpg', 0, .62, .08, .92)
    crop(REF / 'maisie.png', M / 'her-head.jpg', 0, .6, .08, .92)
    shutil.copy(O / 'frames/REF_HER.png', M / 'her-close.png')
    ims = [Image.open(x).convert('RGB') for x in (REF / 'maisie.png', M / 'she-full.png', M / 'her-close.png')]
    h = 1100; ims = [x.resize((int(x.width * h / x.height), h), Image.LANCZOS) for x in ims]
    s = Image.new('RGB', (sum(i.width for i in ims), h), 'white'); x = 0
    for i in ims: s.paste(i, (x, 0)); x += i.width
    s.save(M / 'her-sheet.jpg', quality=92)
    n = int(subprocess.run([FF, '-v', 'error', '-i', str(OPEN), '-map', '0:v', '-c', 'copy', '-f', 'null', '-'], capture_output=True, text=True).stderr or 0) if False else None
    subprocess.run([FF, '-y', '-v', 'error', '-sseof', '-0.15', '-i', str(OPEN), '-frames:v', '1', '-q:v', '2', str(M / 'idle-key.jpg')], check=True)
    shutil.copy(M / 'idle-key.jpg', M / 'open-last.jpg')
    for k in ('he-upper', 'staging', 'open-key', 'vehicle'):
        Image.open(M / f'{k}.png').convert('RGB').save(M / f'{k}.jpg', quality=93)
    sys.path.insert(0, '/Users/vicky/Interactive storyline')
    import os; os.environ.setdefault('MAG_PUBLIC', '1')
    for _l in open('/Users/vicky/Interactive storyline/.env.vivix', encoding='utf-8'):
        if '=' in _l and _l.split('=', 1)[0].strip() == 'VIVIX_API_KEY': os.environ.setdefault('VIVIX_API_KEY', _l.split('=', 1)[1].strip().strip('"\''))
    from vivix_w1 import W1Client
    c = W1Client(); U = json.loads(F.read_text()) if F.exists() else {}
    for key, f in {'face': REF / 'rowan.png', 'face_head': M / 'he-head.jpg', 'outfit': M / 'he-upper.jpg', 'her': M / 'her-sheet.jpg', 'her_head': M / 'her-head.jpg',
                   'staging': M / 'staging.jpg', 'open_key': M / 'open-key.jpg', 'nora': NORA, 'vehicle': M / 'vehicle.jpg', 'look_she_on': M / 'she-full.png', 'idle_key': M / 'idle-key.jpg'}.items():
        U[key] = c.upload(str(f))['url']; F.write_text(json.dumps(U, indent=1)); print(key, U[key], flush=True)
