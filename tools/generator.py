from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def write(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.lstrip(), encoding="utf-8")

def sprint008():

    write(
        "generator/core/engine.py",
'''
from generator.builders.builder_registry import BUILDERS

class GeneratorEngine:

    def run(self):

        print("="*60)
        print(" OnceHumanToolkit Generator")
        print("="*60)

        for builder in BUILDERS:
            print(f"Running {builder.NAME}...")
            builder.build()

        print("="*60)
        print("Build Complete")
'''
    )

    write(
        "generator/cli/main.py",
'''
import argparse

from generator.core.engine import GeneratorEngine

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "command",
        choices=[
            "build",
            "doctor",
            "validate"
        ]
    )

    args = parser.parse_args()

    if args.command == "build":
        GeneratorEngine().run()

if __name__=="__main__":
    main()
'''
    )

    write(
        "generator/build.py",
'''
from generator.cli.main import main

main()
'''
    )

    print("Sprint008 Complete")

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise SystemExit

    if sys.argv[1] == "sprint008":
        sprint008()
