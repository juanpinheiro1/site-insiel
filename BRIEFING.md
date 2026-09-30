# PROMPT PARA O CLAUDE CODE — SITE INSIEL

Cole tudo abaixo no Claude Code, junto com o arquivo `logo-insiel.jpg`.

---

## 1. O QUE VOCÊ VAI CONSTRUIR

Construa o novo site institucional e comercial da **Insiel** (domínio: www.insiel.com.br), empresa de base tecnológica de Campina Grande (PB), fundada em 1996.

O site tem **um objetivo principal: gerar pedidos de orçamento**, separados por divisão de negócio. A prioridade comercial hoje é a **Segurança Eletrônica**. Tudo no site deve empurrar o visitante para pedir orçamento ou falar no WhatsApp da divisão certa.

Objetivos secundários, nesta ordem:
1. Passar credibilidade para compradores de governo (tornozeleiras, semáforos) e para empresas (software de monitoramento, usinas solares industriais).
2. Mostrar a Insiel como uma empresa de tecnologia com várias linhas de atuação, e não só como uma instaladora de alarmes.

Público: pessoas físicas e comércios de Campina Grande e da Paraíba (segurança e solar residencial), indústrias e grandes comércios (solar), empresas de segurança eletrônica de todo o Brasil (software e central de monitoramento), e gestores públicos: secretarias de administração penitenciária, prefeituras, superintendências de trânsito.

Idioma: português do Brasil. Tom: direto, técnico quando precisa, sem jargão corporativo e sem exagero de marketing. Frases curtas.

---

## 2. STACK E INFRAESTRUTURA

- **Next.js (App Router) + TypeScript + Tailwind CSS.**
- **Supabase** para gravar os pedidos de orçamento (tabela `leads`). Deixe a estrutura pronta para, no futuro, ligar um painel de gestão ("Mesa de Comando") que vai ler essa tabela. Não construa esse painel agora.
- **Resend** (ou equivalente) para enviar e-mail a atendimento@insiel.com.br a cada novo pedido de orçamento.
- **Cloudflare Turnstile** nos formulários, contra spam.
- **Deploy na Vercel.** Deixe um README em português explicando como publicar e apontar o domínio insiel.com.br.
- Variáveis sensíveis só em `.env`. Crie um `.env.example` documentado.
- Crie o schema do Supabase via migration, com RLS ativado. O formulário público só pode **inserir** em `leads`, nunca ler.

Performance e qualidade:
- Lighthouse acima de 90 em todas as categorias, no celular.
- Pensado primeiro para o celular: a maioria do tráfego vai vir de Instagram, Google e WhatsApp.
- Imagens em `next/image`, formato WebP/AVIF, com lazy loading.
- Acessibilidade: contraste AA, textos alternativos, navegação por teclado.

---

## 3. IDENTIDADE VISUAL

### Logo
Use o arquivo `logo-insiel.jpg` fornecido. É um símbolo em "i" (elipse azul em cima, corpo vermelho, anéis prateados em volta), com "insiel" e "Tecnologia Eletrônica" em grafite logo abaixo.

- O arquivo tem fundo branco, então o **header deve ser branco**, fixo no topo e com leve sombra ao rolar.
- Gere a partir dele uma versão horizontal para o header (símbolo à esquerda, "insiel" à direita) e um favicon só com o símbolo.
- Deixe o logo isolado num componente `<Logo />`, para trocarmos pela versão vetorial (SVG) depois.

### Cores
As cores foram extraídas do logo. Confirmar com o manual da marca, se existir.

