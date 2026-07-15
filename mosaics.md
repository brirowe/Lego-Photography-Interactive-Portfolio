---
layout: default
title: Mosaics
permalink: /mosaics/
---

# Mosaics
LEGO mosaics, layered brick art, and other projects.

<div id="lightbox-overlay" onclick="this.style.display='none'">
  <img id="lightbox-img" src="">
</div>

<ul class="gallery">
{% assign mosaic_photos = site.static_files | where_exp: "file", "file.path contains '/photos/mosaics/'" | sort: "name" %}
{% for photo in mosaic_photos %}
  <li style="background-image: url('{{ site.baseurl }}{{ photo.path }}');">
    <a href="#" onclick="showLightbox('{{ site.baseurl }}{{ photo.path }}'); return false;"></a>
  </li>
{% endfor %}
</ul>

<script>
  function showLightbox(src) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox-overlay').style.display = 'flex';
  }
</script>
