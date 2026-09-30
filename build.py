#!/usr/bin/env python3
"""Build do site Insiel: src/pages/*.html + src/templates/base.html -> docs/ (GitHub Pages).

Uso:  python build.py            (usa site_url de src/config/contatos.json)
      python build.py --serve    (build + servidor local em http://localhost:8323)

Cada página em src/pages tem um cabeçalho "key: value" até uma linha "---", depois o HTML do corpo.
Chaves: path, title, description, divisao (seguranca|solar|tecnologia|transito), og (imagem), schema (json opcional).
Placeholders: {{rel}} (prefixo relativo até a raiz), {{icon:nome}}, {{c.campo.sub}} (config), {{img:arquivo|alt|classe}}.
"""
import json, os, re, sys, time, html
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SRC, OUT = ROOT / 'src', ROOT / 'docs'
CFG = json.loads((SRC / 'config' / 'contatos.json').read_text(encoding='utf-8'))
BUILD = str(int(time.time()))
SITE = CFG['site_url'].rstrip('/')

ICONS = json.loads((SRC / 'templates' / 'icons.json').read_text(encoding='utf-8'))

def icon(name, cls=''):
    body = ICONS.get(name)
    if not body:
        raise SystemExit(f'ícone desconhecido: {name}')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{(" class=%s" % json.dumps(cls)) if cls else ""}>{body}</svg>')

def cfg_get(path):
    cur = CFG
    for part in path.split('.'):
        cur = cur[part]
    return cur

def parse_page(p: Path):
    text = p.read_text(encoding='utf-8')
    head, _, body = text.partition('\n---\n')
    meta = {}
    for line in head.splitlines():
        if ':' in line:
            k, v = line.split(':', 1); meta[k.strip()] = v.strip()
    meta['body'] = body
    return meta

def rel_for(path):
    depth = path.strip('/').count('/') + (1 if path.strip('/') else 0)
    return '../' * depth

def render(meta):
    base = (SRC / 'templates' / 'base.html').read_text(encoding='utf-8')
    path = meta['path']; rel = rel_for(path)
    canonical = SITE + path
    og = meta.get('og', 'og-default.jpg')
    og_url = SITE + '/images/' + og
    ctx = {
        'title': meta['title'], 'description': meta['description'], 'canonical': canonical, 'og_image': og_url,
        'rel': rel, 'build': BUILD, 'divisao': meta.get('divisao', 'seguranca'), 'ano': str(date.today().year),
        'body': meta['body'],
        'schema_page': f'<script type="application/ld+json">{meta["schema"]}</script>' if meta.get('schema') else '',
        'schema_org': json.dumps(schema_org(), ensure_ascii=False),
        'analytics': analytics(),
        'config_js': json.dumps({
            'whatsapp': CFG['whatsapp'], 'mensagens': CFG['mensagens_whatsapp'], 'telefone': CFG['telefone'],
            'telefone_e164': CFG['telefone_e164'], 'ga4_id': CFG['ga4_id'], 'meta_pixel_id': CFG['meta_pixel_id'],
            'supabase_url': CFG['supabase_url'], 'supabase_anon_key': CFG['supabase_anon_key'],
        }, ensure_ascii=False),
        'instagram_link': (f'<a href="{CFG["instagram"]}" target="_blank" rel="noopener">Instagram</a>' if CFG['instagram']
                           else '<span class="todo">[PREENCHER Instagram]</span>'),
    }
    out = base
    for _ in range(2):
        for k, v in ctx.items():
            out = out.replace('{{' + k + '}}', v)
    # second pass: body may contain placeholders too
    out = out.replace('{{rel}}', rel)
    out = re.sub(r'\{\{active:(\w+)\}\}', lambda m: 'is-active' if m.group(1) == meta.get('nav', meta.get('divisao')) else '', out)
    out = re.sub(r'\{\{icon:([\w-]+)(?:\|([\w -]+))?\}\}', lambda m: icon(m.group(1), m.group(2) or ''), out)
    out = re.sub(r'\{\{img:([\w.-]+)\|([^|}]*)(?:\|([^}]*))?\}\}',
                 lambda m: f'<img src="{rel}images/{m.group(1)}" alt="{html.escape(m.group(2))}" loading="lazy" decoding="async"{(" class=%s" % json.dumps(m.group(3))) if m.group(3) else ""}>', out)
    out = re.sub(r'\{\{c\.([\w.]+)\}\}', lambda m: str(cfg_get(m.group(1))), out)
    out = re.sub(r'\[PREENCHER([^\]]*)\]', lambda m: f'<span class="todo">[PREENCHER{html.escape(m.group(1))}]</span>', out)
    return out

