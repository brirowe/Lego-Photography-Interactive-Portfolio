---
layout: default
title: About
permalink: /about/
---

<div class="about-hero">
  <img src="{{ site.baseurl }}/photos/about/about-1.jpg" alt="Bri checking her camera in Arches National Park" loading="lazy">
  <div class="about-hero-overlay">
    <div class="hero-name">I'm Bri</div>
    <ul class="hero-tagline">
      <li>Adult Fan of Lego</li>
      <li>Avid Hiker</li>
      <li>Subpar Snowboarder</li>
      <li>Less Than Average Rock Climber</li>
    </ul>
  </div>
</div>

<section class="intro-section">
  <div class="intro-heading">
    <img class="intro-logo" src="{{ site.baseurl }}/photos/about/about-11.jpg" alt="Custom Bri minifig holding a camera" loading="lazy">
    <h1>About Bri</h1>
  </div>
  <p class="intro-lede">Hi, I'm Bri! Adult fan of Lego, avid hiker, subpar snowboarder, and less than average rock climber — all with a camera. I take my Lego minifigs hiking across Colorado (and beyond) to capture how tiny the world really is, one scene at a time.</p>
  <a class="btn-outline" href="https://instagram.com/backcountry_bricks" target="_blank" rel="noopener">Follow along</a>
</section>

<div id="lightbox-overlay" onclick="this.style.display='none'">
  <img id="lightbox-img" src="">
</div>

<div class="stagger-grid">

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-3.jpg" alt="Bri crouched down photographing a minifig in the sand dunes" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Idea</h2>
      <p>I use a Lego minifigure as a size reference, so you can see just how tiny the little things in nature really are. A flower. A rock. A patch of moss.</p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-7.jpg" alt="Bri photographing a minifig at Red Rocks Amphitheatre" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Science</h2>
      <p>Everything outside my Lego hobby comes back to science, so I love sharing a fact or two along with each photo.</p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/mosaics/IMG_9289.JPG" alt="Trans Flag Wreath Lego mosaic build" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Mosaics</h2>
      <p>I also build Lego mosaics as a creative outlet, one brick at a time.</p>
      <a class="btn-outline" href="{{ site.baseurl }}/mosaics/">See more mosaics</a>
    </div>
  </div>

</div>

<section class="about-section values-section">
  <p class="section-eyebrow">What I Stand For</p>
  <div class="values-box">
    <ul>
      <li>Women-owned</li>
      <li>LGBTQ+ supportive</li>
      <li>Committed to protecting public lands and national parks</li>
    </ul>
  </div>
</section>

<script>
  function showLightbox(src) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox-overlay').style.display = 'flex';
  }
</script>
