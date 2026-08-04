#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

TEX_FILE = "priyansh_mahajan_cv.tex"
PDF_FILE = "priyansh_mahajan_cv.pdf"

def run(cmd):
    print(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd)
    if res.returncode != 0:
        sys.exit(res.returncode)

cwd = Path.cwd()

run(["docker", "build", "-t", "tectonic-cv", "."])

print("--- Compiling real PDF using secrets.tex ---")
cmd = [
    "docker", "run", "--rm",
    "-v", f"{cwd}:/data",
    "-v", "tectonic-cache:/root/.cache/tectonic",
    "tectonic-cv",
    "tectonic", TEX_FILE
]
run(cmd)

print("\nReal CV build complete!")
print("  - Output PDF: priyansh_mahajan_cv.pdf (compiled using real secrets.tex)")