| Token | Hex | Uso |
|---|---|---|
| `brand-blue` | #0078B5 | Cor principal: links, títulos de destaque, ícones |
| `brand-blue-light` | #60B1DE | Detalhes, gradientes, hover |
| `brand-red` | #D23428 | **Botões de ação (orçamento/WhatsApp)**, alertas, destaques pontuais |
| `brand-red-dark` | #BF3229 | Hover dos botões vermelhos |
| `graphite` | #4E5357 | Texto principal |
| `silver` | #A7A9AC | Linhas, bordas, detalhes |
| `navy-deep` | #0A1A2A | Fundo das seções escuras (hero, faixas de números) |
| `off-white` | #F5F7FA | Fundo das seções claras alternadas |

Regra: o vermelho é **só para ação**. Se tudo for vermelho, nada chama atenção.

### Tipografia
- Títulos: **Sora** (Google Fonts), pesos 600 e 700. É geométrica e combina com o letreiro do logo.
- Texto: **Inter**, pesos 400 e 500.

### Linguagem visual
"Empresa de tecnologia", não "loja de alarme":
- Hero com fundo escuro (`navy-deep`), linhas finas animadas em azul que remetem a circuito e rede de sensores, com movimento lento e discreto. Use as elipses/anéis do logo como motivo gráfico: arcos finos prateados atravessando seções.
- Cards com cantos levemente arredondados (8px), bordas finas, sem sombras pesadas.
- Ícones em linha (Lucide), traço fino, sempre em `brand-blue`.
- Micro-animações de entrada ao rolar (fade + leve subida), respeitando `prefers-reduced-motion`.
- Nada de fotos de banco genéricas com gente sorrindo para a câmera. Ver seção 7 (Imagens).

---

## 4. ESTRUTURA DE PÁGINAS (MAPA DO SITE)

```
/                               Home
/seguranca-eletronica           Divisão Segurança (página principal da divisão)
  /monitoramento-24h
  /alarmes
  /alarme-de-incendio
  /cftv
  /controle-de-acesso
  /cerca-eletrica
  /automacao
/energia-solar                  Divisão Energia Solar
/tecnologia                     Divisão Desenvolvimento de Equipamentos e Software
  /tornozeleira-eletronica
  /software-de-monitoramento
/transito                       Divisão Controle Semafórico
/sobre                          História, linha do tempo, ABRAPE
/orcamento                      Formulário de orçamento em etapas
/contato
/politica-de-privacidade        LGPD
/area-do-cliente                Página provisória (ver seção 6)
```

### Header (todas as páginas)
- Logo | Segurança | Energia Solar | Tecnologia | Trânsito | Sobre | Contato
- "Segurança" abre um menu com as 7 subpáginas.
- À direita: link discreto "Área do Cliente" e botão vermelho **"Pedir orçamento"**.
- No celular: menu hambúrguer, com o botão "Pedir orçamento" sempre visível.

### Footer (todas as páginas)
- Logo, frase curta: "Tecnologia eletrônica desde 1996."
- Colunas: Divisões | Institucional | Contato.
- Endereço: Rua João Florentino de Carvalho, 43 – José Pinheiro, Campina Grande – PB.
- Telefone: (83) 3342-0699 | E-mail: atendimento@insiel.com.br
- Instagram: [PREENCHER]
- Selo/menção: "Associada à ABRAPE – Associação Brasileira dos Produtores de Energia Solar".
- Razão social e CNPJ: [PREENCHER]
- Link para Política de Privacidade.
- Mapa do Google embutido na página de Contato, não no footer.

### WhatsApp flutuante por divisão
- Botão flutuante no canto inferior direito, em todas as páginas.
- O número e a mensagem pré-preenchida **mudam conforme a divisão da página**:
  - Segurança: [PREENCHER WhatsApp] – "Olá! Vim pelo site e quero um orçamento de segurança eletrônica."
  - Solar: [PREENCHER WhatsApp] – "Olá! Vim pelo site e quero um orçamento de energia solar."
  - Tecnologia: [PREENCHER WhatsApp] – "Olá! Vim pelo site e quero falar sobre equipamentos/software."
  - Trânsito: [PREENCHER WhatsApp] – "Olá! Vim pelo site e quero falar sobre controle semafórico."
  - Home, Sobre e Contato: número de Segurança (prioridade comercial).
