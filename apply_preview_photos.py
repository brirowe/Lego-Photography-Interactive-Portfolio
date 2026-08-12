with open('index.md', 'r') as f:
    index = f.read()

replacements = [
    ('<img src="{{ site.baseurl }}/photos/about/about-3.jpg" alt="About Bri">',
     '<img src="{{ site.baseurl }}/photos/about/about-6.jpg" alt="About Bri">'),
    ('<img src="{{ site.baseurl }}/photos/about/about-6.jpg" alt="Map">',
     '<!-- TODO: swap in a map screenshot -->\n    <img src="{{ site.baseurl }}/photos/about/map-PLACEHOLDER.jpg" alt="Map">'),
    ('<img src="{{ site.baseurl }}/photos/about/about-7.jpg" alt="Minifig Archive">',
     '<img src="{{ site.baseurl }}/photos/about/about-11.jpg" alt="Minifig Archive">'),
    ('<img src="{{ site.baseurl }}/photos/about/about-5.jpg" alt="Color Palettes">',
     '<!-- TODO: swap in a color palette screenshot -->\n    <img src="{{ site.baseurl }}/photos/about/palette-PLACEHOLDER.jpg" alt="Color Palettes">'),
]

for old, new in replacements:
    if old not in index:
        raise SystemExit(f"index.md: couldn't find {old!r}, aborting")
    index = index.replace(old, new, 1)

with open('index.md', 'w') as f:
    f.write(index)

print("Done: index.md preview-grid images updated.")
