---
layout: default
title: Color Palettes
permalink: /palettes/
---
# Color Palettes

<p class="archive-intro">Color palettes pulled from each minifig photo. Pick a style to see the colors arranged in different ways, use "View as" to see how they look with different types of color blindness, and click any color to copy its hex code.</p>

<div class="palette-controls">
<div class="filter-pills" id="style-pills">
  <button type="button" class="filter-pill active" data-style="palette">All</button>
  <button type="button" class="filter-pill" data-style="sequential">Sequential</button>
  <button type="button" class="filter-pill" data-style="converging">Converging</button>
  <button type="button" class="filter-pill" data-style="diverging">Diverging</button>
  <button type="button" class="filter-pill" data-style="cool_warm">Cool to warm</button>
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
       data-filename="{{ row.filename }}"
       data-palette="{{ row.palette }}"
       data-sequential="{{ row.sequential }}"
       data-converging="{{ row.converging }}"
       data-diverging="{{ row.diverging }}"
       data-cool_warm="{{ row.cool_warm }}"
       data-categorical="{{ row.categorical }}">
    <img src="{{ site.baseurl }}/photos/photos_compressed/{{ row.filename }}" alt="{{ row.filename }}" loading="lazy">
    <div class="swatches"></div>
    <button type="button" class="copy-all">Copy all</button>
  </div>
{% endfor %}
</div>

<div class="copy-toast" id="copy-toast">Copied!</div>

{% include photo-lightbox.html page="palettes" %}

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

  // ---- styles ----
  var GRADIENTS = { sequential: true, converging: true, diverging: true, cool_warm: true };
  var NOTES = {
    palette: 'The standout colors from each photo, each one next to its closest match.',
    sequential: 'Dark to light through the photo\'s main color. Good for data that goes low to high.',
    converging: 'Cool and warm at the ends, meeting at the photo\'s darkest shade in the middle.',
    diverging: 'Cool and warm at the ends, meeting at the photo\'s lightest shade in the middle.',
    cool_warm: 'The photo\'s boldest cool color blending around the color wheel to its boldest warm color.',
    categorical: 'A few colors picked to be as different from each other as possible.'
  };

  var grid = document.querySelector('.palette-grid');
  var cards = grid.querySelectorAll('.palette-card');
  var note = document.getElementById('style-note');
  var select = document.getElementById('cvd-select');
  var pills = document.querySelectorAll('#style-pills .filter-pill');
  var style = 'palette';
  var view = 'normal';

  function stopButton(hex, cls) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = cls;
    b.setAttribute('data-hex', hex);
    b.title = 'Click to copy ' + hex;
    var label = document.createElement('span');
    label.className = 'swatch-label';
    label.textContent = hex;
    b.appendChild(label);
    return b;
  }

  function render() {
    var shown = 0;
    cards.forEach(function (card) {
      var raw = (card.getAttribute('data-' + style) || '').trim();
      if (!raw) {
        card.hidden = true;
        return;
      }
      card.hidden = false;
      shown++;

      var hexes = raw.split(',').map(function (h) { return h.trim(); });
      var seen = hexes.map(function (h) { return simulate(h, view); });
      card.setAttribute('data-current', hexes.join(', '));

      var box = card.querySelector('.swatches');
      box.innerHTML = '';

      if (GRADIENTS[style]) {
        // one smooth bar, with a click zone over each color stop
        box.className = 'swatches gradient-bar';
        box.style.background = 'linear-gradient(to right, ' + seen.join(', ') + ')';
        var step = 100 / (hexes.length - 1);
        hexes.forEach(function (hex, i) {
          var pos = i * step;                              // where this color sits on the bar
          var left = Math.max(0, pos - step / 2);
          var right = Math.min(100, pos + step / 2);
          var b = stopButton(hex, 'grad-stop');
          b.style.left = left + '%';
          b.style.width = (right - left) + '%';
          b.style.setProperty('--tick', ((pos - left) / (right - left) * 100) + '%');
          box.appendChild(b);
        });
      } else {
        box.className = 'swatches';
        box.style.background = '';
        hexes.forEach(function (hex, i) {
          var b = stopButton(hex, 'swatch');
          b.style.backgroundColor = seen[i];
          box.appendChild(b);
        });
      }

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

  // ---- copying ----
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

  function showToast(msg) {
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toast.classList.remove('show'); }, 1200);
  }

  grid.addEventListener('click', function (e) {
    var photo = e.target.closest('.palette-card img');
    if (photo) {
      openPhoto(photo.closest('.palette-card').getAttribute('data-filename'));
      return;
    }
    var all = e.target.closest('.copy-all');
    if (all) {
      var list = all.closest('.palette-card').getAttribute('data-current');
      copyText(list).then(function () { showToast('Copied all ' + list.split(',').length + ' colors'); });
      return;
    }
    var stop = e.target.closest('.swatch, .grad-stop');
    if (!stop) return;
    var hex = stop.getAttribute('data-hex');
    copyText(hex).then(function () {
      stop.classList.add('copied');
      showToast('Copied ' + hex);
      setTimeout(function () { stop.classList.remove('copied'); }, 600);
    });
  });

  render();

  // Arrived from another page: scroll to that photo's palette
  if (linkedPhoto) {
    var target = Array.prototype.find.call(cards, function (c) {
      return c.getAttribute('data-filename') === linkedPhoto;
    });
    if (target) {
      showLinked(target);
    }
  }
});
</script>