- Centralize os números em um único arquivo de configuração (`/config/contatos.ts`) para trocar fácil.
- Registre o clique como evento de conversão (ver seção 8).

---

## 5. CONTEÚDO DE CADA PÁGINA

Os textos abaixo são a base. Refine a redação, mas **não invente números, clientes, certificações ou prêmios**. Onde houver [PREENCHER], deixe o marcador visível no código e liste todos no README.

Fatos confirmados que podem ser usados:
- Fundada em **1996**, em Campina Grande (PB).
- **Milhares de clientes** atendidos.
- **Central de monitoramento própria, funcionando 24 horas.**
- **Centenas de usinas solares** instaladas e em funcionamento na Paraíba.
- **Primeira empresa brasileira a produzir tornozeleiras eletrônicas** para monitoramento de presos, em **2007**. Sistemas implantados em diversos estados.
- Desenvolveu **software de monitoramento de alarmes** e **central de monitoramento**, usados por empresas de segurança eletrônica.
- Produz **controladores semafóricos, semáforos em LED e sistemas inteligentes de controle de trânsito**, implantados em cidades da Paraíba.
- É associada à **ABRAPE**, cujo presidente nacional é o diretor da Insiel.

### 5.1 Home `/`

1. **Hero** (fundo escuro, animação de linhas)
   - Título: "Tecnologia que protege, gera energia e move cidades."
   - Subtítulo: "Desde 1996, a Insiel desenvolve e instala soluções eletrônicas para casas, empresas e governos na Paraíba e em todo o Brasil."
   - Botões: **"Proteger meu imóvel"** (vermelho, leva a /seguranca-eletronica) e "Conheça nossas soluções" (contorno, rola até as divisões).

2. **Faixa de números** (4 contadores animados)
   - "Desde 1996" | "Milhares de clientes atendidos" | "Central 24h própria" | "Centenas de usinas solares"
   - Use texto quando não houver número exato. Não invente valores.

3. **As 4 divisões** (4 cards grandes, com imagem, ícone, 2 linhas de texto e link)
   - Segurança Eletrônica: "Monitoramento 24h, alarmes, câmeras, controle de acesso e cerca elétrica."
   - Energia Solar: "Usinas solares para residências, comércios e indústrias. Centenas em operação na Paraíba."
   - Equipamentos e Software: "Pioneira nacional em tornozeleira eletrônica e software de monitoramento."
   - Trânsito: "Controladores semafóricos, semáforos em LED e controle inteligente de tráfego."
   - O card de Segurança deve ser **maior ou vir primeiro com destaque**: é a prioridade.

4. **Destaque Segurança** (seção dedicada, fundo claro)
   - Título: "Sua casa e sua empresa vigiadas 24 horas, de verdade."
   - Explica em 3 passos como funciona o monitoramento: o sensor dispara → a central Insiel recebe na hora → a equipe verifica, liga para você e aciona apoio se necessário.
   - Botão: "Quero um orçamento de monitoramento".

5. **Por que a Insiel** (4 itens com ícone)
   - "Desde 1996 no mercado"
   - "Central de monitoramento própria": o sinal não passa por terceirizado.
   - "Engenharia própria": a Insiel fabrica equipamentos e software, não só revende.
   - "Equipe técnica local em Campina Grande"

6. **Pioneirismo** (faixa escura)
   - "Em 2007, a Insiel se tornou a primeira empresa brasileira a produzir tornozeleiras eletrônicas." Link para /tecnologia.

7. **Selo ABRAPE** (faixa curta): "A Insiel é associada à ABRAPE – Associação Brasileira dos Produtores de Energia Solar, presidida nacionalmente pelo diretor da empresa."

8. **Chamada final**: "Fale com um especialista da Insiel" + botões Orçamento e WhatsApp.

