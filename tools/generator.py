from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def write(path, content):
    file = ROOT / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content.lstrip(), encoding="utf-8")

def sprint003():

    plugins = [
        "api",
        "assets",
        "calculator",
        "cli",
        "database",
        "planner",
        "scraper",
        "updater",
        "website"
    ]

    write(
        "generator/plugins/base_plugin.py",
'''
from abc import ABC, abstractmethod

class BasePlugin(ABC):

    NAME="base"

    @abstractmethod
    def register(self):
        ...
'''
    )

    imports=[]
    registry=[]

    for p in plugins:

        cls=p.title()+"Plugin"

        write(
            f"generator/plugins/{p}.py",
f'''
from generator.plugins.base_plugin import BasePlugin

class {cls}(BasePlugin):

    NAME="{p}"

    def register(self):
        print("[PLUGIN]",self.NAME)
'''
        )

        imports.append(
            f"from generator.plugins.{p} import {cls}"
        )

        registry.append(f"{cls}()")

    write(
        "generator/plugins/plugin_registry.py",
f'''
{chr(10).join(imports)}

PLUGINS=[
    {",\n    ".join(registry)}
]
'''
    )

    print("Sprint003 Complete")

if __name__=="__main__":

    if len(sys.argv)<2:
        exit()

    if sys.argv[1]=="sprint003":
        sprint003()
