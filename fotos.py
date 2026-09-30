#!/usr/bin/env python3
"""Baixa as fotos escolhidas do Pexels (licença Pexels: uso comercial livre, sem atribuição),
recorta na proporção de cada uso, otimiza e grava em docs/images/. Também compõe as imagens OG.
Rodar: python fotos.py            (só baixa o que ainda não está em docs/images/_originais/)
       python fotos.py --force    (refaz tudo)
Para trocar uma foto: mude o ID aqui (ou coloque o arquivo final direto em docs/images/)."""
import sys, urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

ROOT = Path(__file__).parent
OUT = ROOT / 'docs' / 'images'; ORIG = OUT / '_originais'; ORIG.mkdir(parents=True, exist_ok=True)
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128'}
FORCE = '--force' in sys.argv

# arquivo: (id Pexels, largura, altura, foco vertical 0..1 do recorte [0=topo, .5=centro, 1=base], foco horizontal)
FOTOS = {
    'hero-home.jpg':            (35391295, 1920, 1080, .45, .5),   # Campina Grande à noite, aérea (Pexels)
    'divisao-seguranca.jpg':    (5213883, 1600, 900, .45, .5),
    'divisao-solar.jpg':        (35105443, 1200, 900, .5, .5),
    'divisao-tecnologia.jpg':   (36169774, 1200, 900, .5, .5),
    'divisao-transito.jpg':     (34444595, 1200, 900, .45, .5),
    'central-monitoramento.jpg':(32529341, 1600, 900, .5, .5),
    'seg-casa.jpg':             (4626268, 1200, 900, .5, .5),
    'seg-empresa.jpg':          (15161977, 1200, 900, .5, .5),
    'sub-monitoramento.jpg':    (11783119, 1600, 900, .5, .5),
    'sub-alarmes.jpg':          (1990764, 1600, 900, .5, .5),
    'sub-incendio.jpg':         (21782970, 1600, 900, .5, .5),
    'sub-cftv.jpg':             (29866272, 1600, 900, .5, .5),
    'sub-acesso.jpg':           (17155842, 1600, 900, .5, .5),
    'sub-cerca.jpg':            (24880269, 1600, 900, .5, .5),
    'sub-automacao.jpg':        (27523128, 1600, 900, .5, .5),
    'solar-residencial.jpg':    (38021376, 1200, 900, .5, .5),
    'solar-comercial.jpg':      (29923348, 1200, 900, .5, .5),
    'solar-industrial.jpg':     (8782730, 1200, 900, .5, .5),
    'solar-instalacao.jpg':     (6961123, 1600, 900, .5, .5),
    'tornozeleira.jpg':         (30403062, 1600, 900, .5, .5),   # plataforma de localização (sem foto do dispositivo no banco)
    'software-monitoramento.jpg':(19317897, 1600, 900, .5, .5),
    'engenharia.jpg':           (37426133, 1600, 900, .5, .5),
    'transito-controlador.jpg': (21812146, 1200, 900, .5, .5),
    'transito-led.jpg':         (10163240, 1200, 900, .5, .5),
    'sobre-campina.jpg':        (1579384, 2000, 1125, .5, .5),
}
OG = {  # og: (foto base, título)
    'og-default.jpg': ('hero-home.jpg', 'Tecnologia que protege, gera energia e move cidades.'),
    'og-home.jpg': ('hero-home.jpg', 'Tecnologia que protege, gera energia e move cidades.'),
    'og-seguranca.jpg': ('central-monitoramento.jpg', 'Segurança eletrônica com central própria 24 horas.'),
    'og-solar.jpg': ('divisao-solar.jpg', 'Energia solar com centenas de usinas na Paraíba.'),
    'og-tecnologia.jpg': ('engenharia.jpg', 'Engenharia brasileira de equipamentos e software.'),
    'og-transito.jpg': ('divisao-transito.jpg', 'Controle semafórico inteligente, fabricado na Paraíba.'),
}

def baixar(pid):
    f = ORIG / f'{pid}.jpg'
    if not f.exists():
        url = f'https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w=2400'
        f.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read())
    return Image.open(f).convert('RGB')

def recortar(im, w, h, fy=.5, fx=.5):
    sw, sh = im.size; alvo = w / h
    if sw / sh > alvo:  # larga demais: corta largura
        nw = int(sh * alvo); x = int((sw - nw) * fx); box = (x, 0, x + nw, sh)
    else:
        nh = int(sw / alvo); y = int((sh - nh) * fy); box = (0, y, sw, y + nh)
    im = im.crop(box)
    if im.size[0] < w: w, h = im.size[0], int(im.size[0] / alvo)
    return im.resize((w, h), Image.LANCZOS)

def font(size, bold=True):
    for n in (('segoeuib.ttf' if bold else 'segoeui.ttf'), ('arialbd.ttf' if bold else 'arial.ttf')):
        try: return ImageFont.truetype(n, size)
        except OSError: pass
    return ImageFont.load_default()

def og(nome, base, titulo):
    im = recortar(Image.open(OUT / base).convert('RGB'), 1200, 630)
    im = ImageEnhance.Brightness(im).enhance(.55)
    d = ImageDraw.Draw(im, 'RGBA')
    d.rectangle([0, 380, 1200, 630], fill=(10, 26, 42, 170))
    logo = Image.open(ROOT / 'docs' / 'img' / 'logo-horizontal.png').convert('RGB'); logo.thumbnail((360, 100))
    card = Image.new('RGB', (logo.size[0] + 40, logo.size[1] + 28), 'white'); card.paste(logo, (20, 14))
    im.paste(card, (56, 48))
    f = font(44); linhas = []; atual = ''
    for p in titulo.split():
        t = (atual + ' ' + p).strip()
        if d.textlength(t, font=f) > 1080: linhas.append(atual); atual = p
        else: atual = t
    linhas.append(atual)
    y = 600 - 58 * len(linhas)
    for l in linhas: d.text((56, y), l, font=f, fill='white'); y += 58
    fu = font(26, False); tw = d.textlength('insiel.com.br', font=fu); d.text((1200 - 56 - tw, 64), 'insiel.com.br', font=fu, fill=(255, 255, 255))
    im.save(OUT / nome, quality=84, optimize=True)

if __name__ == '__main__':
    for nome, (pid, w, h, fy, fx) in FOTOS.items():
        if (OUT / nome).exists() and not FORCE and (ORIG / f'{pid}.jpg').exists(): continue
        try:
            im = recortar(baixar(pid), w, h, fy, fx); im.save(OUT / nome, quality=82, optimize=True, progressive=True)
            print('ok', nome, im.size)
        except Exception as e: print('ERRO', nome, pid, e)
    for nome, (base, titulo) in OG.items():
        og(nome, base, titulo); print('og', nome)
