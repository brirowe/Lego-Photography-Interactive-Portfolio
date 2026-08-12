with open('_sass/about.scss', 'r') as f:
    scss = f.read()

old_block = '''// -----
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

new_block = '''// -----
// Home page hero: dimmed image + centered title overlay near top

.home-hero {
	img {
		opacity: .8;
	}
}

.home-hero-overlay {
	position: absolute;
	left: 0;
	right: 0;
	top: 0;
	padding: 40px 50px;
	text-align: center;
	background: linear-gradient(to bottom, rgba(0,0,0,.75) 0%, rgba(0,0,0,.35) 60%, rgba(0,0,0,0) 100%);
}

.home-hero-title {
	font-family: $font-display;
	font-weight: 700;
	text-transform: uppercase;
	letter-spacing: .12em;
	font-size: 1.6em;
	color: $color;
	text-shadow: 0 2px 14px rgba(0,0,0,.85);

	@media #{$tablet} {
		font-size: 2.2em;
	}

	@media #{$desktop} {
		font-size: 3em;
	}
}
'''

if old_block not in scss:
    raise SystemExit("about.scss: couldn't find old home-hero block, aborting")
scss = scss.replace(old_block, new_block, 1)

with open('_sass/about.scss', 'w') as f:
    f.write(scss)

print("Done: about.scss home-hero block updated.")
