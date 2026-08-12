import os

base = os.path.expanduser("~/Lego Website/Lego-Photography-Interactive-Portfolio")
os.chdir(base)

mosaics_scss = '''.mosaic-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.mosaic-card {
  text-align: center;

  .mosaic-name {
    margin: 0 0 0.5rem;
    font-size: 1.1em;
  }

  img {
    width: 100%;
    aspect-ratio: 3 / 4;
    object-fit: contain;
    background: #0d1117;
    border-radius: 6px;
    display: block;
    cursor: pointer;
  }

  .mosaic-link {
    display: inline-block;
    margin-top: 0.5rem;
    color: $link-color;
    font-size: 0.9em;
  }
}
'''

with open("_sass/_mosaics.scss", "w") as f:
    f.write(mosaics_scss)

print("Done: mosaics images now scale fluidly with screen width instead of a fixed height.")
