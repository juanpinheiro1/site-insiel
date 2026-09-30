#!/usr/bin/env python3
"""Gera as 7 subpáginas de Segurança Eletrônica em src/pages/ a partir de um único template.
Editar o conteúdo AQUI e rodar: python gen_subpaginas.py && python build.py"""
import json
from pathlib import Path

P = Path(__file__).parent / 'src' / 'pages'

SUB = [
  dict(slug='monitoramento-24h', nome='Monitoramento 24h', kw='Monitoramento de alarme 24h em Campina Grande', img='sub-monitoramento.jpg', icon='radio',
       desc='Monitoramento de alarme 24 horas em Campina Grande com central própria da Insiel. Operadores de plantão, verificação por câmera e acionamento de apoio.',
       h1='Monitoramento de alarme 24 horas, com central própria.',
       oque='O seu sistema de alarme fica ligado à central de monitoramento da Insiel, em Campina Grande. Cada evento (disparo, pânico, falta de energia, falha de comunicação) chega na hora à tela de um operador, que segue o procedimento combinado com você.',
       paraquem='Casas, apartamentos, lojas, escritórios, clínicas, escolas, galpões e condomínios. Tanto para quem já tem alarme quanto para quem vai instalar do zero.',
       benef=[('Operação própria', 'A central é da Insiel e fica em Campina Grande. O sinal não passa por terceirizado.'), ('Verificação antes de acionar', 'O operador confere as câmeras e liga para você antes de acionar apoio, evitando falsos alarmes.'), ('Vários caminhos de comunicação', 'O alarme pode se comunicar por internet e rede celular, para não depender de um único meio.'), ('Relatório de eventos', 'Você sabe quando o alarme foi armado, desarmado e o que aconteceu em cada ocorrência.')],
       faq=[('O que acontece quando o alarme dispara?', 'O evento chega à central em segundos. O operador identifica o local, entra em contato com você ou com os contatos cadastrados, confere as câmeras quando houver e aciona apoio se for necessário.'), ('Já tenho alarme de outra empresa. Posso migrar?', 'Na maioria dos casos, sim. Fazemos uma avaliação técnica do equipamento e indicamos o que precisa ser ajustado para ligá-lo à central da Insiel.'), ('O monitoramento tem contrato?', 'Sim, o monitoramento é um serviço mensal. As condições e o prazo são apresentados no orçamento.')],
       servico='monitoramento'),
  dict(slug='alarmes', nome='Alarmes', kw='Alarme residencial e comercial em Campina Grande', img='sub-alarmes.jpg', icon='bell',
       desc='Instalação de alarme residencial e comercial em Campina Grande: sensores de porta, janela e presença, central com aplicativo e opção de monitoramento 24h pela Insiel.',
       h1='Alarme com sensores certos no lugar certo.',
       oque='Sistema de alarme com central, sensores de abertura e de presença, sirene e aplicativo para armar e desarmar pelo celular. Projetado para o seu imóvel, com opção de monitoramento pela central da Insiel.',
       paraquem='Residências, comércios, escritórios e imóveis fechados por longos períodos.',
       benef=[('Projeto por ambiente', 'Cada sensor é escolhido conforme o cômodo: abertura, presença, pet-imune, externo.'), ('Aplicativo no celular', 'Arme, desarme e receba avisos de onde estiver.'), ('Pronto para monitorar', 'O sistema já nasce preparado para ligar à central 24h da Insiel.'), ('Equipe própria de instalação', 'Instaladores da Insiel, em Campina Grande.')],
       faq=[('Posso ter alarme sem monitoramento?', 'Sim. O alarme funciona de forma autônoma, com sirene e avisos no celular. O monitoramento pela central é opcional e pode ser contratado depois.'), ('Tenho animais em casa. O sensor vai disparar?', 'Usamos sensores pet-imunes nos ambientes onde há animais, calibrados para o porte deles.'), ('E se faltar energia?', 'A central tem bateria interna e continua funcionando por horas. A falta de energia também pode ser avisada à central.')],
       servico='alarme'),
  dict(slug='alarme-de-incendio', nome='Alarme de Incêndio', kw='Alarme de incêndio em Campina Grande', img='sub-incendio.jpg', icon='flame',
       desc='Sistema de detecção e alarme de incêndio em Campina Grande: detectores de fumaça e temperatura, acionadores manuais e central endereçável, conforme as normas e as exigências do Corpo de Bombeiros.',
       h1='Detecção e alarme de incêndio conforme a norma.',
       oque='Sistema com detectores de fumaça e de temperatura, acionadores manuais, sirenes e central de alarme, projetado conforme as normas técnicas e as exigências do Corpo de Bombeiros para o seu tipo de edificação.',
       paraquem='Empresas, indústrias, hospitais e clínicas, escolas, hotéis, condomínios e prédios comerciais que precisam de projeto e laudo para funcionamento.',
       benef=[('Projeto conforme norma', 'Dimensionamento dos pontos de detecção e alarme conforme a área e o uso do prédio.'), ('Central endereçável', 'Cada detector identificado na central: você sabe exatamente onde começou o alerta.'), ('Integração com o monitoramento', 'O alarme de incêndio pode ser monitorado pela central 24h da Insiel.'), ('Apoio na regularização', 'Documentação técnica para o processo junto ao Corpo de Bombeiros.')],
       faq=[('Preciso de alarme de incêndio para conseguir o alvará?', 'Depende do tipo, da área e da ocupação da edificação. O projeto de segurança contra incêndio define. Avaliamos o seu caso e indicamos o que a norma exige.'), ('Vocês fazem o projeto ou só a instalação?', 'Fazemos o dimensionamento e a instalação do sistema de detecção e alarme, com a documentação técnica correspondente.'), ('O sistema avisa a central da Insiel?', 'Pode avisar. O alarme de incêndio é integrado ao monitoramento 24h quando o cliente contrata o serviço.')],
       servico='incendio'),
  dict(slug='cftv', nome='CFTV (câmeras)', kw='Câmeras de segurança em Campina Grande', img='sub-cftv.jpg', icon='camera',
       desc='Instalação de câmeras de segurança (CFTV) em Campina Grande com gravação e acesso pelo celular. Projeto para residências, comércios e indústrias, integrado ao monitoramento 24h da Insiel.',
       h1='Câmeras com gravação e acesso pelo celular.',
       oque='Sistema de circuito fechado de TV com câmeras internas e externas, gravador e acesso remoto pelo aplicativo. Projetado para cobrir os pontos que importam, com imagem nítida de dia e de noite.',
       paraquem='Residências, lojas, escritórios, clínicas, escolas, indústrias e condomínios.',
       benef=[('Projeto de cobertura', 'Definimos posição, lente e tipo de câmera para cada ponto, sem ângulo morto nem câmera sobrando.'), ('Acesso pelo celular', 'Veja ao vivo e busque gravações de onde estiver.'), ('Visão noturna', 'Câmeras com infravermelho ou cor à noite, conforme o local.'), ('Integração com o monitoramento', 'A central da Insiel pode usar as câmeras para verificar um disparo de alarme.')],
       faq=[('Por quanto tempo as gravações ficam guardadas?', 'Depende da capacidade do gravador e do número de câmeras. Dimensionamos para o período que você precisa, normalmente de 15 a 30 dias.'), ('Posso ver as câmeras pelo celular?', 'Sim. O acesso é feito por aplicativo, com usuário e senha, de qualquer lugar com internet.'), ('Funciona sem internet?', 'A gravação local funciona sem internet. A internet é necessária apenas para o acesso remoto.')],
       servico='cftv'),
  dict(slug='controle-de-acesso', nome='Controle de Acesso', kw='Controle de acesso em Campina Grande', img='sub-acesso.jpg', icon='key',
       desc='Controle de acesso em Campina Grande: fechaduras eletrônicas, cartão, senha, biometria e catracas para empresas, condomínios e clínicas. Instalação pela Insiel.',
       h1='Quem entra, quando entra, por onde entra.',
       oque='Sistema que libera portas, portões e catracas por cartão, senha, biometria ou aplicativo, com registro de cada acesso. Da fechadura de uma sala à portaria de um condomínio.',
       paraquem='Empresas, clínicas, academias, escolas, condomínios e qualquer lugar que precise controlar e registrar a entrada de pessoas.',
       benef=[('Registro de acessos', 'Relatório de quem entrou, por onde e a que horas.'), ('Perfis e horários', 'Cada pessoa com permissões e horários próprios; desligou, bloqueou na hora.'), ('Integração com o alarme', 'O acesso liberado pode desarmar o alarme do setor automaticamente.'), ('Equipamentos por porte', 'Da fechadura autônoma ao sistema em rede com catracas.')],
       faq=[('Biometria ou cartão: qual é melhor?', 'Depende do fluxo e do ambiente. Biometria dispensa cartão e evita empréstimo de credencial; cartão é mais rápido em portarias com grande fluxo. Muitas vezes usamos os dois.'), ('E se faltar energia?', 'Os equipamentos têm bateria e as fechaduras são especificadas para o comportamento seguro exigido (abrir ou permanecer fechada) conforme o local.'), ('Funciona para condomínio?', 'Sim, com controle de moradores, visitantes e prestadores, integrado à portaria.')],
       servico='acesso'),
  dict(slug='cerca-eletrica', nome='Cerca Elétrica', kw='Cerca elétrica em Campina Grande', img='sub-cerca.jpg', icon='fence',
       desc='Instalação de cerca elétrica em Campina Grande dentro da norma, com central de choque, sensor de violação e integração ao alarme monitorado 24h pela Insiel.',
       h1='Cerca elétrica dentro da norma, integrada ao alarme.',
       oque='Cerca elétrica sobre muros e grades, com central certificada, aterramento, placas de advertência e sensor de violação. Ligada ao alarme, avisa a central da Insiel se alguém tentar cortar ou pular.',
       paraquem='Residências, condomínios, comércios, galpões e sítios.',
       benef=[('Instalação conforme norma', 'Equipamentos certificados, aterramento e sinalização como manda a norma técnica.'), ('Sensor de violação', 'Corte ou curto nos fios gera alarme imediato.'), ('Integração ao monitoramento', 'A violação chega à central 24h da Insiel como qualquer outro disparo.'), ('Manutenção preventiva', 'Revisão periódica para manter a eficiência do choque e a segurança.')],
       faq=[('A cerca elétrica é perigosa?', 'Instalada conforme a norma, com central certificada, o choque é pulsante e de baixa corrente: assusta e inibe, sem causar dano. Por isso a instalação correta e a sinalização são obrigatórias.'), ('Posso ligar a cerca ao alarme que já tenho?', 'Sim. A cerca é integrada ao sistema de alarme existente e pode ser monitorada pela central da Insiel.'), ('Quanto tempo dura a instalação?', 'Depende do perímetro. Na visita técnica informamos o prazo.')],
       servico='cerca'),
  dict(slug='automacao', nome='Automação', kw='Automação residencial e comercial em Campina Grande', img='sub-automacao.jpg', icon='smartphone',
       desc='Automação residencial e comercial em Campina Grande: portões, iluminação, cenários e integração com alarme e câmeras, tudo controlado pelo celular. Instalação pela Insiel.',
       h1='Portão, luzes e cenários no seu celular.',
       oque='Automação de portões, iluminação, tomadas e equipamentos, com controle pelo celular e integração com o alarme e as câmeras. Cenários como "saí de casa" armam o alarme, apagam as luzes e fecham o portão de uma vez.',
       paraquem='Residências, escritórios e comércios que querem conforto e segurança no mesmo sistema.',
       benef=[('Um aplicativo para tudo', 'Alarme, câmeras, portão e luzes no mesmo lugar.'), ('Cenários', 'Rotinas por horário ou por evento, como acender a área externa quando o alarme dispara.'), ('Simulação de presença', 'Luzes acendem e apagam quando você viaja.'), ('Instalação integrada', 'Feita pela mesma equipe que instala a segurança, sem conflito entre sistemas.')],
       faq=[('Preciso trocar as luzes e os portões?', 'Não. Na maioria dos casos usamos módulos que se integram ao que já existe.'), ('Funciona sem internet?', 'Os comandos locais continuam funcionando. A internet é necessária para o controle à distância.'), ('Posso começar pequeno?', 'Sim. Muitos clientes começam pelo portão e pela iluminação externa e ampliam depois.')],
       servico='automacao'),
]

