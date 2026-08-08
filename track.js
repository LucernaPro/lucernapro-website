/* LucernaPro Instrumentation v1.2 (2026-08-08)
 * ไฟล์กลางไฟล์เดียวของระบบวัดผลทั้งเว็บ — แก้ ID 3 ตัวข้างล่างที่นี่ที่เดียว มีผลทุกหน้า
 * Event schema:
 *   channel_click  {channel: shopee|lazada|messenger|line, product, lang}  ← conversion หลัก (proxy)
 *   phone_click    {product, lang, number}
 *   tds_download   {product, lang, doc: tds|sds}
 *   social_click   {channel: facebook, product, lang}  ← intent อ่อน แยกจาก channel_click โดยเจตนา ห้ามยุบรวม
 * product = slug จาก pathname ("home", "tilecoatpoly", "post:why-...", ...)
 * GUARD: ID ไหนยังเป็น placeholder ส่วนนั้นจะไม่ทำงาน — push ได้ปลอดภัยก่อนมี ID จริง
 */
(function () {
  /* ---- workers.dev → โดเมนจริง (v1.2) ----
   * 301 ฝั่ง server ทำไม่ได้ (deploy เป็น assets-only worker, ไม่มี _worker.js ใน repo)
   * จึง redirect ฝั่ง client: ลิงก์เก่า workers.dev ในแชทลูกค้ายังใช้ได้ แต่เด้งเข้าโดเมนจริง
   * QA: เปิด ?qa=1 ครั้งเดียว → จำทั้ง session (sessionStorage) เดินดูหน้าอื่นต่อได้ไม่เด้ง */
  if (location.hostname.slice(-11) === 'workers.dev') {
    var qa = false;
    try {
      if (location.search.indexOf('qa=1') !== -1) sessionStorage.setItem('lp_qa', '1');
      qa = sessionStorage.getItem('lp_qa') === '1';
    } catch (e) {}
    if (!qa) {
      location.replace('https://www.lucernapro.com' + location.pathname + location.search + location.hash);
      return; /* ไม่โหลด gtag — กัน workers.dev ปนเข้า GA4 */
    }
  }

  var GA_ID    = 'G-WHKF5BFB2F';   /* ← GA4 Measurement ID (analytics.google.com) */
  var AW_ID    = 'AW-413684054';  /* ← Google Ads tag ID (conversion action "channel_click", 2 ส.ค. 2026) */
  var AW_LABEL = '52a7CMza2NocENaiocUB';     /* ← conversion label ของ action "channel_click" ใน Ads */
  var hasGA = GA_ID.indexOf('XXXXXXXXXX') === -1;
  var hasAW = AW_ID.indexOf('XXXXXXXXXX') === -1;
  if (!hasGA && !hasAW) return;

  /* ---- โหลด gtag.js (ตัวเดียวรับได้ทั้ง GA4 และ AW) ---- */
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + (hasGA ? GA_ID : AW_ID);
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  if (hasGA) gtag('config', GA_ID);
  if (hasAW) gtag('config', AW_ID);

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
    var m;

    if (h.indexOf('shopee.co.th') !== -1)      { base.channel = 'shopee';    fireConv(base); }
    else if (h.indexOf('lazada.co.th') !== -1) { base.channel = 'lazada';    fireConv(base); }
    else if (h.indexOf('m.me/') !== -1)        { base.channel = 'messenger'; fireConv(base); }
    else if (h.indexOf('lin.ee/') !== -1 || h.indexOf('line.me') !== -1) {
                                                 base.channel = 'line';      fireConv(base); }
    else if (h.indexOf('tel:') === 0)          { base.number = h.slice(4);   gtag('event', 'phone_click', base); }
    else if ((m = /\/files\/[^\/]*-(tds|sds)\.pdf$/.exec(h))) {
                                                 base.doc = m[1];            gtag('event', 'tds_download', base); }
    else if (/https?:\/\/(www\.)?facebook\.com\//.test(h)) {
                                                 base.channel = 'facebook';  gtag('event', 'social_click', base); }
  }, true);

  /* channel_click = conversion proxy: ยิง GA4 เสมอ + ยิง Ads conversion ถ้ามี label */
  function fireConv(base) {
    gtag('event', 'channel_click', base);
    if (hasAW && AW_LABEL.indexOf('XXXXXXXXXX') === -1) {
      gtag('event', 'conversion', { send_to: AW_ID + '/' + AW_LABEL, transport_type: 'beacon' });
    }
  }
})();
