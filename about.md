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

<div class="stagger-grid">

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-4.jpg" alt="Bri bouldering, hanging upside down on a rock formation" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>Background</h2>
      <p>Growing up I loved Legos, mostly for the creativity of it and being able to build whatever I wanted. As a toddler I was really into Jurassic Park, then that turned into a Star Wars phase, then Harry Potter, then pretty much anything space related, so it was cool to see that Lego had tiny versions of all of it.</p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-2.jpg" alt="Bri scrambling up a rocky mountain ridge with mountain views behind her" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Backcountry</h2>
      <p>One of my biggest passions in life is getting outside and exploring, especially in the mountains. I'm lucky enough to live in Colorado, which has endless places to appreciate. I spend most of my free time hiking, snowboarding, and rock climbing, though I don't strive to be the best at any of them (photography included, lol). It's really just about my love of nature and experiencing the outdoors, and it's cool to be able to share that with people in a unique way.</p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-3.jpg" alt="Bri crouched down photographing a minifig in the sand dunes" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Idea</h2>
      <p>Macro photography often captures incredibly small details, but it lacks size perspective, so it's hard to visualize just how tiny some things really are. So I thought it would be helpful to use Lego minifigures as a reference, since most people are familiar with their mostly consistent size. This lets people see just how tiny the little things in nature really are, like wildflowers, rock formations, moss, and more.</p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-7.jpg" alt="Bri photographing a minifig at Red Rocks Amphitheatre" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Science</h2>
      <p>Outside of my Lego hobby I spend most of my time working as a scientist, so I love sharing a fact with each photo to help myself and others learn more about the outdoor world. Alpine environments are incredibly complex, from how plants manage to survive in such harsh conditions to the intricate details in rock formations and weird facts about popular landmarks across the West. </p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/mosaics/IMG_9289.JPG" alt="Trans Flag Wreath Lego mosaic build" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Mosaics</h2>
      <p>I also love to build Lego mosaic-style art as a creative outlet. It's a fun way to create designs with random pieces and show off some of the cool colors Lego makes. I also have enjoyed making flags to represent things I care about and represent different groups of people. This is a corner of the Lego world I only discovered recently, but have really loved and want to share with others!</p>
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
