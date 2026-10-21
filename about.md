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
  <p class="intro-lede">I'm just a Colorado mountain gremlin with a camera.</p>
  <p class="intro-lede">While I'm wandering around in the wild, I bring my Lego minifigs along to capture nature from a tiny perspective.</p>
</section>

<div id="lightbox-overlay" onclick="this.style.display='none'">
  <img id="lightbox-img" src="">
</div>

<div class="stagger-grid">

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-4.jpg" alt="Bri bouldering, hanging upside down on a rock formation" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>Background</h2>
      <p>Growing up I loved Legos and saw them as a way to build my own creations rather than follow the instructions. On top of that, as a toddler I was fascinated by Jurassic Park, then became a huge Star Wars fan and eventually grew to be fascinated with pretty much anything space related as an adult. Rediscovering my love for Legos and using them to not only show my creativity, but also share my outdoor adventures has been such a blast! </p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-2.jpg" alt="Bri scrambling up a rocky mountain ridge with mountain views behind her" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Backcountry</h2>
      <p>Some of my biggest passions in life are adventure and exploration, especially in the mountains. I'm lucky enough to live in Colorado, where I spend most of my free time hiking, snowboarding, and rock climbing, though I don't strive to be the best at any of them (photography included, lol). It's really just about my love of being in nature, and this photography hobby has been a great way to share my experiences with people in a unique way.</p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-3.jpg" alt="Bri crouched down photographing a minifig in the sand dunes" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Idea</h2>
      <p>Macro photography captures incredibly small details, but can lack size perspective. This can make it hard to visualize just how tiny some things really are, so I thought it would be helpful to use Lego minifigures as a reference, since most people are familiar with their size.  Often times people go hiking to chase the end destination and picture perfect views, but there are so many little things along the way like wildflowers, rocks, moss, etc. My goal with this photography is to highlight the small side of nature and beautiful places from the perspertive of Legos.</p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-13.jpg" alt="Bri sitting on her snowboard on a mountain slope, smiling" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Science</h2>
      <p>Outside of my Lego hobby I spend most of my time working as a researcher, so I love sharing a fact with each photo to help myself and others learn more about the outdoor world. Alpine environments are incredibly complex and interesting, whether it's how plants manage to survive in such harsh conditions, the intricate details in rock formations, or weird facts about popular landmarks across the West. </p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/about/about-5.jpg" alt="Bri standing on cracked mud flats next to a river with red rock cliffs behind her" loading="lazy" onclick="showLightbox(this.src)">
    <div class="stagger-text">
      <h2>The Archive</h2>
      <p>Due to Colorado's cost of living, I don't foresee having space anytime soon for a spare Lego room, so I use this photography as a digital collection instead. This is my way of "collecting" not only nostalgic and new minifigs, but also serves as an archive of the plants, places, and small things I've seen along my adventures. Due to this I often sell my used pieces/minifigs so check out my shop page if you're looking to build your physical collection!</p>
    </div>
  </div>

  <div class="stagger-item">
    <img src="{{ site.baseurl }}/photos/mosaics/thumbs/mosaic-9289.jpg" alt="Trans Flag Wreath Lego mosaic build" loading="lazy" onclick="showLightbox('{{ site.baseurl }}/photos/mosaics/mosaic-9289.jpg')">
    <div class="stagger-text">
      <h2>The Mosaics</h2>
      <p>In addition to Minifig photography, I also love to build Lego mosaic-style art as a creative outlet. It's been a fun way to create designs with random pieces and show off some of the cool colors Lego makes. I've really enjoyed making flags to represent things I care about and different groups of people, along with finding a purpose for the random Lego pieces I have laying around. This is a corner of the Lego world I only discovered recently, but have really loved and want to share with others!</p>
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
