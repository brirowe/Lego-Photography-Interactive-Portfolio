---
layout: default
title: Home
permalink: /
---

<div class="about-hero">
  <img src="{{ site.baseurl }}/photos/about/about-1.jpg" alt="Bri checking her camera in Arches National Park" loading="lazy">
  <div class="about-hero-overlay">
    <p class="hero-eyebrow">Backcountry Bricks</p>
    <div class="hero-name">I'm Bri</div>
    <ul class="hero-tagline">
      <li>Adult Fan of Lego</li>
      <li>Avid Hiker</li>
      <li>Subpar Snowboarder</li>
      <li>Less Than Average Rock Climber — All With a Camera</li>
    </ul>
  </div>
</div>

<section class="intro-section">
  <div class="intro-heading">
    <img class="intro-logo" src="{{ site.baseurl }}/photos/about/about-11.jpg" alt="Custom Bri minifig holding a camera" loading="lazy">
    <h1>About Bri</h1>
  </div>
  <div class="intro-columns">
    <p>I grew up building and playing with Legos, lost touch with them for a while, and found a whole new appreciation for them as an adult. Backcountry Bricks is that appreciation turned into a project.</p>
    <p>I take my childhood minifigs, plus a growing collection of ones I've picked up along the way, out hiking with me across the Rocky Mountains, mostly here in Colorado. I've also taken them to the deserts of Utah, the coast of Oregon, the beaches of Cancun, and the Alps of Japan.</p>
  </div>
  <a class="btn-outline" href="https://instagram.com/backcountry_bricks" target="_blank" rel="noopener">Follow along</a>
</section>

<div id="lightbox-overlay" onclick="this.style.display='none'">
  <img id="lightbox-img" src="">
</div>

<div class="stagger-grid">
    <div class="stagger-item">
      <img src="{{ site.baseurl }}/photos/about/about-2.jpg" alt="Bri scrambling along a rocky ridge" loading="lazy" onclick="showLightbox(this.src)">
      <div class="stagger-text">
        <h2>[Your headline here]</h2>
        <p>When people are out in nature, they're usually chasing the big views. I get it, I do it too.</p>
      </div>
    </div>

    <div class="stagger-item">
      <img src="{{ site.baseurl }}/photos/about/about-4.jpg" alt="Bri bouldering" loading="lazy" onclick="showLightbox(this.src)">
      <div class="stagger-text">
        <p class="stagger-caption">Yes, that's actually me climbing.</p>
      </div>
    </div>

    <div class="stagger-item">
      <img src="{{ site.baseurl }}/photos/about/about-6.jpg" alt="Bri kicking her leg up on the summit of Mt. Democrat" loading="lazy" onclick="showLightbox(this.src)">
      <div class="stagger-text">
        <h2>[Your headline here]</h2>
        <p>I really enjoy photographing a variety of Legos to build almost a digital collection, since I don't have space for a real one.</p>
      </div>
    </div>

    <div class="stagger-item">
      <img src="{{ site.baseurl }}/photos/mosaics/IMG_9289.JPG" alt="Trans Flag Wreath Lego mosaic build" loading="lazy" onclick="showLightbox(this.src)">
      <div class="stagger-text">
        <h2>[Your headline here]</h2>
        <p>A while back I took a class on Lego mosaics and got hooked. It's become my other creative outlet, piecing together art one brick at a time. This one's my Trans Flag Wreath build.</p>
        <a class="btn-outline" href="{{ site.baseurl }}/mosaics/">See more mosaics</a>
      </div>
    </div>

    <div class="stagger-item">
      <img src="{{ site.baseurl }}/photos/about/about-10.jpg" alt="Bri at a high alpine lake with two dogs" loading="lazy" onclick="showLightbox(this.src)">
      <div class="stagger-text">
        <h2>[Your headline here]</h2>
        <p>I'm sharing my mountain adventures through Legos, one tiny scene at a time.</p>
      </div>
    </div>

    <div class="stagger-item">
      <img src="{{ site.baseurl }}/photos/about/about-3.jpg" alt="Bri crouched down photographing a minifig in the sand dunes" loading="lazy" onclick="showLightbox(this.src)">
      <div class="stagger-text">
        <h2>[Your headline here]</h2>
        <p>But that means we miss the little things along the way: the plants, the rocks, the insects, the tiny landscapes underfoot. My goal isn't to take the most perfect photograph. It's to use a Lego minifigure as a size reference, something small and familiar, so you can actually see how tiny these things really are.</p>
      </div>
    </div>

    <div class="stagger-item">
      <img src="{{ site.baseurl }}/photos/about/about-5.jpg" alt="Bri standing on a dry cracked lakebed" loading="lazy" onclick="showLightbox(this.src)">
      <div class="stagger-text">
        <h2>[Your headline here]</h2>
        <p>[Write a sentence or two here]</p>
      </div>
    </div>

    <div class="stagger-item">
      <img src="{{ site.baseurl }}/photos/about/about-7.jpg" alt="Bri photographing a minifig at Red Rocks Amphitheatre" loading="lazy" onclick="showLightbox(this.src)">
      <div class="stagger-text">
        <h2>[Your headline here]</h2>
        <p>Everything outside my Lego hobby comes back to science for me, so I try to include a fact or two about whatever plant, bug, or landscape shows up in the shot.</p>
      </div>
    </div>

    <div class="stagger-item">
      <img src="{{ site.baseurl }}/photos/about/about-8.jpg" alt="Bri jumping on a frozen alpine lake" loading="lazy" onclick="showLightbox(this.src)">
      <div class="stagger-text">
        <h2>[Your headline here]</h2>
        <p>[Write a sentence or two about your camera and lenses here]</p>
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
