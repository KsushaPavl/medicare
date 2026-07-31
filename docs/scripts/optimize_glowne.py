#!/usr/bin/env python3
"""Generate optimized hero images from glowne-original.jpg."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "images" / "glowne-original.jpg"
OUT = ROOT / "images"

VARIANTS = [
    ("glowne-desktop", 2560),
    ("glowne-mobile", 1200),
]

WEBP_QUALITY = 82
JPEG_QUALITY = 84


def resize_to_width(img: Image.Image, width: int) -> Image.Image:
    w, h = img.size
    if w <= width:
        return img.copy()
    new_h = round(h * width / w)
    return img.resize((width, new_h), Image.Resampling.LANCZOS)


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"Source not found: {SRC}")

    img = Image.open(SRC).convert("RGB")
    OUT.mkdir(parents=True, exist_ok=True)

    for name, width in VARIANTS:
        resized = resize_to_width(img, width)
        webp_path = OUT / f"{name}.webp"
        jpg_path = OUT / f"{name}.jpg"

        resized.save(webp_path, "WEBP", quality=WEBP_QUALITY, method=6)
        resized.save(jpg_path, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)

        print(f"{name}: {resized.size[0]}x{resized.size[1]}")
        print(f"  webp {webp_path.stat().st_size // 1024} KB")
        print(f"  jpg  {jpg_path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
