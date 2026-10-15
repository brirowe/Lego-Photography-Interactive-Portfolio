---
layout: default
title: Mosaics
permalink: /mosaics/
---

# Mosaics

<div id="lightbox-overlay" onclick="this.style.display='none'">
  <img id="lightbox-img" src="">
</div>

<div class="mosaic-grid">
{% for mosaic in site.data.mosaics %}
  <div class="mosaic-card">
    {% if mosaic.name %}<h3 class="mosaic-name">{{ mosaic.name }}</h3>{% endif %}
    <img src="{{ site.baseurl }}/photos/mosaics/thumbs/{{ mosaic.file }}" alt="{{ mosaic.name }}" loading="lazy" onclick="showLightbox('{{ site.baseurl }}/photos/mosaics/{{ mosaic.file }}')">
    {% if mosaic.instagram_link or mosaic.tiktok_link %}
      <div class="mosaic-links">
        {% if mosaic.instagram_link %}<a class="mosaic-link" href="{{ mosaic.instagram_link }}" target="_blank" rel="noopener">Instagram</a>{% endif %}
        {% if mosaic.tiktok_link %}<a class="mosaic-link" href="{{ mosaic.tiktok_link }}" target="_blank" rel="noopener">TikTok</a>{% endif %}
      </div>
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