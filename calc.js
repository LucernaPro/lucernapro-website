/* LucernaPro Coverage Calculator v2.0 (2026-08-03)
 * เครื่องคำนวณพื้นที่ → ขนาดที่ควรซื้อ + ราคารวม (ไทย/อังกฤษ อัตโนมัติจาก <html lang>)
 *
 * แหล่งข้อมูล = ตารางราคาบนหน้านั้นเอง ไม่มีไฟล์ข้อมูลแยก
 *   <table data-calc="1" data-shipping="130"
 *          data-note="ราคารวมเฉพาะน้ำยา ยังไม่รวมค่าหิน" data-note-en="Binder only ...">
 *     <tr><td class="sz" data-sqm="7.5">1.5 kg</td>
 *         <td class="pr" data-price="2760" data-variant="แบบสี">2,760.-</td></tr>
 *     <tr data-calc="skip"> ... แถวที่ไม่เข้าระบบคำนวณ เช่น "สอบถาม" ...
 *
 * data-sqm = พื้นที่ที่ขนาดนั้นทาได้จริง ระบุ "ต่อแถว" ไม่ใช่คำนวณจากอัตราคงที่
 *   เพราะแต่ละสินค้าอัตราต่างกันจริง (PMMA 1 ตร.ม./กก. · SolarPanelDefender 160 ตร.ม./กก.)
 *   และบางตัวขายเป็นชุด/เซ็ตที่คิดจากน้ำหนักไม่ได้
 *
 * GUARD: ไม่มี data-calc บนตาราง หรือไม่มีแถวที่ใช้ได้ → ไม่แสดงอะไรเลย ใส่ทุกหน้าได้ปลอดภัย
 * นโยบาย: หา "ราคารวมต่ำที่สุดที่ยังทาได้ครบพื้นที่" เสมอ ไม่ใช่ชุดที่ทำกำไรสูงสุด
 */
