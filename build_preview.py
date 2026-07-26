#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

TEX_FILE = "priyansh_mahajan_cv.tex"
PDF_FILE = "priyansh_mahajan_cv.pdf"
PREVIEW_NAME = "cv_preview"

def run(cmd):
    print(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd)
    if res.returncode != 0:
        sys.exit(res.returncode)

cwd = Path.cwd()
example_secrets = cwd / "secrets.example.tex"

run(["docker", "build", "-t", "tectonic-cv", "."])

print("--- Generating public PDF and PNG preview using secrets.example.tex ---")
cmd = [
    "docker", "run", "--rm",
    "-v", f"{cwd}:/data",
    "-v", f"{example_secrets}:/data/secrets.tex:ro",
    "-v", "tectonic-cache:/root/.cache/tectonic",
    "tectonic-cv",
    "sh", "-c", f"tectonic {TEX_FILE} && pdftoppm -png -r 150 -singlefile {PDF_FILE} {PREVIEW_NAME}"
]
run(cmd)

print("\nPreview build complete!")
print("  - PDF: priyansh_mahajan_cv.pdf")
print("  - PNG Preview: cv_preview.png")
