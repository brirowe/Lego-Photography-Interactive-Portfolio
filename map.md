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
<link rel="stylesheet" href="https://unpkg.com/leaflet-gesture-handling@1.2.2/dist/leaflet-gesture-handling.min.css" />
<script src="https://unpkg.com/leaflet-gesture-handling@1.2.2/dist/leaflet-gesture-handling.min.js"></script>

<h1>Explore the Minifig Adventures</h1>
<p class="archive-intro">An interactive map of every place I've taken photos on my hiking and outdoor adventures. Filter by theme, background, country, state, or elevation, and click any photo to view it larger.</p>

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

  // Points east of 60°E (Japan, etc.) are moved one world-width west so they
  // sit just past Hawaii, next to the Americas, instead of across the map.
  function shiftLng(lng) { return lng > 60 ? lng - 360 : lng; }

  // Elevation ranges for the Elevation filter (feet)
  var ELEV_BANDS = [
    [5000, 'Under 5,000 ft'],
    [8000, '5,000 to 8,000 ft'],
    [10000, '8,000 to 10,000 ft'],
    [12000, '10,000 to 12,000 ft'],
    [13000, '12,000 to 13,000 ft'],
    [14000, '13,000 to 14,000 ft'],
    [Infinity, '14,000+ ft']
  ];
  var ELEV_ORDER = ELEV_BANDS.map(function(b) { return b[1]; });
  function elevBand(ft) {
    if (ft === '' || ft == null || isNaN(ft)) return '';
    ft = Number(ft);
    for (var i = 0; i < ELEV_BANDS.length; i++) {
      if (ft < ELEV_BANDS[i][0]) return ELEV_BANDS[i][1];
    }
  }

  var points = archiveData
    .filter(function(p) { return p.latitude && p.longitude; })
    .map(function(p) {
      return {
        filename: p.filename,
        lat: parseFloat(p.latitude),
        lng: shiftLng(parseFloat(p.longitude)),
        theme: p.theme,
        background_type: p.background_type,
        country: p.country,
        state: p.state,
        elevation_band: elevBand(p.elevation_ft)
      };
    });

  var isMobile = window.matchMedia('(max-width: 768px)').matches;

  var map = L.map('map', {
    worldCopyJump: false,
    maxBounds: [[-85, -300], [85, 60]],
    maxBoundsViscosity: 0.8,
    zoomSnap: 0.5,
    gestureHandling: L.Browser.mobile
  });

  var satellite = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, Maxar, Earthstar Geographics, and the GIS User Community',
    maxZoom: 19
  });

  var labels = L.tileLayer('https://services.arcgisonline.com/arcgis/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Labels &copy; Esri',
    maxZoom: 19
  });

  satellite.addTo(map);
  labels.addTo(map);

  L.control.layers(null, {
    'Labels': labels
  }, { position: 'topright', collapsed: true }).addTo(map);


  var filterConfig = [
    { key: 'theme', label: 'Theme' },
    { key: 'background_type', label: 'Background' },
    { key: 'country', label: 'Country' },
    { key: 'state', label: 'State' },
    { key: 'elevation_band', label: 'Elevation', order: ELEV_ORDER }
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

  function uniqueValues(key, order) {
    var vals = new Set();
    points.forEach(function(p) {
      if (!matchesExcluding(p, key)) return;
      if (p[key] && p[key] !== 'None') vals.add(p[key]);
    });
    if (order) {
      return Array.from(vals).sort(function(a, b) { return order.indexOf(a) - order.indexOf(b); });
    }
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
    var values = uniqueValues(cfg.key, cfg.order);

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
        img.src = '/Lego-Photography-Interactive-Portfolio/photos/photos_compressed/' + g.filenames[idx];
        img.width = 200;
        img.style.cursor = 'pointer';
        img.onclick = function() { showLightbox('/Lego-Photography-Interactive-Portfolio/photos/' + g.filenames[idx]); };
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
      marker.bindPopup(buildContent(), {
        className: 'photo-popup',
        maxWidth: 260,
        autoPanPadding: [20, 20]
      });
      clusters.addLayer(marker);
    });

    if (filtered.length) {
      var bounds = L.latLngBounds(filtered.map(function(p) { return [p.lat, p.lng]; }));
      var pad = isMobile ? [20, 20] : [40, 40];
      map.fitBounds(bounds, { padding: pad, maxZoom: 12 });
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