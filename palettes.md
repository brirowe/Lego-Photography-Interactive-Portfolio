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
        <button type="button" class="swatch" style="background-color: {{ hex }};" data-hex="{{ hex }}" title="Click to copy {{ hex }}">
          <span class="swatch-label">{{ hex }}</span>
        </button>
      {% endfor %}
    </div>
  </div>
{% endfor %}
</div>

<div class="copy-toast" id="copy-toast">Copied!</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
  var toast = document.getElementById('copy-toast');
  var toastTimer;

  document.querySelectorAll('.swatch').forEach(function (swatch) {
    swatch.addEventListener('click', function () {
      var hex = swatch.getAttribute('data-hex');

      var copyText = function (text) {
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
      };

      copyText(hex).then(function () {
        swatch.classList.add('copied');
        toast.textContent = 'Copied ' + hex;
        toast.classList.add('show');

        clearTimeout(toastTimer);
        toastTimer = setTimeout(function () {
          toast.classList.remove('show');
        }, 1200);

        setTimeout(function () {
          swatch.classList.remove('copied');
        }, 600);
      });
    });
  });
});
</script>
