from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def write(path, text):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.lstrip(), encoding="utf-8")

def sprint007():

    write(
        "generator/core/writer.py",
'''
from pathlib import Path

class ProjectWriter:

    @staticmethod
    def write(path, content):
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
'''
    )

    write(
        "generator/core/validator.py",
'''
from pathlib import Path

class Validator:

    REQUIRED = [
        "generator/manifests/project.yaml",
        "generator/builders/builder_registry.py",
        "generator/plugins/plugin_registry.py",
    ]

    def validate(self):

        missing = []

        for item in self.REQUIRED:
            if not Path(item).exists():
                missing.append(item)

        return missing
'''
    )

    write(
        "generator/core/exceptions.py",
'''
class GeneratorError(Exception):
    pass

class ValidationError(GeneratorError):
    pass

class BuilderError(GeneratorError):
    pass
'''
    )

    write(
        "generator/build.py",
'''
from generator.core.engine import GeneratorEngine
from generator.core.validator import Validator

missing = Validator().validate()

if missing:
    print("Missing files:")
    for m in missing:
        print(" -", m)
    raise SystemExit(1)

GeneratorEngine().run()
'''
    )

    print("Sprint007 Complete")

if __name__ == "__main__":

    if len(sys.argv) < 2:
        raise SystemExit

    if sys.argv[1] == "sprint007":
        sprint007()
