from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def write(path, text):
    file = ROOT / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(text.lstrip(), encoding="utf-8")

def sprint005():

    write(
        "generator/core/context.py",
'''
from pathlib import Path

class BuildContext:

    def __init__(self, root):
        self.root = Path(root)
        self.output = self.root
        self.variables = {}
'''
    )

    write(
        "generator/core/filesystem.py",
'''
from pathlib import Path

class FileSystem:

    @staticmethod
    def mkdir(path):
        Path(path).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def write(path, text):
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
'''
    )

    write(
        "generator/core/logger.py",
'''
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)

logger = logging.getLogger("OnceHumanToolkit")
'''
    )

    write(
        "generator/core/config.py",
'''
class Config:

    PROJECT_NAME = "OnceHumanToolkit"
    VERSION = "0.1.0"
'''
    )

    write(
        "generator/core/registry.py",
'''
class Registry:

    def __init__(self):
        self.items=[]

    def register(self,obj):
        self.items.append(obj)
'''
    )

    print("Sprint005 Complete")

if __name__=="__main__":

    if len(sys.argv)<2:
        raise SystemExit

    if sys.argv[1]=="sprint005":
        sprint005()
