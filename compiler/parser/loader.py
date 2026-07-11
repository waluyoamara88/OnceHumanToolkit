from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent

SPEC_DIR = ROOT / "specs"

class Project:

    def __init__(self):
        self.data = {}

    def load(self):

        for file in SPEC_DIR.glob("*.yaml"):

            with open(file,"r",encoding="utf8") as f:

                self.data[file.stem]=yaml.safe_load(f)

        return self.data

if __name__=="__main__":

    project=Project()

    data=project.load()

    print("="*60)

    for k in data:
        print(k)

    print("="*60)
