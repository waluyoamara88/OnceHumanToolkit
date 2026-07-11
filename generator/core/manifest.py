from pathlib import Path
import yaml

class Manifest:

    def __init__(self, root):
        self.root = Path(root)

    def load(self, name):
        with open(self.root / "generator" / "manifests" / name, encoding="utf-8") as f:
            return yaml.safe_load(f)
