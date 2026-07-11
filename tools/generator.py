from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def write(path: str, content: str):
    file = ROOT / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content.strip() + "\n", encoding="utf-8")

def sprint001():
    write(
        "generator/core/engine.py",
        """
class GeneratorEngine:

    def run(self):
        print("Generator Engine Started")
"""
    )

    write(
        "generator/build.py",
        """
from generator.core.engine import GeneratorEngine

GeneratorEngine().run()
"""
    )

    print("Sprint001 OK")

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("python tools/generator.py sprint001")
        return

    cmd = sys.argv[1].lower()

    if cmd == "sprint001":
        sprint001()
    else:
        print("Unknown sprint:", cmd)

if __name__ == "__main__":
    main()
