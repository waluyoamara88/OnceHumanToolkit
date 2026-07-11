from pathlib import Path

class BuildContext:

    def __init__(self, root):
        self.root = Path(root)
        self.output = self.root
        self.variables = {}
