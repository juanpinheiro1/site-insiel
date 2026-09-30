# Imagens do site

Todas as imagens ficam em `docs/images/`. Em 30/09/2026 os placeholders foram substituídos por **fotos do Pexels** (licença Pexels: uso comercial livre, sem atribuição obrigatória, permitido editar), escolhidas, recortadas e otimizadas pelo script `fotos.py`. Para trocar uma foto por uma real da Insiel, basta salvar o arquivo **com o mesmo nome** em `docs/images/` (o script não sobrescreve arquivos existentes a menos que rode com `--force`).

Nenhuma legenda no site apresenta essas fotos como instalações da Insiel; os textos alternativos são genéricos. As fotos reais (central de monitoramento, equipe, usinas instaladas, semáforos em operação, bancada) devem substituir as de banco assim que possível: são elas que passam credibilidade.

## Fotos em uso (ID Pexels → https://www.pexels.com/photo/ID/)

| Arquivo | Uso | Pexels ID | Descrição |
|---|---|---|---|
| hero-home.jpg | Home, fundo do hero | 35391295 | Campina Grande vista do alto ao anoitecer |
| divisao-seguranca.jpg | Home, card Segurança | 5213883 | Câmera em fachada de tijolo |
| divisao-solar.jpg | Home, Solar (ABRAPE), OG Solar | 35105443 | Usina solar em solo, vista aérea |
| divisao-tecnologia.jpg | Home, card Tecnologia | 36169774 | Placa eletrônica em close, tons escuros |
| divisao-transito.jpg | Home, Trânsito, OG Trânsito | 34444595 | Semáforo à noite com verde e vermelho |
| central-monitoramento.jpg | Home, Segurança, OG Segurança | 32529341 | Operador de costas em sala de controle |
| seg-casa.jpg | Segurança, aba Casa | 4626268 | Casa contemporânea iluminada ao anoitecer |
| seg-empresa.jpg | Segurança, aba Empresa | 15161977 | Loja iluminada fechada à noite |
| sub-monitoramento.jpg | /monitoramento-24h | 11783119 | Pessoa de costas diante de painel de câmeras |
| sub-alarmes.jpg | /alarmes | 1990764 | Teclado de alarme iluminado |
| sub-incendio.jpg | /alarme-de-incendio | 21782970 | Acionador manual vermelho em parede de concreto |
| sub-cftv.jpg | /cftv | 29866272 | Câmera dome em parede |
| sub-acesso.jpg | /controle-de-acesso | 17155842 | Dedo no leitor biométrico |
| sub-cerca.jpg | /cerca-eletrica | 24880269 | Concertina sobre muro (genérica; trocar por cerca elétrica real) |
| sub-automacao.jpg | /automacao | 27523128 | Celular e dispositivos de casa inteligente |
| solar-residencial.jpg | /energia-solar | 38021376 | Painéis em telhado de telha cerâmica |
| solar-comercial.jpg | /energia-solar | 29923348 | Prédios comerciais com painéis, aérea |
| solar-industrial.jpg | /energia-solar | 8782730 | Telhado industrial coberto de painéis, drone |
| solar-instalacao.jpg | /energia-solar, hero | 6961123 | Equipe instalando painéis em telhado grande |
| tornozeleira.jpg | /tornozeleira-eletronica | 30403062 | Plataforma de localização no celular (não há foto de tornozeleira no banco; trocar pela foto real do produto) |
| software-monitoramento.jpg | /software-de-monitoramento | 19317897 | Sala de controle com operadores e telão |
| engenharia.jpg | /tecnologia, /sobre, OG Tecnologia | 37426133 | Técnico soldando placa em laboratório |
| transito-controlador.jpg | /transito | 21812146 | Eletricista em painel de controle |
| transito-led.jpg | /transito | 10163240 | Semáforo verde em noite de neblina |
| sobre-campina.jpg | /sobre, hero | 1579384 | Campina Grande, Açude Velho ao pôr do sol |
| og-*.jpg | Compartilhamento (1200×630) | composição | Foto da divisão escurecida + logo + título, gerada por `fotos.py` |

## Prompts para gerar versões por IA (opcional, se quiser substituir alguma foto de banco)

