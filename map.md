---
layout: default
title: Map
text_width: false
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>

<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.css" />
<link rel="stylesheet" href="https://unpkg.com/leaflet.markercluster@1.5.3/dist/MarkerCluster.Default.css" />
<script src="https://unpkg.com/leaflet.markercluster@1.5.3/dist/leaflet.markercluster.js"></script>

<h1>Explore the Minifig Adventures</h1>
<p class="archive-intro">An interactive map of every place I've taken photos on my hiking and outdoor adventures. Filter by theme or background type, and click any photo to view it larger.</p>

<div class="archive-filter-bar" id="map-filter-bar"></div>
<div class="archive-filter-panel" id="map-filter-panel"></div>
<div class="archive-active-chips" id="map-active-chips"></div>

<div id="map"></div>

<div id="lightbox-overlay" onclick="this.style.display='none'">
  <img id="lightbox-img" src="">
</div>

<script>
  function showLightbox(src) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox-overlay').style.display = 'flex';
  }

  const archiveData = {{ site.data.minifig_archive | jsonify }};

  var points = archiveData
    .filter(function(p) { return p.latitude && p.longitude; })
    .map(function(p) {
      return {
        filename: p.filename,
        lat: parseFloat(p.latitude),
        lng: parseFloat(p.longitude),
        theme: p.theme,
        background_type: p.background_type
      };
    });

  var map = L.map('map', { worldCopyJump: false, maxBounds: [[-85, -230], [85, 190]], maxBoundsViscosity: 0.8 });

  var satellite = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community',
    maxZoom: 19
  });

  var labels = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}@2x.png', {
    attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
    subdomains: 'abcd',
    maxZoom: 20,
    className: 'thin-labels'
  });

  satellite.addTo(map);
  labels.addTo(map);

  L.control.layers(null, {
    'Labels': labels
  }, { position: 'topright' }).addTo(map);


  var filterConfig = [
    { key: 'theme', label: 'Theme' },
    { key: 'background_type', label: 'Background' }
  ];

  var selected = {};
  filterConfig.forEach(function(c) { selected[c.key] = new Set(); });

  var openCategory = null;

  function matchesExcluding(point, excludeKey) {
    return filterConfig.every(function(cfg) {
      if (cfg.key === excludeKey) return true;
      var chosen = selected[cfg.key];
      if (chosen.size === 0) return true;
      return chosen.has(point[cfg.key]);
    });
  }

  function uniqueValues(key) {
    var vals = new Set();
    points.forEach(function(p) {
      if (!matchesExcluding(p, key)) return;
      if (p[key] && p[key] !== 'None') vals.add(p[key]);
    });
    return Array.from(vals).sort(function(a, b) { return a.localeCompare(b); });
  }

  function pointMatches(p) {
    return filterConfig.every(function(cfg) {
      var chosen = selected[cfg.key];
      if (chosen.size === 0) return true;
      return chosen.has(p[cfg.key]);
    });
  }

  function renderFilterBar() {
    var bar = document.getElementById('map-filter-bar');
    bar.innerHTML = '';
    filterConfig.forEach(function(cfg) {
      var count = selected[cfg.key].size;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'filter-toggle' + (openCategory === cfg.key ? ' open' : '') + (count ? ' has-selection' : '');
      btn.innerHTML = cfg.label + (count ? ' <span class="filter-toggle-count">' + count + '</span>' : '') + ' <span class="filter-toggle-arrow">▾</span>';
      btn.addEventListener('click', function() {
        openCategory = openCategory === cfg.key ? null : cfg.key;
        renderFilterBar();
        renderFilterPanel();
      });
      bar.appendChild(btn);
    });
  }

  function renderFilterPanel() {
    var panel = document.getElementById('map-filter-panel');
    panel.innerHTML = '';
    if (!openCategory) {
      panel.classList.remove('visible');
      return;
    }
    panel.classList.add('visible');

    var cfg = filterConfig.find(function(c) { return c.key === openCategory; });
    var values = uniqueValues(cfg.key);

    var pillWrap = document.createElement('div');
    pillWrap.className = 'filter-pills';

    values.forEach(function(val) {
      var pill = document.createElement('button');
      pill.type = 'button';
      pill.className = 'filter-pill';
      if (selected[cfg.key].has(val)) pill.classList.add('active');
      pill.textContent = val;
      pill.addEventListener('click', function() {
        if (selected[cfg.key].has(val)) {
          selected[cfg.key].delete(val);
        } else {
          selected[cfg.key].add(val);
        }
        renderFilterBar();
        renderActiveChips();
        renderMarkers();
        pill.classList.toggle('active');
      });
      pillWrap.appendChild(pill);
    });

    panel.appendChild(pillWrap);
  }

  function renderActiveChips() {
    var container = document.getElementById('map-active-chips');
    container.innerHTML = '';

    var any = false;
    filterConfig.forEach(function(cfg) {
      selected[cfg.key].forEach(function(val) {
        any = true;
        var chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'active-chip';
        chip.innerHTML = '<span class="active-chip-label">' + cfg.label + ':</span> ' + val + ' <span class="active-chip-remove">&times;</span>';
        chip.addEventListener('click', function() {
          selected[cfg.key].delete(val);
          renderFilterBar();
          renderFilterPanel();
          renderActiveChips();
          renderMarkers();
        });
        container.appendChild(chip);
      });
    });

    if (any) {
      var clearAll = document.createElement('button');
      clearAll.type = 'button';
      clearAll.className = 'clear-all-chip';
      clearAll.textContent = 'Clear all';
      clearAll.addEventListener('click', function() {
        filterConfig.forEach(function(c) { selected[c.key].clear(); });
        renderFilterBar();
        renderFilterPanel();
        renderActiveChips();
        renderMarkers();
      });
      container.appendChild(clearAll);
    }
  }

  // Group points that share the same coordinates
  function groupPoints(pts) {
    var groups = {};
    pts.forEach(function(p) {
      var key = p.lat.toFixed(6) + ',' + p.lng.toFixed(6);
      if (!groups[key]) {
        groups[key] = { lat: p.lat, lng: p.lng, filenames: [] };
      }
      groups[key].filenames.push(p.filename);
    });
    return Object.values(groups);
  }

  var clusters = L.markerClusterGroup({
    iconCreateFunction: function(cluster) {
      var count = 0;
      cluster.getAllChildMarkers().forEach(function(marker) {
        count += marker.photoCount || 1;
      });

      var size = count < 10 ? 'small' : count < 50 ? 'medium' : 'large';

      return L.divIcon({
        html: '<div><span>' + count + '</span></div>',
        className: 'marker-cluster marker-cluster-' + size,
        iconSize: L.point(40, 40)
      });
    }
  });

  map.addLayer(clusters);
  var firstRender = true;

  function renderMarkers() {
    clusters.clearLayers();

    var filtered = points.filter(pointMatches);
    var groups = groupPoints(filtered);

    groups.forEach(function(g) {
      var idx = 0;
      var marker = L.marker([g.lat, g.lng]);
      marker.photoCount = g.filenames.length;

      function buildContent() {
        var container = document.createElement('div');
        container.className = 'carousel-popup';
        var img = document.createElement('img');
        img.src = '/Lego-Photography-Interactive-Portfolio/photos/' + g.filenames[idx];
        img.width = 150;
        img.style.cursor = 'pointer';
        img.onclick = function() { showLightbox(img.src); };
        container.appendChild(img);
        if (g.filenames.length > 1) {
          var controls = document.createElement('div');
          controls.className = 'carousel-controls';
          var prevBtn = document.createElement('button');
          prevBtn.type = 'button';
          prevBtn.innerHTML = '&#8249;';
          prevBtn.onclick = function(e) {
            e.stopPropagation();
            idx = (idx - 1 + g.filenames.length) % g.filenames.length;
            marker.setPopupContent(buildContent());
          };
          var counter = document.createElement('span');
          counter.textContent = (idx + 1) + ' / ' + g.filenames.length;
          var nextBtn = document.createElement('button');
          nextBtn.type = 'button';
          nextBtn.innerHTML = '&#8250;';
          nextBtn.onclick = function(e) {
            e.stopPropagation();
            idx = (idx + 1) % g.filenames.length;
            marker.setPopupContent(buildContent());
          };
          controls.appendChild(prevBtn);
          controls.appendChild(counter);
          controls.appendChild(nextBtn);
          container.appendChild(controls);
        }
        return container;
      }
      marker.bindPopup(buildContent(), { className: 'photo-popup' });
      clusters.addLayer(marker);
    });

    if (filtered.length) {
      var primaryPoints = filtered.filter(function(p) { return p.lng < -50; });
      var basisPoints = primaryPoints.length ? primaryPoints : filtered;
      var bounds = L.latLngBounds(basisPoints.map(function(p) { return [p.lat, p.lng]; }));
      map.fitBounds(bounds, { padding: [30, 30], maxZoom: 12 });
    }
  }

  renderFilterBar();
  renderFilterPanel();
  renderActiveChips();
  renderMarkers();

  window.addEventListener('load', function() {
    map.invalidateSize();
    renderMarkers();
  });

  var resizeTimer;
  window.addEventListener('resize', function() {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function() {
      map.invalidateSize();
    }, 150);
  });
</script>
