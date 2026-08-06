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
      <li>Less Than Average Rock Climber</li>
    </ul>
  </div>
</div>

<div class="about-logo">
  <img src="{{ site.baseurl }}/photos/about/about-11.jpg" alt="Custom Bri minifig holding a camera" loading="lazy">
</div>

<div id="lightbox-overlay" onclick="this.style.display='none'">
  <img id="lightbox-img" src="">
</div>

<div class="story-grid">

  <div class="story-item">
    <img src="{{ site.baseurl }}/photos/about/about-2.jpg" alt="Bri scrambling along a rocky ridge" loading="lazy" onclick="showLightbox(this.src)">
    <p class="section-eyebrow">The Story</p>
    <p>I grew up building and playing with Legos, lost touch with them for a while, and found a whole new appreciation for them as an adult.</p>
  </div>

  <div class="story-item">
    <img src="{{ site.baseurl }}/photos/about/about-3.jpg" alt="Bri crouched down photographing a minifig in the sand dunes" loading="lazy" onclick="showLightbox(this.src)">
    <p class="section-eyebrow">The Idea</p>
    <p>When people are out in nature, they're usually chasing the big views. I get it, I do it too. But that means we miss the little things along the way: the plants, the rocks, the insects, the tiny landscapes underfoot.</p>
  </div>

  <div class="story-item">
    <img src="{{ site.baseurl }}/photos/about/about-4.jpg" alt="Bri bouldering" loading="lazy" onclick="showLightbox(this.src)">
    <p class="section-eyebrow">The Story</p>
    <p>Backcountry Bricks is that appreciation turned into a project. I take my childhood minifigs, plus a growing collection of ones I've picked up along the way, out hiking with me across the Rocky Mountains, mostly here in Colorado.</p>
  </div>

  <div class="story-item">
    <img src="{{ site.baseurl }}/photos/about/about-5.jpg" alt="Bri standing on a dry cracked lakebed" loading="lazy" onclick="showLightbox(this.src)">
    <p class="section-eyebrow">The Story</p>
    <p>I've also taken them to the deserts of Utah, the coast of Oregon, the beaches of Cancun, and the Alps of Japan.</p>
  </div>

  <div class="story-item">
    <img src="{{ site.baseurl }}/photos/about/about-6.jpg" alt="Bri kicking her leg up on the summit of Mt. Democrat" loading="lazy" onclick="showLightbox(this.src)">
    <p class="section-eyebrow">The Idea</p>
    <p>My goal isn't to take the most perfect photograph. It's to use a Lego minifigure as a size reference, something small and familiar, so you can actually see how tiny these things really are.</p>
  </div>

  <div class="story-item">
    <img src="{{ site.baseurl }}/photos/about/about-7.jpg" alt="Bri photographing a minifig at Red Rocks Amphitheatre" loading="lazy" onclick="showLightbox(this.src)">
    <p class="section-eyebrow">The Science</p>
    <p>Everything outside my Lego hobby comes back to science for me, so I try to include a fact or two about whatever plant, bug, or landscape shows up in the shot.</p>
  </div>

  <div class="story-item">
    <img src="{{ site.baseurl }}/photos/mosaics/IMG_9289.JPG" alt="Trans Flag Wreath Lego mosaic build" loading="lazy" onclick="showLightbox(this.src)">
    <p class="section-eyebrow">The Mosaics</p>
    <p>A while back I took a class on Lego mosaics and got hooked. It's become my other creative outlet, piecing together art one brick at a time. This one's my Trans Flag Wreath build. Check out the <a href="{{ site.baseurl }}/mosaics/">mosaics page</a> for more.</p>
  </div>

  <div class="story-item">
    <img src="{{ site.baseurl }}/photos/about/about-8.jpg" alt="Bri jumping on a frozen alpine lake" loading="lazy" onclick="showLightbox(this.src)">
    <p class="section-eyebrow">The Science</p>
    <p>Half the fun is learning something new on the trail, and I like sharing that along with the photo.</p>
  </div>

  <div class="story-full-width">
    <p class="section-eyebrow">What I Stand For</p>
    <div class="values-box">
      <ul>
        <li>Women-owned</li>
        <li>LGBTQ+ supportive</li>
        <li>Committed to protecting public lands and national parks</li>
      </ul>
    </div>
  </div>

  <div class="story-item">
    <img src="{{ site.baseurl }}/photos/about/about-10.jpg" alt="Bri at a high alpine lake with two dogs" loading="lazy" onclick="showLightbox(this.src)">
    <p class="section-eyebrow">The Idea</p>
    <p>A flower. A rock. A patch of moss. I'm sharing my mountain adventures through Legos, one tiny scene at a time.</p>
  </div>

</div>

<script>
  function showLightbox(src) {
    document.getElementById('lightbox-img').src = src;
    document.getElementById('lightbox-overlay').style.display = 'flex';
  }
</script>
