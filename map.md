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

<h1>Map</h1>
<p class="archive-intro">An interactive map of every place I've taken photos on my hiking and outdoor adventures. Filter by theme or background type, and click any photo to view it larger.</p>

<div class="archive-filter-bar" id="map-filter-bar"></div>
<div class="archive-filter-panel" id="map-filter-panel"></div>
<div class="archive-active-chips" id="map-active-chips"></div>

<div id="map" style="width: 100%; height: clamp(500px, 75vh, 900px);"></div>

<div id="lightbox-overlay" onclick="this.style.display='none'">
  <img id="lightbox-img" src="">
</div>

<script>
  function showLightbox(src) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox-overlay').style.display = 'flex';
  }

  const archiveData = {{ site.data.minifig_archive | jsonify }};
  const photoInfo = {};
  archiveData.forEach(function(p) {
    photoInfo[p.filename] = p;
  });

  var map = L.map('map');

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

  var points = [
      {number: "331", lat: 39.674577, lng: -105.662019},
      {number: "182", lat: 39.757872, lng: -105.857065},
      {number: "225", lat: 38.760149, lng: -109.325886},
      {number: "112", lat: 39.672781, lng: -105.206241},
      {number: "19", lat: 38.760149, lng: -109.325886},
      {number: "14", lat: 39.584661, lng: -105.775954},
      {number: "168", lat: 39.584661, lng: -105.775954},
      {number: "176", lat: 39.227158, lng: -105.297391},
      {number: "223", lat: 37.760209, lng: -105.499472},
      {number: "285", lat: 37.760209, lng: -105.499472},
      {number: "265", lat: 39.500297, lng: -105.37962},
      {number: "38", lat: 21.096942, lng: -86.765627},
      {number: "263", lat: 21.096942, lng: -86.765627},
      {number: "47", lat: 39.672659, lng: -105.66326},
      {number: "103", lat: 37.452534, lng: -105.35921},
      {number: "236", lat: 38.697751, lng: -109.20775},
      {number: "209", lat: 39.627614, lng: -105.213614},
      {number: "106", lat: 37.757588, lng: -105.511251},
      {number: "298", lat: 37.757588, lng: -105.511251},
      {number: "304", lat: 39.663981, lng: -105.87801},
      {number: "171", lat: 39.522921, lng: -105.387381},
      {number: "258", lat: 39.672781, lng: -105.206241},
      {number: "337", lat: 38.739535, lng: -109.512168},
      {number: "293", lat: 39.103682, lng: -106.933602},
      {number: "296", lat: 39.584661, lng: -105.775954},
      {number: "75", lat: 39.590596, lng: -105.729015},
      {number: "333", lat: 38.999856, lng: -105.174529},
      {number: "322", lat: 35.697354, lng: 138.268524},
      {number: "330", lat: 39.073656, lng: -106.325407},
      {number: "66", lat: 39.388417, lng: -105.366301},
      {number: "248", lat: 39.388417, lng: -105.366301},
      {number: "80", lat: 39.635723, lng: -105.240122},
      {number: "251", lat: 39.635723, lng: -105.240122},
      {number: "244", lat: 39.538089, lng: -105.28204},
      {number: "338", lat: 39.538089, lng: -105.28204},
      {number: "165", lat: 39.672781, lng: -105.206241},
      {number: "50", lat: 39.723545, lng: -105.894269},
      {number: "164", lat: 39.657749, lng: -105.277688},
      {number: "72", lat: 39.627824, lng: -104.913191},
      {number: "126", lat: 39.627824, lng: -104.913191},
      {number: "68", lat: 37.746796, lng: -105.515218},
      {number: "120", lat: 37.746501, lng: -105.539546},
      {number: "319", lat: 39.077949, lng: -106.35059},
      {number: "162", lat: 39.179044, lng: -106.492744},
      {number: "143", lat: 39.965486, lng: -105.285283},
      {number: "58", lat: 39.627904, lng: -105.213525},
      {number: "118", lat: 39.627904, lng: -105.213525},
      {number: "271", lat: 39.590426, lng: -105.73626},
      {number: "274", lat: 39.590426, lng: -105.73626},
      {number: "115", lat: 39.657854, lng: -105.278427},
      {number: "90", lat: 39.537536, lng: -105.280657},
      {number: "34", lat: 38.738678, lng: -109.512854},
      {number: "48", lat: 38.738678, lng: -109.512854},
      {number: "222", lat: 40.314114, lng: -105.647935},
      {number: "228", lat: 40.312346, lng: -105.647684},
      {number: "313", lat: 38.688351, lng: -109.533083},
      {number: "89", lat: 39.965486, lng: -105.285283},
      {number: "234", lat: 39.538608, lng: -105.277067},
      {number: "245", lat: 39.538608, lng: -105.277067},
      {number: "180", lat: 39.628666, lng: -105.227332},
      {number: "201", lat: 39.628666, lng: -105.227332},
      {number: "312", lat: 39.383499, lng: -105.367857},
      {number: "138", lat: 39.561808, lng: -105.14631},
      {number: "129", lat: 39.541998, lng: -105.99685},
      {number: "170", lat: 39.541998, lng: -105.99685},
      {number: "5", lat: 39.511432, lng: -105.393149},
      {number: "169", lat: 37.746796, lng: -105.515218},
      {number: "306", lat: 39.663517, lng: -105.88235},
      {number: "91", lat: 39.676589, lng: -105.661018},
      {number: "125", lat: 39.804963, lng: -105.736422},
      {number: "195", lat: 39.542033, lng: -105.27533},
      {number: "206", lat: 39.542033, lng: -105.27533},
      {number: "301", lat: 39.105156, lng: -106.930024},
      {number: "188", lat: 39.654697, lng: -105.276475},
      {number: "267", lat: 39.385189, lng: -104.793488},
      {number: "220", lat: 39.801809, lng: -105.784893},
      {number: "37", lat: 39.723329, lng: -105.894287},
      {number: "302", lat: 39.723329, lng: -105.894287},
      {number: "46", lat: 35.697602, lng: 138.269022},
      {number: "92", lat: 35.674785, lng: 138.238807},
      {number: "276", lat: 39.977735, lng: -105.280831},
      {number: "59", lat: 39.414034, lng: -106.147784},
      {number: "208", lat: 35.697476, lng: 138.268442},
      {number: "294", lat: 39.896498, lng: -105.675725},
      {number: "238", lat: 39.896586, lng: -105.674296},
      {number: "218", lat: 39.521663, lng: -105.388151},
      {number: "252", lat: 39.521663, lng: -105.388151},
      {number: "131", lat: 39.798116, lng: -105.75832},
      {number: "76", lat: 39.733718, lng: -105.828695},
      {number: "122", lat: 39.652354, lng: -105.611369},
      {number: "191", lat: 38.791201, lng: -109.606101},
      {number: "262", lat: 38.791201, lng: -109.606101},
      {number: "282", lat: 37.760209, lng: -105.499472},
      {number: "261", lat: 39.098035, lng: -106.944988},
      {number: "297", lat: 38.872642, lng: -106.993454},
      {number: "121", lat: 39.798116, lng: -105.75832},
      {number: "186", lat: 39.627331, lng: -104.913353},
      {number: "217", lat: 37.452534, lng: -105.35921},
      {number: "241", lat: 39.79097, lng: -105.811973},
      {number: "114", lat: 39.665434, lng: -105.205649},
      {number: "202", lat: 39.631846, lng: -104.848036},
      {number: "288", lat: 37.751224, lng: -105.518578},
      {number: "10", lat: 39.688735, lng: -105.197955},
      {number: "175", lat: 39.682342, lng: -105.451552},
      {number: "116", lat: 39.511529, lng: -105.391295},
      {number: "55", lat: 39.511564, lng: -105.391432},
      {number: "9", lat: 35.697354, lng: 138.268524},
      {number: "33", lat: 39.512193, lng: -105.392201},
      {number: "123", lat: 44.039967, lng: -121.575746},
      {number: "1", lat: 39.509599, lng: -105.385572},
      {number: "257", lat: 39.509401, lng: -105.386663},
      {number: "141", lat: 39.628582, lng: -104.911814},
      {number: "88", lat: 39.57364, lng: -104.871391},
      {number: "17", lat: 38.466921, lng: -109.603787},
      {number: "101", lat: 39.69349, lng: -105.435709},
      {number: "324", lat: 39.687534, lng: -105.451149},
      {number: "62", lat: 39.105156, lng: -106.930024},
      {number: "78", lat: 39.628523, lng: -105.213757},
      {number: "86", lat: 39.637151, lng: -104.87669},
      {number: "156", lat: 37.452092, lng: -105.358244},
      {number: "104", lat: 37.751224, lng: -105.518578},
      {number: "269", lat: 39.516723, lng: -105.390272},
      {number: "196", lat: 21.096772, lng: -86.765755},
      {number: "177", lat: 38.739535, lng: -109.512168},
      {number: "144", lat: 39.583435, lng: -105.774872},
      {number: "275", lat: 39.511529, lng: -105.391295},
      {number: "181", lat: 40.313419, lng: -105.646809},
      {number: "95", lat: 39.538089, lng: -105.28204},
      {number: "260", lat: 39.538089, lng: -105.28204},
      {number: "94", lat: 39.63004, lng: -105.231441},
      {number: "42", lat: 39.496953, lng: -105.386831},
      {number: "57", lat: 39.635328, lng: -105.226877},
      {number: "153", lat: 39.59113, lng: -105.735602},
      {number: "49", lat: 40.311089, lng: -105.653013},
      {number: "219", lat: 40.311089, lng: -105.653013},
      {number: "98", lat: 39.385189, lng: -104.793488},
      {number: "77", lat: 37.760209, lng: -105.499472},
      {number: "198", lat: 37.760209, lng: -105.499472},
      {number: "13", lat: 38.693322, lng: -109.215482},
      {number: "30", lat: 38.693322, lng: -109.215482},
      {number: "132", lat: 38.693322, lng: -109.215482},
      {number: "174", lat: 38.693322, lng: -109.215482},
      {number: "233", lat: 38.693322, lng: -109.215482},
      {number: "247", lat: 38.693322, lng: -109.215482},
      {number: "299", lat: 38.693322, lng: -109.215482},
      {number: "107", lat: 38.697751, lng: -109.20775},
      {number: "22", lat: 39.644152, lng: -105.614301},
      {number: "16", lat: 37.509343, lng: -105.544305},
      {number: "109", lat: 37.746501, lng: -105.539546},
      {number: "300", lat: 37.746501, lng: -105.539546},
      {number: "161", lat: 39.750228, lng: -105.877758},
      {number: "85", lat: 39.627824, lng: -104.913191},
      {number: "216", lat: 37.743604, lng: -105.526628},
      {number: "158", lat: 39.723329, lng: -105.894287},
      {number: "133", lat: 39.512719, lng: -105.393429},
      {number: "84", lat: 40.309198, lng: -105.667155},
      {number: "193", lat: 37.446575, lng: -105.362004},
      {number: "87", lat: 39.521663, lng: -105.388151},
      {number: "314", lat: 38.466921, lng: -109.603787},
      {number: "197", lat: 39.409246, lng: -106.139538},
      {number: "190", lat: 39.417259, lng: -106.151309},
      {number: "105", lat: 39.501231, lng: -105.374732},
      {number: "28", lat: 39.544996, lng: -105.273831},
      {number: "309", lat: 39.537453, lng: -105.277437},
      {number: "295", lat: 21.095778, lng: -86.766429},
      {number: "323", lat: 21.095778, lng: -86.766429},
      {number: "160", lat: 45.216294, lng: -123.97313},
      {number: "96", lat: 21.096818, lng: -86.765704},
      {number: "151", lat: 39.733718, lng: -105.828695},
      {number: "60", lat: 39.50194, lng: -105.375604},
      {number: "29", lat: 39.497781, lng: -105.39049},
      {number: "189", lat: 39.497781, lng: -105.39049},
      {number: "23", lat: 37.751224, lng: -105.518578},
      {number: "253", lat: 39.627614, lng: -105.213614},
      {number: "230", lat: 37.760209, lng: -105.499472},
      {number: "7", lat: 39.496694, lng: -106.136757},
      {number: "213", lat: 39.496694, lng: -106.136757},
      {number: "329", lat: 39.624989, lng: -105.344475},
      {number: "166", lat: 39.755273, lng: -105.857752},
      {number: "51", lat: 39.653443, lng: -105.835134},
      {number: "149", lat: 39.408772, lng: -106.140251},
      {number: "159", lat: 39.672977, lng: -105.66267},
      {number: "81", lat: 39.414034, lng: -106.147784},
      {number: "40", lat: 38.739535, lng: -109.512168},
      {number: "256", lat: 38.739535, lng: -109.512168},
      {number: "155", lat: 39.79097, lng: -105.811973},
      {number: "39", lat: 38.999856, lng: -105.174529},
      {number: "229", lat: 37.751224, lng: -105.518578},
      {number: "128", lat: 38.791201, lng: -109.606101},
      {number: "74", lat: 37.751224, lng: -105.518578},
      {number: "194", lat: 39.835577, lng: -105.791006},
      {number: "214", lat: 40.309988, lng: -105.667334},
      {number: "240", lat: 39.688735, lng: -105.197955},
      {number: "227", lat: 39.390476, lng: -105.366389},
      {number: "110", lat: 39.544996, lng: -105.273831},
      {number: "210", lat: 39.544996, lng: -105.273831},
      {number: "243", lat: 35.697354, lng: 138.268524},
      {number: "204", lat: 39.502001, lng: -105.376463},
      {number: "310", lat: 39.514287, lng: -105.396042},
      {number: "308", lat: 39.227158, lng: -105.297391},
      {number: "142", lat: 39.804963, lng: -105.736422},
      {number: "64", lat: 39.380917, lng: -105.374757},
      {number: "32", lat: 39.532648, lng: -105.688562},
      {number: "93", lat: 40.104929, lng: -105.745636},
      {number: "45", lat: 39.768533, lng: -105.858127},
      {number: "150", lat: 40.101113, lng: -105.738279},
      {number: "137", lat: 39.674577, lng: -105.662019},
      {number: "135", lat: 38.743622, lng: -109.499335},
      {number: "185", lat: 38.922211, lng: -106.97276},
      {number: "192", lat: 39.498592, lng: -105.381139},
      {number: "154", lat: 39.541522, lng: -105.678989},
      {number: "291", lat: 39.659937, lng: -105.822402},
      {number: "277", lat: 39.674577, lng: -105.662019},
      {number: "273", lat: 39.671553, lng: -105.664507},
      {number: "6", lat: 39.541998, lng: -105.99685},
      {number: "24", lat: 39.674577, lng: -105.662019},
      {number: "70", lat: 39.590824, lng: -105.729819},
      {number: "280", lat: 39.631846, lng: -104.848036},
      {number: "335", lat: 39.514116, lng: -105.390402},
      {number: "172", lat: 39.514116, lng: -105.390402},
      {number: "111", lat: 39.63004, lng: -105.231441},
      {number: "44", lat: 40.312982, lng: -105.646676},
      {number: "63", lat: 40.311089, lng: -105.653013},
      {number: "8", lat: 40.309202, lng: -105.659633},
      {number: "43", lat: 40.309202, lng: -105.659633},
      {number: "254", lat: 39.631846, lng: -104.848036},
      {number: "15", lat: 39.631846, lng: -104.848036},
      {number: "327", lat: 39.631846, lng: -104.848036},
      {number: "178", lat: 39.381118, lng: -105.370965},
      {number: "4", lat: 21.096906, lng: -86.765699},
      {number: "102", lat: 21.096934, lng: -86.765965},
      {number: "239", lat: 21.096934, lng: -86.765965},
      {number: "130", lat: 39.075715, lng: -106.335353},
      {number: "203", lat: 21.096772, lng: -86.765755},
      {number: "232", lat: 21.096772, lng: -86.765755},
      {number: "318", lat: 21.096772, lng: -86.765755},
      {number: "127", lat: 21.096772, lng: -86.765755},
      {number: "113", lat: 37.498676, lng: -105.491609},
      {number: "152", lat: 38.737154, lng: -109.517589},
      {number: "231", lat: 38.737154, lng: -109.517589},
      {number: "25", lat: 35.697354, lng: 138.268524},
      {number: "36", lat: 35.723516, lng: 139.769086},
      {number: "163", lat: 39.385189, lng: -104.793488},
      {number: "136", lat: 39.723329, lng: -105.894287},
      {number: "173", lat: 39.66479, lng: -105.888024},
      {number: "99", lat: 40.314114, lng: -105.647935},
      {number: "281", lat: 39.50194, lng: -105.375604},
      {number: "97", lat: 40.309988, lng: -105.667334},
      {number: "183", lat: 37.746796, lng: -105.515218},
      {number: "326", lat: 40.101113, lng: -105.738279},
      {number: "305", lat: 39.65373, lng: -105.83392},
      {number: "147", lat: 39.672977, lng: -105.66267},
      {number: "148", lat: 39.749857, lng: -105.876007},
      {number: "215", lat: 39.678273, lng: -105.44801},
      {number: "221", lat: 39.677664, lng: -105.44724},
      {number: "108", lat: 39.683444, lng: -105.452796},
      {number: "146", lat: 37.498676, lng: -105.491609},
      {number: "2", lat: 39.50194, lng: -105.375604},
      {number: "35", lat: 39.835577, lng: -105.791006},
      {number: "139", lat: 37.452606, lng: -105.358818},
      {number: "140", lat: 37.452606, lng: -105.358818},
      {number: "250", lat: 37.452534, lng: -105.35921},
      {number: "278", lat: 37.452534, lng: -105.35921},
      {number: "52", lat: 39.227673, lng: -105.297588},
      {number: "71", lat: 39.227673, lng: -105.297588},
      {number: "167", lat: 39.417259, lng: -106.151309},
      {number: "200", lat: 39.65375, lng: -105.836275},
      {number: "207", lat: 39.672977, lng: -105.66267},
      {number: "179", lat: 39.408772, lng: -106.139719},
      {number: "79", lat: 39.538089, lng: -105.28204},
      {number: "212", lat: 39.538089, lng: -105.28204}
  ];

  points.forEach(function(p) {
    var info = photoInfo['Pic (' + p.number + ').jpg'];
    p.theme = info ? info.theme : null;
    p.background_type = info ? info.background_type : null;
  });

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
        groups[key] = { lat: p.lat, lng: p.lng, numbers: [] };
      }
      groups[key].numbers.push(p.number);
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
      marker.photoCount = g.numbers.length;

      function buildContent() {
        var container = document.createElement('div');
        container.className = 'carousel-popup';
        var img = document.createElement('img');
        img.src = '/Lego-Photography-Interactive-Portfolio/photos/Pic (' + g.numbers[idx] + ').jpg';
        img.width = 150;
        img.style.cursor = 'pointer';
        img.onclick = function() { showLightbox(img.src); };
        container.appendChild(img);
        if (g.numbers.length > 1) {
          var controls = document.createElement('div');
          controls.className = 'carousel-controls';
          var prevBtn = document.createElement('button');
          prevBtn.type = 'button';
          prevBtn.innerHTML = '&#8249;';
          prevBtn.onclick = function(e) {
            e.stopPropagation();
            idx = (idx - 1 + g.numbers.length) % g.numbers.length;
            marker.setPopupContent(buildContent());
          };
          var counter = document.createElement('span');
          counter.textContent = (idx + 1) + ' / ' + g.numbers.length;
          var nextBtn = document.createElement('button');
          nextBtn.type = 'button';
          nextBtn.innerHTML = '&#8250;';
          nextBtn.onclick = function(e) {
            e.stopPropagation();
            idx = (idx + 1) % g.numbers.length;
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

    if (groups.length) {
      map.fitBounds(clusters.getBounds(), { padding: [30, 30] });
    }
  }

  renderFilterBar();
  renderFilterPanel();
  renderActiveChips();
  renderMarkers();

  window.addEventListener('load', function() {
    map.invalidateSize();
    if (clusters.getLayers().length) {
      map.fitBounds(clusters.getBounds(), { padding: [30, 30] });
    }
  });
</script>