(function () {
  'use strict';
  var table = document.querySelector('.pricecard table[data-calc]');
  if (!table) return;

  var EN = (document.documentElement.lang || 'th').toLowerCase().indexOf('en') === 0;
  var T = EN ? {
    h: 'How much do you need?',
    sub: 'Enter your area — we work out the <b>cheapest combination</b> that still covers it',
    w: 'Width (m)', l: 'Length (m)', a: 'Or enter area (m&sup2;)',
    buf: 'Add 10% for porous or rough surfaces',
    ship: 'Shipping', total: 'Total',
    meta: function (a, got, cov, spare, per) {
      return 'Area ' + a + ' m&sup2; &middot; you get ' + got + ' (covers ' + cov + ' m&sup2;)<br>' +
             'Spare ' + spare + ' m&sup2; &middot; ' + per + ' THB per m&sup2;';
    },
    hint: 'Based on a sound, smooth surface with the full number of coats — rough or porous surfaces always take more. Use this to budget, not to order down to the last gram.',
    big: 'Larger than this table covers — message us for a quote'
  } : {
    h: 'คำนวณว่าต้องซื้อขนาดไหน',
    sub: 'กรอกขนาดพื้นที่ เราจัดชุดที่<b>ราคารวมถูกที่สุด</b>ที่ยังทาได้ครบให้',
    w: 'กว้าง (ม.)', l: 'ยาว (ม.)', a: 'หรือกรอกพื้นที่ (ตร.ม.)',
    buf: 'เผื่อ 10% สำหรับพื้นดูดซึม/ผิวหยาบ',
    ship: 'ค่าจัดส่ง', total: 'รวม',
    meta: function (a, got, cov, spare, per) {
      return 'พื้นที่ ' + a + ' ตร.ม. &middot; ได้มา ' + got + ' (ทาได้ ' + cov + ' ตร.ม.)<br>' +
             'เหลือเผื่อ ' + spare + ' ตร.ม. &middot; เฉลี่ย ' + per + ' บาท/ตร.ม.';
    },
    hint: 'ตัวเลขนี้ตั้งอยู่บนผิวเรียบสภาพดีและทาครบจำนวนรอบ — พื้นหยาบหรือพื้นดูดซึมกินมากกว่านี้เสมอ ใช้ตั้งงบ ไม่ใช่สั่งให้พอดีเป๊ะ',
    big: 'พื้นที่ใหญ่เกินตารางนี้ — ทักมาขอใบเสนอราคาได้เลย'
  };

  var COV  = parseFloat(table.getAttribute('data-coverage') || '0') || 0;
  var SHIP = parseFloat(table.getAttribute('data-shipping') || '0') || 0;

  var variants = {};
  [].forEach.call(table.querySelectorAll('tr'), function (tr) {
    if (tr.getAttribute('data-calc') === 'skip') return;
    var sz = tr.querySelector('td.sz');
    if (!sz) return;
    var sqm = parseFloat(sz.getAttribute('data-sqm') || '0');
    if (!(sqm > 0) && COV > 0) sqm = parseFloat(sz.getAttribute('data-kg') || '0') * COV;
    if (!(sqm > 0)) return;
    var label = (sz.getAttribute('data-label') || sz.textContent).trim().split('\n')[0].trim();
    [].forEach.call(tr.querySelectorAll('td.pr[data-price]'), function (td) {
      var price = parseFloat(td.getAttribute('data-price'));
      if (!(price > 0)) return;
      var v = td.getAttribute('data-variant') || '';
      (variants[v] = variants[v] || []).push({ sqm: sqm, price: price, label: label });
    });
  });
  var names = Object.keys(variants);
  if (!names.length) return;

  function bestCombo(packs, needSqm) {
    var U = 10, need = Math.ceil(needSqm * U - 1e-9), i, j;
    if (need <= 0 || need > 200000) return null;
    var maxU = 0;
    for (i = 0; i < packs.length; i++) maxU = Math.max(maxU, Math.round(packs[i].sqm * U));
    var N = need + maxU;
    var cost = new Float64Array(N + 1), from = new Int32Array(N + 1);
    for (i = 1; i <= N; i++) { cost[i] = Infinity; from[i] = -1; }
    for (i = 1; i <= N; i++) {
      for (j = 0; j < packs.length; j++) {
        var u = Math.round(packs[j].sqm * U);
        var prev = i - u < 0 ? 0 : i - u;
        var c = cost[prev] + packs[j].price;
        if (c < cost[i] - 1e-9) { cost[i] = c; from[i] = j; }
      }
    }
    var bi = need;
    for (i = need; i <= N; i++) if (cost[i] < cost[bi] - 1e-9) bi = i;
    if (!isFinite(cost[bi])) return null;

    var counts = {}, cur = bi, covers = 0, key;
    while (cur > 0 && from[cur] >= 0) {
      var k = from[cur], pk = packs[k];
      counts[k] = (counts[k] || 0) + 1;
      covers += pk.sqm;
      cur -= Math.round(pk.sqm * U); if (cur < 0) cur = 0;
    }
    var items = [], total = 0;
    for (key in counts) {
      var p = packs[key];
      items.push({ label: p.label, sqm: p.sqm, n: counts[key], sum: p.price * counts[key] });
      total += p.price * counts[key];
    }
    items.sort(function (a, b) { return b.sqm - a.sqm; });
    return { items: items, total: total, covers: Math.round(covers * 100) / 100 };
  }

  var money = function (n) { return n.toLocaleString('en-US'); };
  var num   = function (n) { return (Math.round(n * 100) / 100).toLocaleString('en-US'); };

  var css = document.createElement('style');
  css.textContent =
    '.lcalc{margin-top:18px;border:1px solid var(--line);border-radius:14px;background:var(--panel);padding:16px 18px 18px;max-width:720px}' +
    '.lcalc h3{font-family:var(--disp);font-size:16.5px;font-weight:700;color:var(--ink);margin-bottom:3px}' +
    '.lcalc .sub{font-size:13px;color:var(--muted);margin-bottom:14px}' +
    '.lcalc .fields{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}' +
    '.lcalc .f{display:flex;flex-direction:column;gap:5px;flex:1 1 96px;min-width:96px}' +
    '.lcalc .f label{font-size:12px;color:var(--muted)}' +
    '.lcalc input{font-family:var(--body);font-size:16px;padding:10px 12px;border:1.5px solid var(--line);' +
    'border-radius:10px;background:var(--bg);color:var(--ink);width:100%;outline:none}' +
    '.lcalc input:focus{border-color:var(--orange)}' +
    '.lcalc .x{align-self:center;color:var(--muted);font-size:15px;padding-bottom:11px}' +
    '.lcalc .vsel{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}' +
    '.lcalc .vsel button{font-family:var(--body);font-size:13.5px;font-weight:600;padding:8px 14px;' +
    'border:1.5px solid var(--line);border-radius:999px;background:var(--bg);color:var(--ink);cursor:pointer}' +
    '.lcalc .vsel button.on{background:var(--orange);border-color:var(--orange);color:#16130F}' +
    '.lcalc .buffer{margin-top:12px;display:flex;align-items:center;gap:8px;font-size:13.5px;color:var(--muted)}' +
    '.lcalc .buffer input{width:auto;flex:none}' +
    '.lcalc .out{margin-top:14px;border-top:1px solid var(--line);padding-top:14px;font-size:14.5px;color:var(--ink)}' +
    '.lcalc .out .row{display:flex;justify-content:space-between;gap:12px;padding:4px 0}' +
    '.lcalc .out .row b{font-weight:600}' +
    '.lcalc .tot{border-top:1px solid var(--line);margin-top:8px;padding-top:9px;font-family:var(--disp);font-size:18px;font-weight:700}' +
    '.lcalc .tot .o{color:var(--orange)}' +
    '.lcalc .meta{margin-top:8px;font-family:var(--mono);font-size:11.5px;color:var(--muted);line-height:1.75}' +
    '.lcalc .calcnote{margin-top:10px;border-left:3px solid var(--orange);background:var(--panel-2,transparent);'+
    'border-radius:0 8px 8px 0;padding:9px 12px;font-size:13px;color:var(--ink)}' +
    '.lcalc .hint{margin-top:10px;font-size:13px;color:var(--muted)}';
  document.head.appendChild(css);

  var box = document.createElement('div');
  box.className = 'lcalc';
  box.innerHTML =
    '<h3>' + T.h + '</h3><div class="sub">' + T.sub + '</div>' +
    '<div class="fields">' +
      '<div class="f"><label>' + T.w + '</label><input id="lcW" type="number" inputmode="decimal" min="0" step="0.1" placeholder="0"></div>' +
      '<div class="x">&times;</div>' +
      '<div class="f"><label>' + T.l + '</label><input id="lcL" type="number" inputmode="decimal" min="0" step="0.1" placeholder="0"></div>' +
      '<div class="f"><label>' + T.a + '</label><input id="lcA" type="number" inputmode="decimal" min="0" step="0.5" placeholder="0"></div>' +
    '</div>' +
    (names.length > 1 ? '<div class="vsel" id="lcV"></div>' : '') +
    '<label class="buffer"><input type="checkbox" id="lcB"> ' + T.buf + '</label>' +
    '<div class="out" id="lcOut"></div>';

  var card = document.querySelector('.pricecard');
  card.parentNode.insertBefore(box, card.nextSibling);

  var W = box.querySelector('#lcW'), L = box.querySelector('#lcL'),
      A = box.querySelector('#lcA'), B = box.querySelector('#lcB'),
      OUT = box.querySelector('#lcOut');
  var active = names[0];

  if (names.length > 1) {
    var vs = box.querySelector('#lcV');
    names.forEach(function (n) {
      var b = document.createElement('button');
      b.type = 'button'; b.textContent = n;
      if (n === active) b.className = 'on';
      b.addEventListener('click', function () {
        active = n;
        [].forEach.call(vs.children, function (c) { c.className = c === b ? 'on' : ''; });
        run();
      });
      vs.appendChild(b);
    });
  }

  function area() {
    var w = parseFloat(W.value), l = parseFloat(L.value), a = parseFloat(A.value);
    if (w > 0 && l > 0) return w * l;
    return a > 0 ? a : 0;
  }

  function run() {
    var a = area();
    if (!(a > 0)) { OUT.innerHTML = ''; return; }
    var r = bestCombo(variants[active], a * (B.checked ? 1.1 : 1));
    if (!r) { OUT.innerHTML = '<div class="hint">' + T.big + '</div>'; return; }
    var h = '';
    r.items.forEach(function (it) {
      h += '<div class="row"><span>' + it.label + ' &times; ' + it.n + '</span><b>' + money(it.sum) + '.-</b></div>';
    });
    if (SHIP) h += '<div class="row"><span>' + T.ship + '</span><b>' + money(SHIP) + '.-</b></div>';
    h += '<div class="row tot"><span>' + T.total + '</span><span class="o">' + money(r.total + SHIP) + '.-</span></div>';
    var NOTE = table.getAttribute(EN ? 'data-note-en' : 'data-note');
    if (NOTE) h += '<div class="calcnote">' + NOTE + '</div>';
    var spare = r.covers - a;
    h += '<div class="meta">' + T.meta(num(a),
          r.items.map(function (i) { return i.label + '\u00d7' + i.n; }).join(', '),
          num(r.covers), num(spare > 0 ? spare : 0), num(r.total / a)) + '</div>';
    h += '<div class="hint">' + T.hint + '</div>';
    OUT.innerHTML = h;
    if (window.gtag) window.gtag('event', 'calc_used', { area: Math.round(a), total: r.total + SHIP });
  }

  [W, L, A, B].forEach(function (el) { el.addEventListener('input', run); el.addEventListener('change', run); });
  W.addEventListener('input', function () { A.value = ''; });
  L.addEventListener('input', function () { A.value = ''; });
  A.addEventListener('input', function () { W.value = ''; L.value = ''; });
})();
