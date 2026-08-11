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
      <li>AFOL</li>
      <li>Avid Hiker</li>
      <li>Subpar Snowboarder</li>
      <li>Less Than Average Rock Climber</li>
    </ul>
  </div>
</div>

<section class="intro-section">
  <div class="intro-heading">
    <h1>About Me</h1>
  </div>
  <p class="intro-lede">I'm just a Colorado mountain gremlin with a camera. While I'm wondering around in the mountains I bring my Lego minifigs along to capture nature from a tiny perspective.</p>
</section>

<div id="lightbox-overlay" onclick="this.style.display='none'">
  <img id="lightbox-img" src="">
</div>

<section class="about-section background-section">
  <p class="section-eyebrow">Background</p>
  <p>Growing up, I loved playing with Legos &mdash; building the set was never really the point for me. I was a creative kid (my older sister might call me a menace) who'd finish a set, immediately take it completely apart, throw away the instructions, and try to build something totally random instead. I didn't know it at the time, but I was making MOCs, and I loved the chaos of it. My sister didn't always appreciate me doing the same thing to her sets.</p>
  <p>As a toddler I was mesmerized by Jurassic Park, then that faded into loving Star Wars, Harry Potter, and eventually anything space-related.</p>
</section>

<div class="stagger-grid">

  <div class="stagger-item">
    <div class="photo-placeholder">Photo coming soon</div>
    <div class="stagger-text">
      <h2>Background</h2>
      <p>Growing up, I loved playing with Legos &mdash; building the set was never really the point for me. I was a creative kid (my older sister might call me a menace) who'd finish a set, immediately take it completely apart, throw away the instructions, and try to build something totally random instead. I didn't know it at the time, but I was making MOCs, and I loved the chaos of it. My sister didn't always appreciate me doing the same thing to her sets.</p>
      <p>As a toddler I was mesmerized by Jurassic Park, then that faded into loving Star Wars, Harry Potter, and eventually anything space-related.</p>
    </div>
  </div>

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
      <p>Outside of my Lego hobby I spend most of my time working as a scientist, so I love sharing a fact with each photo to help myself and others learn more about the outdoor world.</p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/mosaics/IMG_9289.JPG" alt="Trans Flag Wreath Lego mosaic build" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Mosaics</h2>
      <p>I also love to build Lego mosaic-style art as a creative outlet.</p>
      <a class="btn-outline" href="{{ site.baseurl }}/mosaics/">See more mosaics</a>
    </div>
  </div>

</div>


<script>
  function showLightbox(src) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox-overlay').style.display = 'flex';
  }
</script>
