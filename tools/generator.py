from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def write(path, text):
    file = ROOT / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(text.lstrip(), encoding="utf-8")

def sprint004():

    manifests = {
        "project.yaml": """
name: OnceHumanToolkit
version: 0.1.0
license: MIT
python: "3.14"
""",
        "modules.yaml": """
modules:
  - api
  - database
  - website
  - scraper
  - assets
  - planner
  - calculator
  - cli
""",
        "plugins.yaml": """
plugins:
  - api
  - database
  - scraper
  - assets
  - planner
  - calculator
  - cli
""",
        "builders.yaml": """
builders:
  - backend
  - frontend
  - database
  - api
  - website
"""
    }

    for name, content in manifests.items():
        write(f"generator/manifests/{name}", content)

    write(
        "generator/core/manifest.py",
'''
from pathlib import Path
import yaml

class Manifest:

    def __init__(self, root):
        self.root = Path(root)

    def load(self, name):
        with open(self.root / "generator" / "manifests" / name, encoding="utf-8") as f:
            return yaml.safe_load(f)
'''
    )

    print("Sprint004 Complete")

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise SystemExit("python tools/generator.py sprint004")

    if sys.argv[1] == "sprint004":
        sprint004()
