# Pendências de conteúdo (marcadas como [PREENCHER] no site)

Tudo abaixo aparece como marcador amarelo nas páginas até ser preenchido. Contatos são editados em `src/config/contatos.json`; textos nas páginas em `src/pages/`.

## Já resolvidos (30/09/2026)
- [x] WhatsApp: (83) 98725-9010 para as 4 divisões (número único informado pelo usuário; o site assume o 9 na frente)
- [x] Razão social: Insiel Tecnologia Eletrônica Ltda.
- [x] CNPJ: não divulgar (removido do rodapé)
- [x] Instagram: não há (removido)
- [x] Área de atendimento: Paraíba, Pernambuco e Rio Grande do Norte
- [x] FAQ de Segurança: cidades atendidas e prazo de instalação (resposta genérica, sem prazo fixo)

## Contatos (contatos.json)
- [ ] CEP
- [ ] Horário de atendimento (página Contato e schema LocalBusiness)
- [ ] IDs do Google Analytics 4 e do Meta Pixel

## Confirmar tecnicamente (texto já publicado, sem marcador)
- [ ] "Preciso de internet para ter monitoramento?" — resposta diz que há internet e rede celular
- [ ] "Já tenho alarme de outra empresa" — resposta diz que na maioria dos casos dá para migrar
- [ ] Subpáginas de Segurança: retenção de gravação (15 a 30 dias), sensores pet-imunes, bateria da central

## Energia Solar
- [ ] Há financiamento/parceiros? (FAQ)

## Tecnologia
- [ ] Estados onde a tornozeleira foi implantada (listar só com autorização)
- [ ] Nome do software de monitoramento e demais funcionalidades (aplicativo, integrações, receptoras)
- [ ] Anos dos marcos: software/central e semáforos (linhas do tempo de Tecnologia e Sobre)

## Trânsito
- [ ] Cidades onde os semáforos estão implantados (se autorizado)

## Sobre
- [ ] Missão: escolher a opção 1 ou 2 (ou mandar outra)

## Privacidade
- [ ] Nome do encarregado de dados (DPO), se houver
- [ ] Prazo de guarda dos pedidos sem contratação (sugestão: 24 meses)

## Contas externas (você cria; eu configuro)
- [ ] Resend (e-mail transacional) — hoje o aviso sai por tarefa agendada no Gmail (insiel-aviso-leads-site, de hora em hora, 7h–21h, só com o app aberto)
- [ ] Cloudflare Turnstile (anti-spam) — hoje: honeypot + limite de 3 envios por número a cada 10 min
- [ ] Google Analytics 4 / Meta Pixel

## Imagens
- [x] Placeholders substituídos por fotos do Pexels em 30/09/2026 (ver IMAGENS.md)
- [ ] Trocar por fotos reais da Insiel quando houver: central de monitoramento, equipe, usinas, semáforos, tornozeleira (a foto atual é genérica de plataforma de localização) e cerca elétrica (a atual é concertina)

## Domínio
- [x] 30/09/2026: zona migrada para o DNS do Registro.br (modo avançado, 17 registros, e-mail preservado); insiel.com.br e mesa.insiel.com.br apontados ao GitHub Pages
- [ ] Conferir se o HTTPS forçado ficou ativo nos dois repositórios depois da emissão do certificado (Settings → Pages)
