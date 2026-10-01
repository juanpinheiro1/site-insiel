/* Insiel — site.js (sem dependências) */
(function () {
  'use strict';
  var C = window.INSIEL || {};
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var divisao = document.body.getAttribute('data-divisao') || 'seguranca';

  /* ---- header shadow ---- */
  var hdr = document.querySelector('.hdr');
  function onScroll() { if (hdr) hdr.classList.toggle('is-scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---- mobile menu ---- */
  var burger = document.querySelector('.burger'), mnav = document.querySelector('.mnav');
  if (burger && mnav) {
    burger.addEventListener('click', function () {
      var open = mnav.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
  }

  /* ---- reveal on scroll ---- */
  var rv = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    rv.forEach(function (el) { io.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add('is-in'); }); }

  /* ---- counters ---- */
  var counters = document.querySelectorAll('[data-count]');
  function animate(el) {
    var target = parseInt(el.getAttribute('data-count'), 10), prefix = el.getAttribute('data-prefix') || '', suffix = el.getAttribute('data-suffix') || '';
    if (reduce) { el.textContent = prefix + target + suffix; return; }
    var t0 = null, dur = 1400;
    function step(ts) {
      if (!t0) t0 = ts; var p = Math.min(1, (ts - t0) / dur); p = 1 - Math.pow(1 - p, 3);
      el.textContent = prefix + Math.round(target * p) + suffix; if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if (counters.length && 'IntersectionObserver' in window) {
    var io2 = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { animate(e.target); io2.unobserve(e.target); } }); }, { threshold: 0.4 });
    counters.forEach(function (el) { io2.observe(el); });
  } else counters.forEach(animate);

  /* ---- hero network animation ---- */
  var cv = document.querySelector('canvas.hero__net');
  if (cv && !reduce) {
    var ctx = cv.getContext('2d'), W, H, nodes = [], N = 46, raf;
    function resize() {
      var r = cv.parentElement.getBoundingClientRect(); var dpr = Math.min(2, window.devicePixelRatio || 1);
      W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      N = W < 640 ? 26 : 46; nodes = [];
      for (var i = 0; i < N; i++) nodes.push({ x: Math.random() * W, y: Math.random() * H, vx: (Math.random() - .5) * .18, vy: (Math.random() - .5) * .18, r: 1 + Math.random() * 1.6, p: Math.random() * Math.PI * 2 });
    }
    function draw(ts) {
      ctx.clearRect(0, 0, W, H);
      var maxd = W < 640 ? 120 : 160;
      for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i]; a.x += a.vx; a.y += a.vy;
        if (a.x < -10) a.x = W + 10; if (a.x > W + 10) a.x = -10; if (a.y < -10) a.y = H + 10; if (a.y > H + 10) a.y = -10;
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j], dx = a.x - b.x, dy = a.y - b.y, d = Math.sqrt(dx * dx + dy * dy);
          if (d < maxd) { ctx.strokeStyle = 'rgba(96,177,222,' + (0.22 * (1 - d / maxd)).toFixed(3) + ')'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke(); }
        }
      }
      for (var k = 0; k < nodes.length; k++) {
        var n = nodes[k], pulse = 0.55 + 0.45 * Math.sin(ts / 900 + n.p);
        ctx.fillStyle = 'rgba(96,177,222,' + (0.35 + 0.5 * pulse).toFixed(2) + ')'; ctx.beginPath(); ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2); ctx.fill();
      }
      if (running) raf = requestAnimationFrame(draw);
    }
    var running = false;
    function start() { if (!running) { running = true; raf = requestAnimationFrame(draw); } }
    function stop() { running = false; cancelAnimationFrame(raf); }
    resize(); window.addEventListener('resize', resize);
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { es[0].isIntersecting && !document.hidden ? start() : stop(); }).observe(cv); else start();
    document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
  }

  /* ---- tabs ---- */
  document.querySelectorAll('[role="tablist"]').forEach(function (list) {
    var tabs = list.querySelectorAll('[role="tab"]');
    tabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        tabs.forEach(function (t) { t.setAttribute('aria-selected', 'false'); var p = document.getElementById(t.getAttribute('aria-controls')); if (p) p.hidden = true; });
        tab.setAttribute('aria-selected', 'true'); var panel = document.getElementById(tab.getAttribute('aria-controls')); if (panel) panel.hidden = false;
      });
    });
  });

  /* ---- WhatsApp / phone ---- */
  function waLink(div, extra) {
    var num = (C.whatsapp || {})[div] || '';
    var msg = (C.mensagens || {})[div] || 'Olá! Vim pelo site da Insiel.';
    if (extra) msg += ' ' + extra;
    if (!num) return C.telefone_e164 ? 'tel:' + C.telefone_e164 : 'fale-conosco/';
    return 'https://wa.me/' + num + '?text=' + encodeURIComponent(msg);
  }
  window.INSIEL_waLink = waLink;
  document.querySelectorAll('[data-wa]').forEach(function (a) {
    var div = a.getAttribute('data-wa') === 'auto' ? divisao : a.getAttribute('data-wa');
    a.href = waLink(div, a.getAttribute('data-wa-extra') || '');
    if (a.href.indexOf('tel:') === 0) { a.setAttribute('title', 'WhatsApp a definir — ligue para ' + C.telefone); }
    a.addEventListener('click', function () { track('clique_whatsapp', { divisao: div }); });
  });
  document.querySelectorAll('a[href^="tel:"]').forEach(function (a) { a.addEventListener('click', function () { track('clique_telefone', {}); }); });

  /* ---- UTMs ---- */
  try {
    var q = new URLSearchParams(location.search), utm = {};
    ['utm_source', 'utm_medium', 'utm_campaign'].forEach(function (k) { if (q.get(k)) utm[k] = q.get(k); });
    if (Object.keys(utm).length) localStorage.setItem('insiel_utm', JSON.stringify(utm));
  } catch (e) { }
  function getUtm() { try { return JSON.parse(localStorage.getItem('insiel_utm') || '{}'); } catch (e) { return {}; } }

  /* ---- analytics ---- */
  function track(name, params) {
    try { if (window.gtag) gtag('event', name, params || {}); } catch (e) { }
    try { if (window.fbq) fbq('trackCustom', name, params || {}); } catch (e) { }
  }
  window.INSIEL_track = track;

  /* ---- cookie banner ---- */
  var ck = document.querySelector('.cookie');
  if (ck) {
    var ok = false; try { ok = localStorage.getItem('insiel_cookies') === '1'; } catch (e) { }
    if (!ok && (C.ga4_id || C.meta_pixel_id)) ck.classList.add('is-open');
    ck.querySelector('button').addEventListener('click', function () { try { localStorage.setItem('insiel_cookies', '1'); } catch (e) { } ck.classList.remove('is-open'); });
  }

  /* ---- lead forms ---- */
  function onlyDigits(s) { return (s || '').replace(/\D/g, ''); }
  function collect(form) {
    var d = {}, det = {};
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || el.disabled) return;
      if (el.type === 'checkbox') {
        if (el.name === 'consentimento_lgpd') { d.consentimento_lgpd = el.checked; return; }
        if (!el.checked) return; (det[el.name] = det[el.name] || []).push(el.value); return;
      }
      if (el.type === 'radio' && !el.checked) return;
      if (['nome', 'whatsapp', 'email', 'cidade', 'perfil', 'divisao', 'tipo', 'site'].indexOf(el.name) >= 0) d[el.name] = el.value; else if (el.value) det[el.name] = el.value;
    });
    d.detalhes = det; return d;
  }
  window.INSIEL_enviarLead = function (data) {
    var u = getUtm();
    var payload = {
      tipo: data.tipo || 'orcamento', divisao: data.divisao || divisao, perfil: data.perfil || null,
      nome: data.nome, whatsapp: onlyDigits(data.whatsapp), email: data.email || null, cidade: data.cidade || null,
      detalhes: data.detalhes || {}, pagina_origem: location.pathname, utm_source: u.utm_source || null, utm_medium: u.utm_medium || null, utm_campaign: u.utm_campaign || null,
      consentimento_lgpd: !!data.consentimento_lgpd, site: data.site || ''
    };
    if (!C.supabase_url || !C.supabase_anon_key) return Promise.reject(new Error('Formulário ainda não conectado ao banco.'));
    return fetch(C.supabase_url + '/rest/v1/rpc/insiel_novo_lead', {
      method: 'POST', headers: { 'Content-Type': 'application/json', 'apikey': C.supabase_anon_key, 'Authorization': 'Bearer ' + C.supabase_anon_key },
      body: JSON.stringify({ p: payload })
    }).then(function (r) { if (!r.ok) return r.json().then(function (j) { throw new Error(j.message || j.hint || 'Erro ao enviar'); }); return r.json(); });
  };
  document.querySelectorAll('form[data-lead]').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var msg = form.querySelector('.form__msg'), btn = form.querySelector('[type="submit"]');
      var data = collect(form); data.divisao = data.divisao || form.getAttribute('data-lead') || divisao;
      if (!data.consentimento_lgpd) { msg.className = 'form__msg err'; msg.textContent = 'Marque o consentimento para continuar.'; return; }
      if (onlyDigits(data.whatsapp).length < 10) { msg.className = 'form__msg err'; msg.textContent = 'Informe um WhatsApp com DDD.'; return; }
      btn.disabled = true; msg.className = 'form__msg'; msg.textContent = '';
      window.INSIEL_enviarLead(data).then(function () {
        track('lead_enviado', { divisao: data.divisao });
        form.reset(); btn.disabled = false;
        msg.className = 'form__msg ok';
        var wa = waLink(data.divisao, 'Meu nome é ' + data.nome + '.');
        msg.innerHTML = 'Recebemos seu pedido. Vamos retornar pelo WhatsApp informado. <a href="' + wa + '" target="_blank" rel="noopener">Falar agora no WhatsApp</a>.';
      }).catch(function (e) {
        btn.disabled = false; msg.className = 'form__msg err';
        msg.innerHTML = 'Não foi possível enviar agora (' + e.message + '). Fale conosco pelo telefone <a href="tel:' + C.telefone_e164 + '">' + C.telefone + '</a>.';
      });
    });
  });
})();