def schema_org():
    e = CFG['endereco']
    return {
        '@context': 'https://schema.org', '@type': ['Organization', 'LocalBusiness'],
        'name': CFG['empresa'], 'url': SITE + '/', 'logo': SITE + '/img/logo-vertical.png', 'foundingDate': CFG['fundacao'],
        'telephone': CFG['telefone_e164'], 'email': CFG['email'],
        'address': {'@type': 'PostalAddress', 'streetAddress': e['rua'] + ' – ' + e['bairro'], 'addressLocality': e['cidade'],
                    'addressRegion': e['uf'], 'addressCountry': 'BR'},
        'areaServed': CFG.get('area_atendimento','Paraíba, Brasil'),
        'memberOf': {'@type': 'Organization', 'name': 'ABRAPE – Associação Brasileira dos Produtores de Energia Solar'},
    }

def analytics():
    parts = []
    if CFG['ga4_id']:
        parts.append(f'<script async src="https://www.googletagmanager.com/gtag/js?id={CFG["ga4_id"]}"></script>'
                     f'<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{CFG["ga4_id"]}");</script>')
    if CFG['meta_pixel_id']:
        parts.append('<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};'
                     'if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];'
                     f's.parentNode.insertBefore(t,s)}}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","{CFG["meta_pixel_id"]}");fbq("track","PageView");</script>')
    return '\n'.join(parts)

def main():
    pages = []
    for p in sorted((SRC / 'pages').glob('*.html')):
        meta = parse_page(p)
        out_path = OUT / meta['path'].strip('/') / 'index.html' if meta['path'] != '/' else OUT / 'index.html'
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(render(meta), encoding='utf-8')
        pages.append(meta)
        print('  ', meta['path'], '->', out_path.relative_to(ROOT))
    # sitemap / robots / manifest / 404
    today = date.today().isoformat()
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for m in pages:
        if m.get('noindex') == 'true': continue
        sm.append(f'  <url><loc>{SITE}{m["path"]}</loc><lastmod>{today}</lastmod><priority>{m.get("priority","0.6")}</priority></url>')
    sm.append('</urlset>')
    (OUT / 'sitemap.xml').write_text('\n'.join(sm), encoding='utf-8')
    (OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n', encoding='utf-8')
    (OUT / 'manifest.webmanifest').write_text(json.dumps({
        'name': CFG['empresa'], 'short_name': 'Insiel', 'start_url': '/', 'display': 'browser', 'background_color': '#ffffff', 'theme_color': '#0A1A2A',
        'icons': [{'src': '/img/icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': '/img/icon-512.png', 'sizes': '512x512', 'type': 'image/png'}]}, ensure_ascii=False), encoding='utf-8')
    nf = parse_page(SRC / 'templates' / '404.html'); (OUT / '404.html').write_text(render(nf), encoding='utf-8')
    print(f'{len(pages)} páginas geradas em {OUT}')

if __name__ == '__main__':
    main()
    if '--serve' in sys.argv:
        import http.server, functools
        h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
        print('Servindo em http://localhost:8323/'); http.server.ThreadingHTTPServer(('127.0.0.1', 8323), h).serve_forever()
