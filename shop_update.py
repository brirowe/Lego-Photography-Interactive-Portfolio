import os

base = os.path.expanduser("~/Lego Website/Lego-Photography-Interactive-Portfolio")
os.chdir(base)

# 1. New shop.scss partial
shop_scss = '''// -----
// Shop page

.shop-apps-grid {
	display: grid;
	grid-template-columns: repeat(2, 1fr);
	gap: 1rem;
	max-width: 700px;
	margin: 1.5rem auto 0;

	@media #{$tablet} {
		grid-template-columns: repeat(3, 1fr);
	}
}

.shop-app-link {
	display: flex;
	align-items: center;
	justify-content: center;
	padding: 1.1em 1em;
	border: 1px solid rgba(255,255,255,.15);
	border-radius: 6px;
	color: $color;
	text-decoration: none;
	font-family: $font-display;
	text-transform: uppercase;
	letter-spacing: .06em;
	font-size: .95em;
	text-align: center;
	transition: border-color .2s ease, background .2s ease;

	&:hover {
		border-color: $accent;
		background: rgba(201,123,74,.1);
	}
}

.partner-card {
	display: grid;
	grid-template-columns: 1fr;
	gap: 2rem;
	max-width: 1000px;
	margin: 1.5rem auto 0;

	@media #{$mid-point} {
		grid-template-columns: 1.1fr 1fr;
		align-items: center;
	}
}

.partner-info {
	h3 {
		font-family: $font-display;
		font-size: 1.3em;
		margin: 0 0 .6rem;
	}

	p {
		margin: 0 0 1rem;
	}

	.partner-address {
		color: rgba(255,255,255,.65);
		font-size: .95em;
		margin: 0 0 1.2rem;
		line-height: 1.6;
	}
}

.partner-photos {
	display: grid;
	grid-template-columns: repeat(3, 1fr);
	gap: 10px;

	@media #{$tablet} {
		grid-template-columns: repeat(3, 1fr);
	}
}

.partner-photo-placeholder {
	aspect-ratio: 3 / 4;
	display: flex;
	align-items: center;
	justify-content: center;
	border: 1px dashed rgba(255,255,255,.3);
	border-radius: 6px;
	color: rgba(255,255,255,.5);
	font-family: $font-display;
	text-transform: uppercase;
	letter-spacing: .08em;
	font-size: .8em;
	text-align: center;
	padding: .5em;
}
'''

with open("_sass/shop.scss", "w") as f:
    f.write(shop_scss)

# 2. Register the partial in screen.scss
with open("css/screen.scss") as f:
    screen = f.read()

if '@import "shop";' not in screen:
    screen = screen.rstrip("\n") + "\n@import \"shop\";\n"
    with open("css/screen.scss", "w") as f:
        f.write(screen)

# 3. Shop page content
shop_md = '''---
layout: default
title: Shop
permalink: /shop/
---

<section class="intro-section">
  <div class="intro-heading">
    <h1>Shop</h1>
  </div>
  <p class="intro-lede">I sell complete used Lego sets, parts and pieces, minifigs, and my custom Lego art and prints.</p>
</section>

<section class="about-section">
  <p class="section-eyebrow">Apps I Sell On</p>
  <div class="shop-apps-grid">
    <a class="shop-app-link" href="#" target="_blank" rel="noopener">Depop</a>
    <a class="shop-app-link" href="#" target="_blank" rel="noopener">Whatnot</a>
    <a class="shop-app-link" href="#" target="_blank" rel="noopener">Poshmark</a>
    <a class="shop-app-link" href="#" target="_blank" rel="noopener">Vinted</a>
    <a class="shop-app-link" href="#" target="_blank" rel="noopener">eBay</a>
  </div>
</section>

<section class="about-section">
  <p class="section-eyebrow">Buy Prints In Person</p>
  <div class="partner-card">
    <div class="partner-info">
      <h3>Bricks &amp; Minifigs Centennial</h3>
      <p>I partner with a local Lego franchise, Bricks &amp; Minifigs Centennial in Colorado. You can buy my prints there along with sets to build Lego frames for them.</p>
      <p class="partner-address">
        12201 E Arapahoe Rd, Ste A4<br>
        Centennial, CO 80112<br>
        (720) 636-5556
      </p>
      <a class="btn-outline" href="https://www.google.com/maps/search/?api=1&query=Bricks+%26+Minifigs+Centennial+12201+E+Arapahoe+Rd+Ste+A4+Centennial+CO+80112" target="_blank" rel="noopener">Get Directions</a>
    </div>
    <div class="partner-photos">
      <div class="partner-photo-placeholder">Photo</div>
      <div class="partner-photo-placeholder">Photo</div>
      <div class="partner-photo-placeholder">Photo</div>
    </div>
  </div>
</section>
'''

with open("shop.md", "w") as f:
    f.write(shop_md)

print("Done: _sass/shop.scss, css/screen.scss, shop.md updated.")
