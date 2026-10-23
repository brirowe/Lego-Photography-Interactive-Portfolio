---
layout: default
title: Color Palettes
permalink: /palettes/
---
# Color Palettes

<p class="archive-intro">Color palettes pulled from each minifig photo. Use the filters to narrow down the photos, pick one or more styles to see the colors arranged in different ways, use "View as" to see how they look with different types of color blindness, and click any color to copy its hex code.</p>

<div class="archive-filter-bar" id="palette-filter-bar"></div>
<div class="archive-filter-panel" id="palette-filter-panel"></div>
<div class="archive-active-chips" id="palette-active-chips"></div>

<div class="palette-controls">
<div class="filter-pills" id="style-pills">
  <button type="button" class="filter-pill active" data-style="palette">Standout</button>
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

<div class="style-note" id="style-note"></div>

<div class="cvd-filters" aria-hidden="true">
<svg width="0" height="0" focusable="false">
  <filter id="cvd-deutan"><feColorMatrix type="matrix" values="0.367322 0.860646 -0.227968 0 0  0.280085 0.672501 0.047413 0 0  -0.011820 0.042940 0.968881 0 0  0 0 0 1 0"/></filter>
  <filter id="cvd-protan"><feColorMatrix type="matrix" values="0.152286 1.052583 -0.204868 0 0  0.114503 0.786281 0.099216 0 0  -0.003882 -0.048116 1.051998 0 0  0 0 0 1 0"/></filter>
  <filter id="cvd-tritan"><feColorMatrix type="matrix" values="1.255528 -0.076749 -0.178779 0 0  -0.078411 0.930809 0.147602 0 0  0.004733 0.691367 0.303900 0 0  0 0 0 1 0"/></filter>
  <filter id="cvd-gray"><feColorMatrix type="matrix" values="0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0.2126 0.7152 0.0722 0 0  0 0 0 1 0"/></filter>
</svg>
</div>

<div class="palette-grid"></div>

<div class="copy-toast" id="copy-toast">Copied!</div>

{% include photo-lightbox.html page="palettes" %}

