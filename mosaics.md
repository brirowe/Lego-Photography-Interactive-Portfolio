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

<div class="mosaic-grid">
{% for mosaic in site.data.mosaics %}
  <div class="mosaic-card">
    {% if mosaic.name != "" %}<h3 class="mosaic-name">{{ mosaic.name }}</h3>{% endif %}
    <img src="{{ site.baseurl }}/photos/mosaics/{{ mosaic.filename }}" alt="{{ mosaic.name }}" loading="lazy" onclick="showLightbox(this.src)">
    {% if mosaic.instagram_link != "" %}
      <a class="mosaic-link" href="{{ mosaic.instagram_link }}" target="_blank" rel="noopener">Click to see me building this! 🧱</a>
    {% endif %}
    {% if mosaic.tiktok_link != "" %}
      <a class="mosaic-link" href="{{ mosaic.tiktok_link }}" target="_blank" rel="noopener">Watch me build this on TikTok</a>
    {% endif %}
  </div>
{% endfor %}
</div>

<script>
  function showLightbox(src) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox-overlay').style.display = 'flex';
  }
</script>
