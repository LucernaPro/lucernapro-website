/* LucernaPro Instrumentation v1.0 (2026-08-01)
 * ไฟล์กลางไฟล์เดียวของระบบวัดผลทั้งเว็บ — แก้ GA_ID ที่นี่ที่เดียว มีผลทุกหน้า
 * Event schema:
 *   channel_click  {channel: shopee|lazada|messenger|line, product, lang}  ← conversion หลัก (proxy)
 *   phone_click    {product, lang, number}
 *   tds_download   {product, lang}
 * product = slug จาก pathname ("home", "tilecoatpoly", "post:why-...", ...)
 * GUARD: ถ้า GA_ID ยังเป็น placeholder สคริปต์จะไม่ทำอะไรเลย — push ได้ปลอดภัยก่อนมี ID จริง
 */
(function () {
  var GA_ID = 'G-XXXXXXXXXX'; /* ← วาง Measurement ID จริงตรงนี้ที่เดียว */
  if (GA_ID.indexOf('XXXXXXXXXX') !== -1) return;

  /* ---- โหลด gtag.js ---- */
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', GA_ID);

  /* ---- บริบทของหน้า ---- */
  var path = location.pathname;
  var lang = path.indexOf('/en/') === 0 ? 'en' : 'th';
  var p = path.replace(/^\/en\//, '/').replace(/^\/+|\/+$/g, '');
  var slug;
  if (p === '' || p === 'index.html') slug = 'home';
  else if (p.indexOf('post/') === 0) slug = 'post:' + p.slice(5).replace(/\/index\.html$/, '');
  else slug = p.split('/')[0];

  /* ---- ตัวจำแนกช่องทางจาก href (delegated, capture phase — ยิงก่อน navigate) ---- */
  document.addEventListener('click', function (e) {
    var el = e.target;
    while (el && el.tagName !== 'A') el = el.parentElement;
    if (!el || !el.href) return;
    var h = el.href;
    var base = { product: slug, lang: lang, transport_type: 'beacon' };

    if (h.indexOf('shopee.co.th') !== -1)      { base.channel = 'shopee';    gtag('event', 'channel_click', base); }
    else if (h.indexOf('lazada.co.th') !== -1) { base.channel = 'lazada';    gtag('event', 'channel_click', base); }
    else if (h.indexOf('m.me/') !== -1)        { base.channel = 'messenger'; gtag('event', 'channel_click', base); }
    else if (h.indexOf('lin.ee/') !== -1 || h.indexOf('line.me') !== -1) {
                                                 base.channel = 'line';      gtag('event', 'channel_click', base); }
    else if (h.indexOf('tel:') === 0)          { base.number = h.slice(4);   gtag('event', 'phone_click', base); }
    else if (/\/files\/[^\/]*-tds\.pdf$/.test(h)) {                          gtag('event', 'tds_download', base); }
  }, true);
})();