### 5.2 Segurança Eletrônica `/seguranca-eletronica` (PÁGINA MAIS IMPORTANTE)

1. Hero: "Segurança eletrônica com central própria 24 horas." / Subtítulo: "Projetamos, instalamos e monitoramos. Tudo com equipe da Insiel, em Campina Grande e região." / Botão vermelho: "Pedir orçamento de segurança".
2. **Seletor de perfil** (abas ou 2 cards): "Para sua casa" | "Para sua empresa". Cada aba mostra os serviços mais indicados para o perfil.
3. **Grade de serviços** (7 cards, cada um com link para sua subpágina): Monitoramento 24h, Alarmes, Alarme de Incêndio, CFTV (câmeras), Controle de Acesso, Cerca Elétrica, Automação.
4. **Como funciona o monitoramento** (linha do tempo visual em 4 passos).
5. **Central de monitoramento Insiel**: bloco com imagem da central e texto sobre operação própria 24h/7 dias.
6. **Perguntas frequentes** (acordeão, com schema FAQ para o Google). Perguntas-base:
   - "O que acontece quando o alarme dispara?"
   - "Preciso de internet para ter monitoramento?" [confirmar resposta técnica]
   - "Posso ver minhas câmeras pelo celular?"
   - "Vocês atendem quais cidades?" [PREENCHER]
   - "Quanto tempo leva a instalação?" [PREENCHER]
   - "Já tenho alarme de outra empresa. Vocês podem monitorar?" [confirmar]
7. **Formulário curto embutido** (nome, WhatsApp, bairro/cidade, casa ou empresa, serviço de interesse) que grava em `leads` com `divisao = 'seguranca'`.

**Subpáginas de Segurança** (/monitoramento-24h, /alarmes etc.): um único template reutilizável com hero curto, "o que é", "para quem é", benefícios em 3 a 4 itens, imagem, FAQ específico de 3 perguntas e o formulário curto. Cada uma com title e description próprios para o Google, focados em "[serviço] em Campina Grande".

### 5.3 Energia Solar `/energia-solar`

1. Hero: "Energia solar com quem já instalou centenas de usinas na Paraíba." / Botão: "Quero reduzir minha conta de luz".
2. Três perfis em cards: Residencial | Comercial | Industrial, cada um com 3 benefícios.
3. Etapas do projeto: visita técnica → projeto → homologação na concessionária → instalação → monitoramento da geração.
4. Bloco ABRAPE (autoridade setorial).
5. FAQ (economia, prazo de retorno, manutenção, financiamento [PREENCHER se houver]).
6. Formulário com os campos: valor médio da conta de luz, tipo de imóvel e cidade. Grava com `divisao = 'solar'`.

### 5.4 Tecnologia `/tecnologia`

Tom mais institucional, voltado a **governo e empresas**.
1. Hero: "Engenharia brasileira de equipamentos eletrônicos e software." / Subtítulo: "Da tornozeleira eletrônica ao software de monitoramento: a Insiel projeta e produz."
2. Linha do tempo da inovação: 1996 fundação → 2007 primeira tornozeleira eletrônica produzida no Brasil → [PREENCHER outros marcos: software de monitoramento, central, semáforos].
3. Cards para as 2 subpáginas.
4. Botão: "Falar com a área de projetos" (formulário com os campos: órgão/empresa, cargo, estado, necessidade).

**`/tornozeleira-eletronica`**: pioneirismo em 2007, sistemas implantados em diversos estados (listar só com autorização: [PREENCHER estados]), como funciona o monitoramento eletrônico de pessoas (dispositivo + plataforma + central), foco em confiabilidade. Botão: "Solicitar apresentação técnica". Linguagem sóbria: é compra pública.

**`/software-de-monitoramento`**: software e central de monitoramento de alarmes para **empresas de segurança eletrônica**. Benefícios para o dono da empresa de segurança (recepção de eventos, gestão de clientes, relatórios) [PREENCHER nome do produto e funcionalidades]. Botão: "Agendar demonstração".