<script>
document.addEventListener('DOMContentLoaded', function () {

  var baseurl = "{{ site.baseurl }}";
  var PALETTES = {};
  {{ site.data.palettes | jsonify }}.forEach(function (row) { PALETTES[row.filename] = row; });

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
  var STYLE_ORDER = ['palette', 'sequential', 'converging', 'diverging', 'cool_warm', 'categorical'];
  var LABELS = {
    palette: 'Standout',
    sequential: 'Sequential',
    converging: 'Converging',
    diverging: 'Diverging',
    cool_warm: 'Cool to warm',
    categorical: 'Categorical'
  };
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
  var note = document.getElementById('style-note');
  var select = document.getElementById('cvd-select');
  var pills = document.querySelectorAll('#style-pills .filter-pill');
  var styles = ['palette'];   // styles currently turned on, can be more than one
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

  // One palette bar plus its label / Copy all line
  function buildRow(raw, style, showLabel) {
    var hexes = raw.split(',').map(function (h) { return h.trim(); });
    var seen = hexes.map(function (h) { return simulate(h, view); });

    var row = document.createElement('div');
    row.className = 'palette-row';
    row.setAttribute('data-current', hexes.join(', '));

    var box = document.createElement('div');
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
      hexes.forEach(function (hex, i) {
        var b = stopButton(hex, 'swatch');
        b.style.backgroundColor = seen[i];
        box.appendChild(b);
      });
    }
    row.appendChild(box);

    var foot = document.createElement('div');
    foot.className = 'palette-row-foot';
    var label = document.createElement('span');
    label.className = 'palette-row-label';
    label.textContent = showLabel ? LABELS[style] : '';
    foot.appendChild(label);
    var copy = document.createElement('button');
    copy.type = 'button';
    copy.className = 'copy-all';
    copy.textContent = 'Copy all';
    foot.appendChild(copy);
    row.appendChild(foot);

    return row;
  }

  // ---- photo filters (theme, background, etc.) ----
  var filterConfig = [
    { key: 'theme', label: 'Theme' },
    { key: 'subtheme', label: 'Subtheme' },
    { key: 'background_type', label: 'Background' },
    { key: 'season', label: 'Season' },
    { key: 'country', label: 'Country' },
    { key: 'state', label: 'State' }
  ];

  // only photos that have a palette, each filter value as a list so a photo
  // with two figs (like "Star Wars, Agents") shows up under both
  var photos = PHOTO_DATA.filter(function (p) { return PALETTES[p.filename]; });
  photos.forEach(function (p) {
    p.tok = {};
    filterConfig.forEach(function (cfg) { p.tok[cfg.key] = photoTokens(p[cfg.key]); });
  });

  var selected = {};
  filterConfig.forEach(function (c) { selected[c.key] = new Set(); });
  var openCategory = null;

  function matchesExcluding(p, excludeKey) {
    return filterConfig.every(function (cfg) {
      if (cfg.key === excludeKey) return true;
      var chosen = selected[cfg.key];
      return chosen.size === 0 || p.tok[cfg.key].some(function (t) { return chosen.has(t); });
    });
  }

  function uniqueValues(key) {
    var vals = new Set();
    photos.forEach(function (p) {
      if (!matchesExcluding(p, key)) return;
      p.tok[key].forEach(function (t) { vals.add(t); });
    });
    return Array.from(vals).sort(function (a, b) { return a.localeCompare(b); });
  }

  function refreshFilters() {
    renderFilterBar();
    renderFilterPanel();
    renderActiveChips();
    render();
  }

  function renderFilterBar() {
    var bar = document.getElementById('palette-filter-bar');
    bar.innerHTML = '';
    filterConfig.forEach(function (cfg) {
      var count = selected[cfg.key].size;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'filter-toggle' + (openCategory === cfg.key ? ' open' : '') + (count ? ' has-selection' : '');
      btn.innerHTML = cfg.label + (count ? ' <span class="filter-toggle-count">' + count + '</span>' : '') + ' <span class="filter-toggle-arrow">▾</span>';
      btn.addEventListener('click', function () {
        openCategory = openCategory === cfg.key ? null : cfg.key;
        renderFilterBar();
        renderFilterPanel();
      });
      bar.appendChild(btn);
    });
  }

  function renderFilterPanel() {
    var panel = document.getElementById('palette-filter-panel');
    panel.innerHTML = '';
    if (!openCategory) {
      panel.classList.remove('visible');
      return;
    }
    panel.classList.add('visible');

    var cfg = filterConfig.find(function (c) { return c.key === openCategory; });
    var pillWrap = document.createElement('div');
    pillWrap.className = 'filter-pills';

    uniqueValues(cfg.key).forEach(function (val) {
      var pill = document.createElement('button');
      pill.type = 'button';
      pill.className = 'filter-pill' + (selected[cfg.key].has(val) ? ' active' : '');
      pill.textContent = val;
      pill.addEventListener('click', function () {
        if (selected[cfg.key].has(val)) {
          selected[cfg.key].delete(val);
        } else {
          selected[cfg.key].add(val);
        }
        renderFilterBar();
        renderActiveChips();
        render();
        pill.classList.toggle('active');
      });
      pillWrap.appendChild(pill);
    });

    panel.appendChild(pillWrap);
  }

  function renderActiveChips() {
    var container = document.getElementById('palette-active-chips');
    container.innerHTML = '';

    var any = false;
    filterConfig.forEach(function (cfg) {
      selected[cfg.key].forEach(function (val) {
        any = true;
        var chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'active-chip';
        chip.innerHTML = '<span class="active-chip-label">' + cfg.label + ':</span> ' + val + ' <span class="active-chip-remove">&times;</span>';
        chip.addEventListener('click', function () {
          selected[cfg.key].delete(val);
          refreshFilters();
        });
        container.appendChild(chip);
      });
    });

    if (any) {
      var clearAll = document.createElement('button');
      clearAll.type = 'button';
      clearAll.className = 'clear-all-chip';
      clearAll.textContent = 'Clear all';
      clearAll.addEventListener('click', function () {
        filterConfig.forEach(function (c) { selected[c.key].clear(); });
        refreshFilters();
      });
      container.appendChild(clearAll);
    }
  }

  // ---- cards: one per shot, dots flip between near-duplicate versions ----
  var cards = [];   // the cards currently on the page

  function cvd() { return view === 'normal' ? '' : 'url(#cvd-' + view + ')'; }

  // redraw one card for its current version
  function drawCard(card) {
    var f = card._files[card._idx];
    var img = card.querySelector('img');
    img.src = baseurl + '/photos/photos_compressed/' + f;
    img.alt = f;
    img.style.filter = cvd();

    card.querySelectorAll('.version-dot').forEach(function (d, i) {
      d.classList.toggle('active', i === card._idx);
    });

    var rows = card.querySelector('.palette-rows');
    rows.innerHTML = '';
    styles.forEach(function (s) {
      var raw = (PALETTES[f][s] || '').trim();
      if (raw) rows.appendChild(buildRow(raw, s, styles.length > 1));
    });
  }

  function makeCard(files) {
    var card = document.createElement('div');
    card.className = 'palette-card';
    card._files = files;
    card._idx = 0;

    var img = document.createElement('img');
    img.loading = 'lazy';
    card.appendChild(img);

    if (files.length > 1) {
      var dots = document.createElement('div');
      dots.className = 'version-dots';
      files.forEach(function (f, i) {
        var d = document.createElement('button');
        d.type = 'button';
        d.className = 'version-dot';
        d.setAttribute('aria-label', 'Version ' + (i + 1));
        d.addEventListener('click', function () {
          card._idx = i;
          drawCard(card);
        });
        dots.appendChild(d);
      });
      card.appendChild(dots);
    }

    var rows = document.createElement('div');
    rows.className = 'palette-rows';
    card.appendChild(rows);
    return card;
  }

  // ---- draw the grid ----
  function render() {
    var multi = styles.length > 1;

    // one card per shot, mixed by theme
    var groups = mixOrder(groupPhotos(photos.filter(function (p) { return matchesExcluding(p, null); })));
    var keep = {};
    cards.forEach(function (c) { keep[c._files.join('|')] = c; });

    grid.innerHTML = '';
    cards = groups.map(function (g) {
      var files = g.map(function (p) { return p.filename; });
      var card = keep[files.join('|')] || makeCard(files);
      drawCard(card);
      grid.appendChild(card);
      return card;
    });
    var shown = cards.length;

    note.innerHTML = '';
    styles.forEach(function (s) {
      var line = document.createElement('p');
      if (multi) {
        var b = document.createElement('strong');
        b.textContent = LABELS[s] + ': ';
        line.appendChild(b);
      }
      line.appendChild(document.createTextNode(NOTES[s]));
      note.appendChild(line);
    });
    var count = document.createElement('p');
    count.className = 'palette-count';
    count.textContent = shown + (shown === 1 ? ' photo' : ' photos');
    note.appendChild(count);
  }

  pills.forEach(function (pill) {
    pill.addEventListener('click', function () {
      var s = pill.getAttribute('data-style');
      var on = styles.indexOf(s) !== -1;
      if (on && styles.length === 1) return;   // always keep at least one style on
      if (on) {
        styles = styles.filter(function (x) { return x !== s; });
      } else {
        styles.push(s);
      }
      styles.sort(function (a, b) { return STYLE_ORDER.indexOf(a) - STYLE_ORDER.indexOf(b); });
      pill.classList.toggle('active', !on);
      render();
    });
  });

  select.addEventListener('change', function () {
    view = select.value;
    render();
  });

  // ---- popup: every palette for the clicked photo ----
  var popupImg = document.getElementById('photo-lightbox-img');
  window.onPhotoOpen = function (filename, extra) {
    popupImg.style.filter = cvd();
    var row = PALETTES[filename];
    if (!row) return;
    var wrap = document.createElement('div');
    wrap.className = 'palette-rows palette-rows-compact';
    STYLE_ORDER.forEach(function (s) {
      var raw = (row[s] || '').trim();
      if (raw) wrap.appendChild(buildRow(raw, s, true));
    });
    extra.appendChild(wrap);
  };

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

  // handles Copy all and single colors, on the cards and in the popup
  function handleCopy(e) {
    var all = e.target.closest('.copy-all');
    if (all) {
      var list = all.closest('.palette-row').getAttribute('data-current');
      copyText(list).then(function () { showToast('Copied all ' + list.split(',').length + ' colors'); });
      return true;
    }
    var stop = e.target.closest('.swatch, .grad-stop');
    if (!stop) return false;
    var hex = stop.getAttribute('data-hex');
    copyText(hex).then(function () {
      stop.classList.add('copied');
      showToast('Copied ' + hex);
      setTimeout(function () { stop.classList.remove('copied'); }, 600);
    });
    return true;
  }

  grid.addEventListener('click', function (e) {
    var photo = e.target.closest('.palette-card img');
    if (photo) {
      var card = photo.closest('.palette-card');
      openPhoto(card._files[card._idx], card._files);
      return;
    }
    handleCopy(e);
  });

  document.getElementById('photo-lightbox-extra').addEventListener('click', handleCopy);

  renderFilterBar();
  renderFilterPanel();
  renderActiveChips();
  render();

  // Arrived from another page: scroll to that photo's card, on that version, and open it
  if (linkedPhoto) {
    var target = cards.find(function (c) { return c._files.indexOf(linkedPhoto) !== -1; });
    if (target) {
      target._idx = target._files.indexOf(linkedPhoto);
      drawCard(target);
      showLinked(target);
      openPhoto(linkedPhoto, target._files);
    } else {
      openPhoto(linkedPhoto);
    }
  }
});
</script>