| Arquivo | Página | Proporção / tamanho | Prompt de geração (inglês) |
|---|---|---|---|
| hero-home.jpg | Home (fundo do hero, sob overlay escuro) | 16:9 · 1920×1080 | Aerial night view of a mid-sized Brazilian city in the northeast, warm streetlights and traffic lights glowing, subtle blue digital network lines connecting buildings, cinematic, dark navy tones, photorealistic, no text |
| divisao-seguranca.jpg | Home, card Segurança (destaque, horizontal) | 16:9 · 1600×900 | Modern white security camera mounted on the corner of a contemporary Brazilian house facade at dusk, soft blue light, shallow depth of field, photorealistic |
| divisao-solar.jpg | Home, card Solar | 4:3 · 1200×900 | Rows of solar panels on a ground-mounted solar plant in the semi-arid landscape of Paraíba, Brazil, clear blue sky, late afternoon sun, photorealistic |
| divisao-tecnologia.jpg | Home, card Tecnologia | 4:3 · 1200×900 | Close-up of an electronics engineering workbench, printed circuit board under a magnifying lamp, oscilloscope in background, blue and red accent lighting, photorealistic |
| divisao-transito.jpg | Home, card Trânsito | 4:3 · 1200×900 | LED traffic light at a Brazilian urban intersection at dusk, red light glowing, light trails from cars, photorealistic |
| central-monitoramento.jpg | Home + Segurança | 16:9 · 1600×900 | Security monitoring center at night, operators seen from behind facing a large video wall with camera feeds and maps, dark room with blue screen glow, photorealistic, no readable text on screens |
| seg-casa.jpg | Segurança, aba "Casa" | 4:3 · 1200×900 | Family home entrance in Brazil at night with a wall-mounted alarm keypad glowing softly near the door, cozy and safe atmosphere, photorealistic |
| seg-empresa.jpg | Segurança, aba "Empresa" | 4:3 · 1200×900 | Small commercial storefront in Brazil after closing time, metal shutter down, security camera and motion sensor visible, night, photorealistic |
| sub-monitoramento.jpg | /seguranca-eletronica/monitoramento-24h | 16:9 · 1600×900 | Operator hand on a keyboard in a monitoring center, alert icon on a screen, blue light, shallow focus, photorealistic |
| sub-alarmes.jpg | /seguranca-eletronica/alarmes | 16:9 · 1600×900 | Modern alarm control panel keypad mounted on a white wall, soft light, minimalist, photorealistic |
| sub-incendio.jpg | /seguranca-eletronica/alarme-de-incendio | 16:9 · 1600×900 | Ceiling smoke detector and red manual fire alarm call point in a clean commercial corridor, photorealistic |
| sub-cftv.jpg | /seguranca-eletronica/cftv | 16:9 · 1600×900 | Dome security camera on a ceiling of a modern commercial space, blurred background, photorealistic |
| sub-acesso.jpg | /seguranca-eletronica/controle-de-acesso | 16:9 · 1600×900 | Person's hand holding an access card near a biometric access control reader at an office turnstile, photorealistic |
| sub-cerca.jpg | /seguranca-eletronica/cerca-eletrica | 16:9 · 1600×900 | Electric fence wires on top of a residential wall in Brazil, blue sky, warning sign without text, photorealistic |
| sub-automacao.jpg | /seguranca-eletronica/automacao | 16:9 · 1600×900 | Smartphone in a hand controlling smart home lights and gate, modern living room in background, warm light, photorealistic |
| solar-residencial.jpg | /energia-solar | 4:3 · 1200×900 | Solar panels on the tiled roof of a Brazilian house, bright sunny day, photorealistic |
| solar-comercial.jpg | /energia-solar | 4:3 · 1200×900 | Solar panels covering the roof of a supermarket or commercial building in Brazil, aerial view, photorealistic |
| solar-industrial.jpg | /energia-solar | 4:3 · 1200×900 | Large industrial warehouse roof fully covered with solar panels, aerial drone view, photorealistic |
| solar-instalacao.jpg | /energia-solar | 16:9 · 1600×900 | Technicians in safety helmets and harnesses installing solar panels, seen from behind, blue sky, photorealistic |
| tornozeleira.jpg | /tecnologia/tornozeleira-eletronica | 16:9 · 1600×900 | Product shot of a generic black electronic ankle monitoring device on a neutral gray studio background, soft lighting, no logos, photorealistic |
| software-monitoramento.jpg | /tecnologia/software-de-monitoramento | 16:9 · 1600×900 | Laptop and monitor showing a generic dark-themed security monitoring dashboard with a map and event list, no readable text, office desk, photorealistic |
| engenharia.jpg | /tecnologia + /sobre | 16:9 · 1600×900 | Electronics lab with engineers seen from behind assembling circuit boards, clean environment, blue accent light, photorealistic |
| transito-controlador.jpg | /transito | 4:3 · 1200×900 | Open traffic signal controller cabinet on a street corner showing electronic modules inside, photorealistic |
| transito-led.jpg | /transito | 4:3 · 1200×900 | Close-up of a modern LED traffic light module, individual LEDs visible, green light on, photorealistic |
| sobre-campina.jpg | /sobre | 16:9 · 2000×1125 | Panoramic view of Campina Grande, Paraíba, Brazil at golden hour, city skyline, photorealistic |
| og-default.jpg, og-home.jpg, og-seguranca.jpg, og-solar.jpg, og-tecnologia.jpg, og-transito.jpg | Compartilhamento (WhatsApp, redes) | 1200×630 | Gerados a partir da imagem da divisão + logo. Hoje: placeholder com logo. Depois que as fotos reais existirem, montar via script (PIL) ou Canva. |

Fotos reais da Insiel (central de monitoramento, equipe de costas, usinas instaladas, semáforos em operação, bancada de engenharia) devem substituir as geradas assim que possível: são elas que passam credibilidade.
