---
layout: default
title: Color Palettes
permalink: /palettes/
---
# Color Palettes

<div class="palette-controls">
<div class="filter-pills" id="style-pills">
  <button type="button" class="filter-pill active" data-style="palette">All</button>
  <button type="button" class="filter-pill" data-style="converging">Converging</button>
  <button type="button" class="filter-pill" data-style="diverging">Diverging</button>
  <button type="button" class="filter-pill" data-style="categorical">Categorical</button>
</div>
<div class="cvd-control">
<label for="cvd-select">View as</label>
<select id="cvd-select" class="cvd-select">
  <option value="normal">Normal vision</option>
  <option value="deutan">Deuteranopia (red-green)</option>
  <option value="protan">Protanopia (red-green)</option>
  <option value="tritan">Tritanopia (blue-yellow)</option>
  <option value="gray">Grayscale</option>
</select>
</div>
</div>

<p class="style-note" id="style-note"></p>

<div class="cvd-filters" aria-hidden="true">
<svg width="0" height="0" focusable="false">
  <filter id="cvd-deutan"><feColorMatrix type="matrix" values="0.367322 0.860646 -0.227968 0 0  0.280085 0.672501 0.047413 0 0  -0.011820 0.042940 0.968881 0 0  0 0 0 1 0"/></filter>
  <filter id="cvd-protan"><feColorMatrix type="matrix" values="0.152286 1.052583 -0.204868 0 0  0.114503 0.786281 0.099216 0 0  -0.003882 -0.048116 1.051998 0 0  0 0 0 1 0"/></filter>
  <filter id="cvd-tritan"><feColorMatrix type="matrix" values="1.255528 -0.076749 -0.178779 0 0  -0.078411 0.930809 0.147602 0 0  0.004733 0.691367 0.303900 0 0  0 0 0 1 0"/></filter>
  <filter id="cvd-gray"><feColorMatrix type="matrix" values="0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0 0 0 1 0"/></filter>
</svg>
</div>

<div class="palette-grid">
{% for row in site.data.palettes %}
  <div class="palette-card"
       data-palette="{{ row.palette }}"
       data-converging="{{ row.converging }}"
       data-diverging="{{ row.diverging }}"
       data-categorical="{{ row.categorical }}">
    <img src="{{ site.baseurl }}/photos/photos_compressed/{{ row.filename }}" alt="{{ row.filename }}" loading="lazy">
    <div class="swatches"></div>
  </div>
{% endfor %}
</div>

<div class="copy-toast" id="copy-toast">Copied!</div>

<script>
document.addEventListener('DOMContentLoaded', function () {

  // ---- colorblind simulation ----
  var M = {
    deutan: [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
    protan: [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
    tritan: [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]]
  };

  function toLin(c) { c = c / 255; return c <= 0.04045 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }
  function toSrgb(c) { c = Math.min(1, Math.max(0, c)); return Math.round(255 * (c <= 0.0031308 ? c * 12.92 : 1.055 * Math.pow(c, 1 / 2.4) - 0.055)); }

  function simulate(hex, kind) {
    if (kind === 'normal') return hex;
    var rgb = [1, 3, 5].map(function (i) { return toLin(parseInt(hex.substr(i, 2), 16)); });
    var out;
    if (kind === 'gray') {
      var y = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2];
      out = [y, y, y];
    } else {
      out = M[kind].map(function (r) { return r[0] * rgb[0] + r[1] * rgb[1] + r[2] * rgb[2]; });
    }
    return '#' + out.map(function (v) { return ('0' + toSrgb(v).toString(16)).slice(-2); }).join('');
  }

  // ---- styles + view ----
  var NOTES = {
    palette: 'Every photo. Each color sits next to its closest match, darker end first.',
    converging: 'Muted at both ends, building to the boldest color in the middle.',
    diverging: 'Warm colors on one side, cool on the other, meeting in the middle.',
    categorical: 'A few colors picked to be as different from each other as possible.'
  };

  var grid = document.querySelector('.palette-grid');
  var cards = grid.querySelectorAll('.palette-card');
  var note = document.getElementById('style-note');
  var select = document.getElementById('cvd-select');
  var pills = document.querySelectorAll('#style-pills .filter-pill');
  var style = 'palette';
  var view = 'normal';

  function render() {
    var shown = 0;
    cards.forEach(function (card) {
      var hexes = (card.getAttribute('data-' + style) || '').trim();
      if (!hexes) {
        card.hidden = true;
        return;
      }
      card.hidden = false;
      shown++;

      var box = card.querySelector('.swatches');
      box.innerHTML = '';
      hexes.split(',').forEach(function (raw) {
        var hex = raw.trim();
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'swatch';
        b.setAttribute('data-hex', hex);
        b.title = 'Click to copy ' + hex;
        b.style.backgroundColor = simulate(hex, view);
        var label = document.createElement('span');
        label.className = 'swatch-label';
        label.textContent = hex;
        b.appendChild(label);
        box.appendChild(b);
      });

      card.querySelector('img').style.filter = view === 'normal' ? '' : 'url(#cvd-' + view + ')';
    });
    note.textContent = NOTES[style] + ' (' + shown + (shown === 1 ? ' photo)' : ' photos)');
  }

  pills.forEach(function (pill) {
    pill.addEventListener('click', function () {
      pills.forEach(function (p) { p.classList.remove('active'); });
      pill.classList.add('active');
      style = pill.getAttribute('data-style');
      render();
    });
  });

  select.addEventListener('change', function () {
    view = select.value;
    render();
  });

  // ---- click a swatch to copy ----
  var toast = document.getElementById('copy-toast');
  var toastTimer;

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }
    var textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();
    try {
      document.execCommand('copy');
    } catch (err) {}
    document.body.removeChild(textarea);
    return Promise.resolve();
  }

  grid.addEventListener('click', function (e) {
    var swatch = e.target.closest('.swatch');
    if (!swatch) return;
    var hex = swatch.getAttribute('data-hex');
    copyText(hex).then(function () {
      swatch.classList.add('copied');
      toast.textContent = 'Copied ' + hex;
      toast.classList.add('show');
      clearTimeout(toastTimer);
      toastTimer = setTimeout(function () { toast.classList.remove('show'); }, 1200);
      setTimeout(function () { swatch.classList.remove('copied'); }, 600);
    });
  });

  render();
});
</script>