from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parent.parent

class Generator:

    def write(self, path: str, content: str = ""):
        p = ROOT / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content.lstrip(), encoding="utf-8")

    def touch(self, path: str):
        self.write(path)

    def build(self):

        dirs = [
            "generator/core",
            "generator/builders",
            "generator/plugins",
            "generator/manifests",
            "generator/templates",
            "generator/config",
            "generator/cli",
            "generator/pipeline",

            "app/api",
            "app/core",
            "app/models",
            "app/schemas",
            "app/repositories",
            "app/services",
            "app/workers",

            "assets",
            "data/json",
            "data/sqlite",
            "docs",
            "tests"
        ]

        for d in dirs:
            (ROOT / d).mkdir(parents=True, exist_ok=True)

        manifest = {
            "name":"OnceHumanToolkit",
            "version":"0.1.0",
            "python":"3.14"
        }

        self.write(
            "generator/manifests/project.json",
            json.dumps(manifest, indent=2)
        )

        self.write(
            "generator/core/engine.py",
'''
class GeneratorEngine:

    def run(self):
        print("Generator Engine Running")
'''
        )

        self.write(
            "generator/build.py",
'''
from generator.core.engine import GeneratorEngine

GeneratorEngine().run()
'''
        )

        print("Build Success")

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "command",
        choices=[
            "build"
        ]
    )

    args = parser.parse_args()

    gen = Generator()

    if args.command == "build":
        gen.build()

if __name__ == "__main__":
    main()
