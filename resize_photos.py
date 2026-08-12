from pathlib import Path
from PIL import Image, ImageOps
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = False  # keep strict so we catch bad files

INPUT_DIR = Path.home() / "Lego Website" / "Home Page Photos"
OUTPUT_DIR = Path.home() / "Lego Website" / "Lego-Photography-Interactive-Portfolio" / "photos" / "about"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MAX_DIM = 1600
QUALITY = 82

photo_map = {
    "1.JPG": 1,
    "2.jpg": 2,
    "3.JPG": 3,
    "4.jpg": 4,
    "5.JPG": 5,
    "6.jpg": 6,
    "7.JPG": 7,
    "8.jpg": 8,
    "10.JPG": 10,
}

failed = []

for filename, n in photo_map.items():
    src = INPUT_DIR / filename
    if not src.exists():
        print(f"missing: {filename}")
        continue

    try:
        img = Image.open(src)
        img = ImageOps.exif_transpose(img)
        img = img.convert("RGB")
        img.thumbnail((MAX_DIM, MAX_DIM), Image.LANCZOS)

        out_path = OUTPUT_DIR / f"about-{n}.jpg"
        img.save(out_path, "JPEG", quality=QUALITY, optimize=True)
        print(f"saved {out_path.name}  ({out_path.stat().st_size // 1024} KB)")
    except OSError as e:
        print(f"FAILED: {filename}  -> {e}")
        failed.append(filename)

print("done")
if failed:
    print(f"\n{len(failed)} file(s) need to be re-uploaded: {failed}")
