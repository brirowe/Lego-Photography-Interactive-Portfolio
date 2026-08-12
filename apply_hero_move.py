with open('about.md', 'r') as f:
    about = f.read()

hero_block = '''<div class="about-hero">
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

'''

marker = '<section class="intro-section">'
if marker not in about:
    raise SystemExit("about.md: couldn't find intro-section marker, aborting")
about = about.replace(marker, hero_block + marker, 1)

with open('about.md', 'w') as f:
    f.write(about)

with open('index.md', 'r') as f:
    index = f.read()

old_hero = '''<div class="about-hero">
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
</div>'''

new_hero = '''<!-- TODO: swap in the photo number Bri picks for the home hero -->
<div class="about-hero">
  <img src="{{ site.baseurl }}/photos/about/about-PLACEHOLDER.jpg" alt="Home hero photo" loading="lazy">
</div>'''

if old_hero not in index:
    raise SystemExit("index.md: couldn't find hero block to replace, aborting")
index = index.replace(old_hero, new_hero, 1)

with open('index.md', 'w') as f:
    f.write(index)

print("Done: about.md and index.md updated.")
