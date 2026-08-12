with open('index.md', 'r') as f:
    index = f.read()

old = '''<!-- TODO: swap in the photo number Bri picks for the home hero -->
<div class="about-hero">
  <img src="{{ site.baseurl }}/photos/about/about-12.jpg" alt="Home hero photo" loading="lazy">
</div>'''

new = '''<div class="about-hero home-hero">
  <img src="{{ site.baseurl }}/photos/about/about-12.jpg" alt="Home hero photo" loading="lazy">
  <div class="home-hero-overlay">
    <span class="home-hero-title">Backcountry Bricks</span>
  </div>
</div>'''

if old not in index:
    raise SystemExit("index.md: couldn't find placeholder hero block, aborting")
index = index.replace(old, new, 1)

with open('index.md', 'w') as f:
    f.write(index)

css = '''
// -----
// Home page hero: dimmed image + centered title overlay

.home-hero {
	img {
		opacity: .8;
	}
}

.home-hero-overlay {
	position: absolute;
	inset: 0;
	display: flex;
	align-items: center;
	justify-content: center;
	text-align: center;
	background: rgba(16, 16, 16, .2);
}

.home-hero-title {
	font-family: $font-display;
	font-weight: 700;
	text-transform: uppercase;
	letter-spacing: .12em;
	font-size: 2em;
	color: $color;
	text-shadow: 0 2px 14px rgba(0,0,0,.85);

	@media #{$tablet} {
		font-size: 2.6em;
	}

	@media #{$desktop} {
		font-size: 3.6em;
	}
}
'''

with open('_sass/about.scss', 'a') as f:
    f.write(css)

print("Done: index.md and about.scss updated.")
