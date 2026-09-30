# Imagens do site

Todas as imagens ficam em `docs/images/`. Hoje são **placeholders** (gradiente da marca + nome do arquivo), gerados por `gen_placeholders.py`. Para trocar, basta salvar a imagem real **com o mesmo nome** e proporção; nada muda no código.

Regras (do briefing): nenhuma imagem gerada por IA pode ter legenda que a apresente como obra real da Insiel; nada de rostos em close (pessoas de costas, silhueta ou fora de foco); fotografia realista, tons frios com toque de vermelho quando couber, sem texto nem marcas de terceiros. Exportar em JPG qualidade 80–85 (ou WebP) no tamanho indicado.

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