### 5.5 Trânsito `/transito`

1. Hero: "Controle semafórico inteligente, fabricado na Paraíba."
2. Produtos: Controladores semafóricos | Semáforos em LED | Sistemas inteligentes de controle de trânsito.
3. Benefícios para o município: economia de energia com LED, menos manutenção, gestão de tráfego.
4. "Implantado em cidades da Paraíba" [PREENCHER nomes, se autorizados].
5. Formulário para prefeituras (município, cargo, necessidade). Grava com `divisao = 'transito'`.

### 5.6 Sobre `/sobre`
- História desde 1996 em Campina Grande.
- Linha do tempo (mesma da página de Tecnologia, mais completa).
- As 4 divisões resumidas.
- ABRAPE.
- Missão em uma frase [PREENCHER ou propor 2 opções curtas para o cliente escolher].

### 5.7 Orçamento `/orcamento` (formulário em etapas)
- Etapa 1: "O que você precisa?" → Segurança | Energia Solar | Equipamentos/Software | Trânsito.
- Etapa 2: "Para quem?" → Residência | Empresa | Indústria | Órgão público.
- Etapa 3: perguntas específicas da divisão:
  - Segurança: serviços de interesse (múltipla escolha) e "já possui algum sistema?"
  - Solar: valor médio da conta e tipo de ligação (monofásica, bifásica ou trifásica, com a opção "não sei").
  - Tecnologia/Trânsito: órgão/empresa, cargo e necessidade.
- Etapa 4: nome, WhatsApp, e-mail (opcional), cidade, checkbox de consentimento LGPD.
- Ao enviar: grava em `leads`, dispara e-mail para atendimento@insiel.com.br e mostra uma tela de confirmação com o botão "Falar agora no WhatsApp" (número da divisão, com mensagem já contendo o nome e o serviço).
- Barra de progresso visível. Botões grandes. Tudo precisa funcionar bem com o polegar, no celular.
- Aceitar parâmetro na URL (`/orcamento?divisao=solar`) para pular a etapa 1.

### 5.8 Contato `/contato`
Endereço, telefone, e-mail, mapa do Google, WhatsApp por divisão e um formulário simples.

### 5.9 Política de Privacidade
Texto padrão LGPD adaptado: quais dados coletamos no formulário, finalidade (retorno comercial), contato do responsável [PREENCHER], direito de exclusão.

---

## 6. ÁREA DO CLIENTE (PROVISÓRIA)

A área do cliente e o painel dos gestores serão construídos depois, em um projeto separado. **Não construa login nem painel agora.**

Por enquanto:
- `/area-do-cliente` é uma página simples com dois caminhos: "Solicitar atendimento técnico" (formulário que grava em `leads` com `tipo = 'chamado'`) e "Falar com o suporte" (WhatsApp de Segurança).
- Deixe o link no header, para não mudar a navegação quando o sistema chegar.

---

## 7. BANCO DE DADOS (SUPABASE)

Tabela `leads`:
- `id` (uuid), `created_at`
- `tipo`: 'orcamento' | 'chamado' | 'contato'
- `divisao`: 'seguranca' | 'solar' | 'tecnologia' | 'transito'
- `perfil`: 'residencia' | 'empresa' | 'industria' | 'orgao_publico'
- `nome`, `whatsapp`, `email`, `cidade`
- `detalhes` (jsonb: respostas específicas de cada divisão)
- `pagina_origem`, `utm_source`, `utm_medium`, `utm_campaign`
- `status` (default 'novo'): já existe pensando na futura Mesa de Comando
- `consentimento_lgpd` (boolean, obrigatório true)

RLS: o público anônimo só insere. A leitura fica restrita à service role.

---

## 8. SEO E MEDIÇÃO

