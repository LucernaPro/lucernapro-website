/* LucernaPro Coverage Calculator v1.0 (2026-08-03)
 * เครื่องคำนวณพื้นที่ → ขนาดที่ควรซื้อ + ราคารวม
 *
 * แหล่งข้อมูล = ตารางราคาบนหน้านั้นเอง ไม่มีไฟล์ข้อมูลแยก
 *   <table data-coverage="5" data-shipping="130">   coverage = ตร.ม. ต่อ 1 กก. เมื่อทาครบ 2 รอบ
 *     <tr><td class="sz" data-kg="1.5">1.5 kg</td>
 *         <td class="pr" data-price="2760" data-variant="แบบสี">2,760.-</td></tr>
 *
 * GUARD: หน้าไหนไม่มี data-coverage หรือไม่มีแถวที่มี data-kg+data-price ครบ
 *        สคริปต์จะไม่แสดงอะไรเลย — ใส่ไว้ทุกหน้าได้อย่างปลอดภัย
 *
 * นโยบายการเลือกขนาด: หา "ราคารวมต่ำที่สุดที่ยังทาได้ครบพื้นที่"
 *   เสมอ — ไม่ใช่ชุดที่ทำกำไรสูงสุด ถ้าเสมอกันให้เลือกชุดที่เหลือทิ้งน้อยกว่า
 */
