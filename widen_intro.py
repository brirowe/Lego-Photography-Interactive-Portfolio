import os

base = os.path.expanduser("~/Lego Website/Lego-Photography-Interactive-Portfolio")
os.chdir(base)

with open("_sass/shop.scss") as f:
    scss = f.read()

if '.shop-intro' not in scss:
    scss = scss.replace(
        '// -----\n// Shop page\n',
        '// -----\n// Shop page\n\n.shop-intro {\n\tmax-width: 1100px;\n}\n'
    )
    with open("_sass/shop.scss", "w") as f:
        f.write(scss)

with open("shop.md") as f:
    content = f.read()

content = content.replace(
    '<section class="intro-section">',
    '<section class="intro-section shop-intro">'
)

with open("shop.md", "w") as f:
    f.write(content)

print("Done: shop intro now matches full page width.")