- Title e meta description únicos em cada página, focados em busca local: "monitoramento de alarme Campina Grande", "câmeras de segurança Campina Grande", "energia solar Paraíba", "cerca elétrica Campina Grande", "controlador semafórico" etc.
- Schema.org `LocalBusiness` (com endereço, telefone e horário [PREENCHER]), `Organization` com `foundingDate: 1996` e `FAQPage` nas páginas com FAQ.
- `sitemap.xml`, `robots.txt` e Open Graph com imagem por divisão, para o link ficar bonito no WhatsApp.
- Google Analytics 4 e Meta Pixel (IDs em `.env`), com banner de cookies simples.
- Eventos de conversão: `lead_enviado` (com divisão), `clique_whatsapp` (com divisão), `clique_telefone`.
- Capturar UTMs na primeira visita e mandar junto com o lead.

---

## 9. IMAGENS

Todas as imagens do site serão geradas por IA ou retiradas de banco de imagens nesta primeira versão.

**Regras:**
1. Crie a pasta `/public/images/` com os nomes de arquivo abaixo e use **placeholders** (gradiente da marca + nome da imagem escrito) nas proporções corretas, para que a troca seja só substituir o arquivo.
2. Gere um arquivo `IMAGENS.md` na raiz do projeto com a tabela completa: arquivo, página, proporção, tamanho mínimo e prompt de geração.
3. **Nenhuma imagem gerada por IA pode ter legenda que a apresente como obra real da Insiel** (ex.: "Usina instalada em Patos"). Legendas genéricas apenas. As fotos reais entram depois, substituindo as geradas.
4. Nada de rostos em close. Pessoas aparecem de costas, em silhueta ou fora de foco.
5. Estilo comum a todas: fotografia realista, luz natural ou noturna azulada, tons frios com um toque de vermelho quando couber, sem texto na imagem, sem marcas de terceiros.

**Lista de imagens** (os prompts estão em inglês porque os geradores funcionam melhor assim):

