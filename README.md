# Site Insiel — insiel.com.br

Site institucional e comercial da Insiel Tecnologia Eletrônica. Site **estático** (HTML/CSS/JS), gerado por um script Python e publicado no **GitHub Pages**. Os pedidos de orçamento vão para o **Supabase** (schema `insiel`, projeto ABRAPE SOLAR `puepmnyffpfjttxmwfjt`).

Briefing completo: [BRIEFING.md](BRIEFING.md). Pendências de conteúdo: [PENDENCIAS.md](PENDENCIAS.md). Imagens: [IMAGENS.md](IMAGENS.md).

## Estrutura

```
build.py                 gera docs/ a partir de src/ (python build.py)
gen_placeholders.py      cria as imagens placeholder que ainda não existem em docs/images/
src/config/contatos.json telefones, WhatsApp por divisão, e-mail, IDs de analytics, chave pública Supabase
src/templates/base.html  cabeçalho, rodapé, WhatsApp flutuante, cookies, schema.org
src/templates/icons.json ícones em linha (estilo Lucide)
src/pages/*.html         uma página por arquivo: cabeçalho "chave: valor" + "---" + HTML do corpo
docs/                    SAÍDA publicada (GitHub Pages serve esta pasta). Não editar à mão.
docs/images/             fotos do site (placeholders até chegarem as reais — só substituir o arquivo)
docs/img/                logo, favicons
assets/logo-insiel.jpg   logo original
```

## Editar e publicar

1. Editar `src/pages/…` ou `src/config/contatos.json`.
2. Rodar `python build.py` (ou `python build.py --serve` para ver em http://localhost:8323/).
3. `git add -A && git commit -m "…" && git push` — o GitHub Pages publica em ~1 minuto.

Placeholders disponíveis nas páginas: `{{rel}}` (caminho relativo até a raiz), `{{icon:nome}}`, `{{img:arquivo.jpg|texto alternativo}}`, `{{c.campo.subcampo}}` (valores de contatos.json). Qualquer `[PREENCHER …]` no texto vira um marcador amarelo visível na página.

## Formulários e banco

- Os formulários (`<form data-lead="divisao">`) chamam a RPC `public.insiel_novo_lead(jsonb)` com a chave pública. A função valida, aplica honeypot e limite de 3 envios por número a cada 10 minutos, e insere em `insiel.leads`.
- O schema `insiel` **não é exposto** na API. O público não lê nada; a leitura é só com a service role (futura Mesa de Comando).
- Campos: tipo (orcamento|chamado|contato), divisao (seguranca|solar|tecnologia|transito), perfil, nome, whatsapp, email, cidade, detalhes (jsonb), pagina_origem, utm_*, status (novo|em_contato|convertido|descartado), consentimento_lgpd, notificado_em.
- Aviso por e-mail: tarefa agendada do Claude lê `insiel.leads where notificado_em is null` e envia para atendimento@insiel.com.br (mesmo padrão da ABRAPE). Migrar para Resend quando houver conta.

## Domínio insiel.com.br

ATUALIZAÇÃO 30/09/2026: a zona passou para o **DNS do Registro.br** (modo avançado; servidores d/e.sec.dns.br). Os registros abaixo já estão lá, junto com `mesa CNAME juanpinheiro1.github.io`. Qualquer novo registro é feito em registro.br → painel → insiel.com.br → Configurar zona DNS. Registros do site:

| Tipo | Nome | Valor |
|---|---|---|
| A | @ (apex) | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | juanpinheiro1.github.io |

**Não mexer** em MX (`mx.insiel.com.br`), TXT SPF (`v=spf1 include:_spf.hospedagemweb.net -all`) e DKIM (`default._domainkey`): é o e-mail da empresa.
Depois, no repositório GitHub: Settings → Pages → Custom domain `insiel.com.br` + "Enforce HTTPS" (o arquivo `docs/CNAME` já faz isso no push).

## Analytics

Preencher `ga4_id` e `meta_pixel_id` em `src/config/contatos.json`; o banner de cookies só aparece quando algum ID existe. Eventos: `lead_enviado` (divisao), `clique_whatsapp` (divisao), `clique_telefone`.
