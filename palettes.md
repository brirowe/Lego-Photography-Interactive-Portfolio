---
layout: default
title: Color Palettes
permalink: /palettes/
---
# Color Palettes

Color palettes pulled from photos of our Lego mountain, wildflower, rock, lake, and trail scenes.

<div class="palette-grid">
{% for row in site.data.palettes %}
  <div class="palette-card">
    <img src="/assets/images/photos_compressed/{{ row.filename }}" alt="{{ row.filename }}">
    <div class="swatches">
      {% assign colors = row.palette | split: ", " %}
      {% for hex in colors %}
        <div class="swatch" style="background-color: {{ hex }};" title="{{ hex }}"></div>
      {% endfor %}
    </div>
  </div>
{% endfor %}
</div>
