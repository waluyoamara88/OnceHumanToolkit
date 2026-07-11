from pathlib import Path

class GeneratorEngine:
    def __init__(self, root: Path):
        self.root=root
    def run(self):
        print("Generator Engine v1")
