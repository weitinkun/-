"""Prepare the prebuilt site for this repository's GitHub Pages subpath."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site"
DESTINATION = ROOT / "_site"
BASE = "/-/"

if DESTINATION.exists():
    shutil.rmtree(DESTINATION)
shutil.copytree(SOURCE, DESTINATION)

for path in (DESTINATION / "index.html", *DESTINATION.glob("assets/*.js")):
    content = path.read_text(encoding="utf-8")
    for directory in ("assets", "images", "media", "video"):
        content = content.replace(f"/{directory}/", f"{BASE}{directory}/")
    content = content.replace("/favicon.svg", f"{BASE}favicon.svg")
    path.write_text(content, encoding="utf-8")

(DESTINATION / ".nojekyll").touch()
print(f"Prepared {sum(1 for path in DESTINATION.rglob('*') if path.is_file())} files")
