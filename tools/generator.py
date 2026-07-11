from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def write(path: str, text: str):
    file = ROOT / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(text.lstrip(), encoding="utf-8")

def sprint002():

    builders = [
        "backend",
        "frontend",
        "database",
        "sqlite",
        "json",
        "api",
        "assets",
        "scraper",
        "calculator",
        "planner",
        "website",
        "docs",
        "github",
        "cli",
        "updater",
    ]

    write(
        "generator/builders/base_builder.py",
'''
from abc import ABC, abstractmethod

class BaseBuilder(ABC):

    NAME = "base"

    @abstractmethod
    def build(self):
        ...
'''
    )

    registry = []

    for builder in builders:

        cls = builder.title().replace("_","") + "Builder"

        write(
            f"generator/builders/{builder}_builder.py",
f'''
from generator.builders.base_builder import BaseBuilder

class {cls}(BaseBuilder):

    NAME = "{builder}"

    def build(self):
        print("[BUILD]", self.NAME)
'''
        )

        registry.append(
            f"from generator.builders.{builder}_builder import {cls}"
        )

    imports = "\n".join(registry)

    classes = ",\n    ".join(
        x.title().replace("_","")+"Builder()"
        for x in builders
    )

    write(
        "generator/builders/builder_registry.py",
f'''
{imports}

BUILDERS = [
    {classes}
]
'''
    )

    print("Sprint002 OK")

if __name__=="__main__":

    if len(sys.argv)<2:
        print("python tools/generator.py sprint002")
        raise SystemExit

    if sys.argv[1]=="sprint002":
        sprint002()
