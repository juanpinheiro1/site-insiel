#!/usr/bin/env python3
"""Gera imagens placeholder (gradiente da marca + nome do arquivo) em docs/images/.
Só cria o arquivo se ele NÃO existir — trocar a imagem real é só substituir o arquivo."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

OUT = Path(__file__).parent / 'docs' / 'images'
OUT.mkdir(parents=True, exist_ok=True)

# (arquivo, largura, altura)
IMAGENS = [
    ('hero-home.jpg', 1920, 1080), ('divisao-seguranca.jpg', 1200, 900), ('divisao-solar.jpg', 1200, 900),
    ('divisao-tecnologia.jpg', 1200, 900), ('divisao-transito.jpg', 1200, 900), ('central-monitoramento.jpg', 1600, 900),
    ('seg-casa.jpg', 1200, 900), ('seg-empresa.jpg', 1200, 900), ('sub-monitoramento.jpg', 1600, 900), ('sub-alarmes.jpg', 1600, 900),
    ('sub-incendio.jpg', 1600, 900), ('sub-cftv.jpg', 1600, 900), ('sub-acesso.jpg', 1600, 900), ('sub-cerca.jpg', 1600, 900),
    ('sub-automacao.jpg', 1600, 900), ('solar-residencial.jpg', 1200, 900), ('solar-comercial.jpg', 1200, 900),
    ('solar-industrial.jpg', 1200, 900), ('solar-instalacao.jpg', 1600, 900), ('tornozeleira.jpg', 1600, 900),
    ('software-monitoramento.jpg', 1600, 900), ('engenharia.jpg', 1600, 900), ('transito-controlador.jpg', 1200, 900),
    ('transito-led.jpg', 1200, 900), ('sobre-campina.jpg', 2000, 1125),
    ('og-default.jpg', 1200, 630), ('og-home.jpg', 1200, 630), ('og-seguranca.jpg', 1200, 630), ('og-solar.jpg', 1200, 630),
    ('og-tecnologia.jpg', 1200, 630), ('og-transito.jpg', 1200, 630),
]
NAVY, BLUE, LIGHT = (10, 26, 42), (0, 120, 181), (96, 177, 222)

def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def font(size):
    for name in ('segoeui.ttf', 'arial.ttf', 'DejaVuSans.ttf'):
        try: return ImageFont.truetype(name, size)
        except OSError: pass
    return ImageFont.load_default()

def make(name, w, h):
    im = Image.new('RGB', (w, h)); px = im.load()
    for y in range(h):
        for x in range(0, w, 4):
            t = (x / w * .6 + y / h * .4)
            c = lerp(NAVY, BLUE, t) if t < .7 else lerp(BLUE, LIGHT, (t - .7) / .3)
            for k in range(4):
                if x + k < w: px[x + k, y] = c
    d = ImageDraw.Draw(im, 'RGBA')
    # anéis (motivo do logo)
    cx, cy = int(w * .72), int(h * .55)
    for i, r in enumerate((.55, .42, .3)):
        rx, ry = int(w * r), int(w * r * .5)
        d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], outline=(167, 169, 172, 90 - i * 20), width=max(2, w // 600))
    label = name.replace('.jpg', '')
    f1, f2 = font(max(28, w // 22)), font(max(16, w // 50))
    d.text((w * .05, h * .78), label, font=f1, fill=(255, 255, 255, 230))
    d.text((w * .05, h * .78 + f1.size * 1.3), f'placeholder {w}x{h} · substituir pela imagem real', font=f2, fill=(200, 210, 220, 200))
    if name.startswith('og-'):
        try:
            logo = Image.open(Path(__file__).parent / 'docs' / 'img' / 'logo-horizontal.png').convert('RGB')
            lw = int(w * .32); logo = logo.resize((lw, int(lw * logo.size[1] / logo.size[0])))
            card = Image.new('RGB', (lw + 40, logo.size[1] + 30), 'white'); card.paste(logo, (20, 15))
            im.paste(card, (int(w * .05), int(h * .12)))
        except Exception: pass
    im.save(OUT / name, quality=82, optimize=True)

if __name__ == '__main__':
    n = 0
    for name, w, h in IMAGENS:
        if (OUT / name).exists(): continue
        make(name, w, h); n += 1
    print(f'{n} placeholders criados em {OUT}')