(function () {
  'use strict';
  var table = document.querySelector('.pricecard table[data-coverage]');
  if (!table) return;

  var COV = parseFloat(table.getAttribute('data-coverage'));           /* ตร.ม./กก. */
  var SHIP = parseFloat(table.getAttribute('data-shipping') || '0') || 0;
  if (!(COV > 0)) return;

  /* ---------- อ่านขนาด/ราคาออกจากตาราง ---------- */
  var variants = {};                        /* ชื่อรุ่น -> [{kg, price}] */
  [].forEach.call(table.querySelectorAll('tr'), function (tr) {
    var sz = tr.querySelector('td.sz[data-kg]');
    if (!sz) return;
    var kg = parseFloat(sz.getAttribute('data-kg'));
    if (!(kg > 0)) return;
    [].forEach.call(tr.querySelectorAll('td.pr[data-price]'), function (td) {
      var price = parseFloat(td.getAttribute('data-price'));
      if (!(price > 0)) return;
      var v = td.getAttribute('data-variant') || '';
      (variants[v] = variants[v] || []).push({ kg: kg, price: price, label: sz.textContent.trim() });
    });
  });
  var names = Object.keys(variants);
  if (!names.length) return;

  /* ---------- หาชุดที่ถูกที่สุดที่ยังคลุมพื้นที่ครบ ----------
     unbounded knapsack บนหน่วย 0.1 กก. — พื้นที่ค้นหาเล็กมาก คำนวณตรงได้ ไม่ต้องประมาณ */
  function bestCombo(packs, needKg) {
    var U = 10, need = Math.ceil(needKg * U - 1e-9);
    if (need <= 0) return null;
    var maxUnit = 0, i, p;
    for (i = 0; i < packs.length; i++) maxUnit = Math.max(maxUnit, Math.round(packs[i].kg * U));
    var N = need + maxUnit;
    var cost = new Float64Array(N + 1), from = new Int32Array(N + 1);
    for (i = 1; i <= N; i++) { cost[i] = Infinity; from[i] = -1; }
    for (i = 1; i <= N; i++) {
      for (var j = 0; j < packs.length; j++) {
        var u = Math.round(packs[j].kg * U);
        var prev = i - u < 0 ? 0 : i - u;
        var c = cost[prev] + packs[j].price;
        if (c < cost[i] - 1e-9) { cost[i] = c; from[i] = j; }
      }
    }
    /* จาก need ขึ้นไป เลือกตัวที่ถูกสุด ถ้าราคาเท่ากันเอาที่เหลือทิ้งน้อยกว่า */
    var bi = need;
    for (i = need; i <= N; i++) if (cost[i] < cost[bi] - 1e-9) bi = i;
    if (!isFinite(cost[bi])) return null;

    var counts = {}, cur = bi, totalKg = 0;
    while (cur > 0 && from[cur] >= 0) {
      var k = from[cur], pk = packs[k];
      counts[k] = (counts[k] || 0) + 1;
      totalKg += pk.kg;
      cur = cur - Math.round(pk.kg * U); if (cur < 0) cur = 0;
    }
    var items = [], total = 0;
    for (var key in counts) {
      p = packs[key];
      items.push({ label: p.label, kg: p.kg, n: counts[key], price: p.price, sum: p.price * counts[key] });
      total += p.price * counts[key];
    }
    items.sort(function (a, b) { return b.kg - a.kg; });
    return { items: items, total: total, kg: Math.round(totalKg * 100) / 100 };
  }

  var baht = function (n) { return n.toLocaleString('en-US'); };
  var num = function (n) { return (Math.round(n * 100) / 100).toLocaleString('en-US'); };

  /* ---------- UI ---------- */
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
    '.lcalc .tot{border-top:1px solid var(--line);margin-top:8px;padding-top:9px;font-family:var(--disp);' +
    'font-size:18px;font-weight:700}' +
    '.lcalc .tot .o{color:var(--orange)}' +
    '.lcalc .meta{margin-top:8px;font-family:var(--mono);font-size:11.5px;color:var(--muted);line-height:1.75}' +
    '.lcalc .hint{margin-top:10px;font-size:13px;color:var(--muted)}';
  document.head.appendChild(css);

  var box = document.createElement('div');
  box.className = 'lcalc';
  box.innerHTML =
    '<h3>คำนวณว่าต้องซื้อขนาดไหน</h3>' +
    '<div class="sub">กรอกขนาดพื้นที่ เราจัดชุดที่<b>ราคารวมถูกที่สุด</b>ที่ยังทาได้ครบให้</div>' +
    '<div class="fields">' +
      '<div class="f"><label>กว้าง (ม.)</label><input id="lcW" type="number" inputmode="decimal" min="0" step="0.1" placeholder="0"></div>' +
      '<div class="x">×</div>' +
      '<div class="f"><label>ยาว (ม.)</label><input id="lcL" type="number" inputmode="decimal" min="0" step="0.1" placeholder="0"></div>' +
      '<div class="f"><label>หรือกรอกพื้นที่ (ตร.ม.)</label><input id="lcA" type="number" inputmode="decimal" min="0" step="0.5" placeholder="0"></div>' +
    '</div>' +
    (names.length > 1 ? '<div class="vsel" id="lcV"></div>' : '') +
    '<label class="buffer"><input type="checkbox" id="lcB"> เผื่อ 10% สำหรับพื้นดูดซึม/ผิวหยาบ</label>' +
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
      b.type = 'button'; b.textContent = n || 'มาตรฐาน';
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
    var need = a * (B.checked ? 1.1 : 1);
    var kgNeeded = need / COV;
    var r = bestCombo(variants[active], kgNeeded);
    if (!r) { OUT.innerHTML = '<div class="hint">พื้นที่ใหญ่เกินตารางนี้ — ทักมาขอใบเสนอราคาได้เลย</div>'; return; }

    var h = '';
    r.items.forEach(function (it) {
      h += '<div class="row"><span>' + it.label + ' × ' + it.n + '</span><b>' + baht(it.sum) + '.-</b></div>';
    });
    if (SHIP) h += '<div class="row"><span>ค่าจัดส่ง</span><b>' + baht(SHIP) + '.-</b></div>';
    var total = r.total + SHIP;
    h += '<div class="row tot"><span>รวม</span><span class="o">' + baht(total) + '.-</span></div>';

    var covers = r.kg * COV, spare = covers - a;
    h += '<div class="meta">' +
         'พื้นที่ ' + num(a) + ' ตร.ม. · ต้องใช้ ' + num(kgNeeded) + ' กก. · ได้มา ' + num(r.kg) + ' กก. (ทาได้ ' + num(covers) + ' ตร.ม.)<br>' +
         'เหลือเผื่อ ' + num(spare > 0 ? spare : 0) + ' ตร.ม. · เฉลี่ย ' + num(r.total / a) + ' บาท/ตร.ม.' +
         (SHIP ? ' (ยังไม่รวมค่าส่ง)' : '') +
         '</div>';
    h += '<div class="hint">ตัวเลขนี้ตั้งอยู่บนผิวเรียบสภาพดีและทาครบ 2 รอบ — พื้นหยาบหรือพื้นดูดซึมกินมากกว่านี้เสมอ ใช้ตั้งงบ ไม่ใช่สั่งให้พอดีเป๊ะ</div>';
    OUT.innerHTML = h;

    if (window.gtag) window.gtag('event', 'calc_used', { area: Math.round(a), total: total });
  }

  [W, L, A, B].forEach(function (el) { el.addEventListener('input', run); el.addEventListener('change', run); });
  W.addEventListener('input', function () { A.value = ''; });
  L.addEventListener('input', function () { A.value = ''; });
  A.addEventListener('input', function () { W.value = ''; L.value = ''; });
})();