| Arquivo | Página | Proporção | Prompt |
|---|---|---|---|
| `hero-home.jpg` | Home (fundo do hero, sob overlay escuro) | 16:9, 2400px | Aerial night view of a mid-sized Brazilian city in the northeast, warm streetlights and traffic lights glowing, subtle blue digital network lines connecting buildings, cinematic, dark navy tones, photorealistic, no text |
| `divisao-seguranca.jpg` | Home, card Segurança | 4:3, 1200px | Modern white security camera mounted on the corner of a contemporary Brazilian house facade at dusk, soft blue light, shallow depth of field, photorealistic |
| `divisao-solar.jpg` | Home, card Solar | 4:3, 1200px | Rows of solar panels on a ground-mounted solar plant in the semi-arid landscape of Paraíba, Brazil, clear blue sky, late afternoon sun, photorealistic |
| `divisao-tecnologia.jpg` | Home, card Tecnologia | 4:3, 1200px | Close-up of an electronics engineering workbench, printed circuit board under a magnifying lamp, oscilloscope in background, blue and red accent lighting, photorealistic |
| `divisao-transito.jpg` | Home, card Trânsito | 4:3, 1200px | LED traffic light at a Brazilian urban intersection at dusk, red light glowing, light trails from cars, photorealistic |
| `central-monitoramento.jpg` | Segurança + Home | 16:9, 1800px | Security monitoring center at night, operators seen from behind facing a large video wall with camera feeds and maps, dark room with blue screen glow, photorealistic, no readable text on screens |
| `seg-casa.jpg` | Segurança, aba "Casa" | 4:3, 1200px | Family home entrance in Brazil at night with a wall-mounted alarm keypad glowing softly near the door, cozy and safe atmosphere, photorealistic |
| `seg-empresa.jpg` | Segurança, aba "Empresa" | 4:3, 1200px | Small commercial storefront in Brazil after closing time, metal shutter down, security camera and motion sensor visible, night, photorealistic |
| `sub-monitoramento.jpg` | /monitoramento-24h | 16:9, 1600px | Operator hand on a keyboard in a monitoring center, alert icon on a screen, blue light, shallow focus, photorealistic |
| `sub-alarmes.jpg` | /alarmes | 16:9, 1600px | Modern alarm control panel keypad mounted on a white wall, soft light, minimalist, photorealistic |
| `sub-incendio.jpg` | /alarme-de-incendio | 16:9, 1600px | Ceiling smoke detector and red manual fire alarm call point in a clean commercial corridor, photorealistic |
| `sub-cftv.jpg` | /cftv | 16:9, 1600px | Dome security camera on a ceiling of a modern commercial space, blurred background, photorealistic |
| `sub-acesso.jpg` | /controle-de-acesso | 16:9, 1600px | Person's hand holding an access card near a biometric access control reader at an office turnstile, photorealistic |
| `sub-cerca.jpg` | /cerca-eletrica | 16:9, 1600px | Electric fence wires on top of a residential wall in Brazil, blue sky, warning sign without text, photorealistic |
| `sub-automacao.jpg` | /automacao | 16:9, 1600px | Smartphone in a hand controlling smart home lights and gate, modern living room in background, warm light, photorealistic |
| `solar-residencial.jpg` | /energia-solar | 4:3, 1200px | Solar panels on the tiled roof of a Brazilian house, bright sunny day, photorealistic |
| `solar-comercial.jpg` | /energia-solar | 4:3, 1200px | Solar panels covering the roof of a supermarket or commercial building in Brazil, aerial view, photorealistic |
| `solar-industrial.jpg` | /energia-solar | 4:3, 1200px | Large industrial warehouse roof fully covered with solar panels, aerial drone view, photorealistic |
| `solar-instalacao.jpg` | /energia-solar | 16:9, 1600px | Technicians in safety helmets and harnesses installing solar panels, seen from behind, blue sky, photorealistic |
| `tornozeleira.jpg` | /tornozeleira-eletronica | 16:9, 1600px | Product shot of a generic black electronic ankle monitoring device on a neutral gray studio background, soft lighting, no logos, photorealistic |
| `software-monitoramento.jpg` | /software-de-monitoramento | 16:9, 1600px | Laptop and monitor showing a generic dark-themed security monitoring dashboard with a map and event list, no readable text, office desk, photorealistic |
| `engenharia.jpg` | /tecnologia + /sobre | 16:9, 1600px | Electronics lab with engineers seen from behind assembling circuit boards, clean environment, blue accent light, photorealistic |
| `transito-controlador.jpg` | /transito | 4:3, 1200px | Open traffic signal controller cabinet on a street corner showing electronic modules inside, photorealistic |
| `transito-led.jpg` | /transito | 4:3, 1200px | Close-up of a modern LED traffic light module, individual LEDs visible, green light on, photorealistic |
| `sobre-campina.jpg` | /sobre | 16:9, 2000px | Panoramic view of Campina Grande, Paraíba, Brazil at golden hour, city skyline, photorealistic |
| `og-*.jpg` | Compartilhamento | 1200x630 | Gerar a partir das imagens de divisão + logo + título da página (fazer via código, com a `next/og`) |

---

## 10. ENTREGA

Ao terminar, entregue:
1. O projeto rodando localmente, com instruções no README.
2. A lista de todos os [PREENCHER] pendentes, em um arquivo `PENDENCIAS.md`.
3. `IMAGENS.md` com a tabela de imagens.
4. Instruções para deploy na Vercel e configuração do domínio insiel.com.br.
5. Um relatório do Lighthouse (celular) da Home e da página de Segurança.

Trabalhe por etapas: primeiro a estrutura e o design system, depois a Home e a Segurança (prioridade), depois as demais divisões, por último formulários, banco e SEO. Mostre a Home e a Segurança para aprovação antes de seguir com o resto.
