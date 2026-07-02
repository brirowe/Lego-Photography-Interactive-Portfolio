---
layout: default
title: Map
---

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.js"></script>

<div id="map" style="width: 100%; height: 500px;"></div>

<script>
  var map = L.map('map').setView([39.5, -105.5], 8);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  var points = [
    {number: "331", lat: 39.674577, lng: -105.662019},
    {number: "182", lat: 39.757872, lng: -105.857065},
    {number: "225", lat: 38.760149, lng: -109.325886}
  ];

  points.forEach(function(p) {
    L.marker([p.lat, p.lng]).addTo(map).bindPopup(p.number);
  });
</script>
