from pathlib import Path
from generator.core.engine import GeneratorEngine
GeneratorEngine(Path(__file__).resolve().parent.parent).run()
