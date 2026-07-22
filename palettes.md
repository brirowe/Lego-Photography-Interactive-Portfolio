---
layout: default
title: Color Palettes
permalink: /palettes/
---
# Color Palettes
<div class="palette-grid">
{% for row in site.data.palettes %}
  <div class="palette-card">
    <img src="{{ site.baseurl }}/photos/photos_compressed/{{ row.filename }}" alt="{{ row.filename }}" loading="lazy">
    <div class="swatches">
      {% assign colors = row.palette | split: ", " %}
      {% for hex in colors %}
        <div class="swatch" style="background-color: {{ hex }};" title="{{ hex }}"></div>
      {% endfor %}
    </div>
  </div>
{% endfor %}
</div>