TPL = '''path: /seguranca-eletronica/{slug}/
title: {kw} | Insiel
description: {desc}
divisao: seguranca
og: og-seguranca.jpg
priority: 0.7
schema: {schema}
---
<section class="hero hero--short">
  <div class="hero__bg" style="background-image:url('{{{{rel}}}}images/{img}')"></div>
  <canvas class="hero__net" aria-hidden="true"></canvas>
  <div class="wrap">
    <div class="hero__in">
      <p class="kicker"><a href="{{{{rel}}}}seguranca-eletronica/" style="color:inherit">Segurança eletrônica</a> · {nome}</p>
      <h1>{h1}</h1>
      <p class="lead">{desc}</p>
      <div class="btn-row">
        <a class="btn btn--red" href="#orcamento">Pedir orçamento</a>
        <a class="btn btn--outline" data-wa="seguranca" data-wa-extra="Tenho interesse em {nome_lower}." href="#" target="_blank" rel="noopener">{{{{icon:whatsapp}}}} WhatsApp</a>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="kicker">O que é</p>
        <h2>{nome}</h2>
        <p class="lead">{oque}</p>
        <h3 class="mt-2">Para quem é</h3>
        <p>{paraquem}</p>
      </div>
      <div class="split__media rv">{{{{img:{img}|{nome}}}}}</div>
    </div>
  </div>
</section>

<section class="sec sec--off">
  <div class="wrap">
    <p class="kicker">Benefícios</p>
    <h2>Por que fazer com a Insiel.</h2>
    <div class="grid grid--4 mt-2">
{benef_html}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="split" style="align-items:start">
      <div>
        <p class="kicker">Perguntas frequentes</p>
        <h2>Dúvidas sobre {nome_lower}.</h2>
        <div class="faq mt-2">
{faq_html}
        </div>
        <p class="mt-2"><a href="{{{{rel}}}}seguranca-eletronica/">{{{{icon:arrow-right}}}} Ver todos os serviços de segurança</a></p>
      </div>
      <div id="orcamento">
        <form class="form rv" data-lead="seguranca" novalidate>
          <h3>Pedir orçamento de {nome_lower}</h3>
          <p class="hint">Retornamos pelo WhatsApp em horário comercial.</p>
          <input type="hidden" name="tipo" value="orcamento">
          <input type="hidden" name="divisao" value="seguranca">
          <input type="hidden" name="servicos" value="{servico}">
          <div class="hp" aria-hidden="true"><label>Não preencha<input type="text" name="site" tabindex="-1" autocomplete="off"></label></div>
          <div class="f-grid f-grid--2">
            <div class="f f--full"><label for="s-nome">Seu nome</label><input id="s-nome" name="nome" type="text" required autocomplete="name"></div>
            <div class="f"><label for="s-wa">WhatsApp (com DDD)</label><input id="s-wa" name="whatsapp" type="tel" inputmode="tel" required autocomplete="tel" placeholder="(83) 9 9999-9999"></div>
            <div class="f"><label for="s-cid">Bairro / cidade</label><input id="s-cid" name="cidade" type="text" required autocomplete="address-level2"></div>
            <div class="f f--full"><label for="s-perfil">É para</label>
              <select id="s-perfil" name="perfil" required><option value="residencia">Minha casa</option><option value="empresa">Minha empresa</option><option value="industria">Indústria</option><option value="orgao_publico">Órgão público</option></select></div>
            <div class="f f--full"><label class="consent"><input type="checkbox" name="consentimento_lgpd" required><span>Autorizo a Insiel a usar meus dados para retornar este pedido de orçamento, conforme a <a href="{{{{rel}}}}politica-de-privacidade/">política de privacidade</a>.</span></label></div>
          </div>
          <button class="btn btn--red btn--block mt-2" type="submit">Enviar pedido de orçamento</button>
          <div class="form__msg" role="status" aria-live="polite"></div>
        </form>
      </div>
    </div>
  </div>
</section>
'''

for s in SUB:
    schema = json.dumps({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in s['faq']]}, ensure_ascii=False)
    benef_html = '\n'.join(f'      <div class="feat rv"><span class="ico">{{{{icon:{"check"}}}}}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for t, d in s['benef'])
    faq_html = '\n'.join(f'          <details><summary>{q} {{{{icon:plus}}}}</summary><div class="faq__a"><p>{a}</p></div></details>' for q, a in s['faq'])
    out = TPL.format(slug=s['slug'], kw=s['kw'], desc=s['desc'], schema=schema, img=s['img'], nome=s['nome'], nome_lower=s['nome'][0].lower() + s['nome'][1:],
                     h1=s['h1'], oque=s['oque'], paraquem=s['paraquem'], benef_html=benef_html, faq_html=faq_html, servico=s['servico'])
    (P / f"seguranca-eletronica_{s['slug']}.html").write_text(out, encoding='utf-8')
print(f'{len(SUB)} subpáginas geradas')
