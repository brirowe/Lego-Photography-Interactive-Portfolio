with open('index.md', 'r') as f:
    index = f.read()

replacements = [
    ('<!-- TODO: swap in a map screenshot -->\n    <img src="{{ site.baseurl }}/photos/about/map-PLACEHOLDER.jpg" alt="Map">',
     '<img src="{{ site.baseurl }}/photos/about/map-preview.jpg" alt="Map">'),
    ('<!-- TODO: swap in a color palette screenshot -->\n    <img src="{{ site.baseurl }}/photos/about/palette-PLACEHOLDER.jpg" alt="Color Palettes">',
     '<img src="{{ site.baseurl }}/photos/about/palette-preview.jpg" alt="Color Palettes">'),
]

for old, new in replacements:
    if old not in index:
        raise SystemExit(f"index.md: couldn't find block, aborting")
    index = index.replace(old, new, 1)

with open('index.md', 'w') as f:
    f.write(index)

print("Done: index.md updated with real placeholder filenames.")
