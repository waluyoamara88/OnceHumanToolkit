from generator.core.engine import GeneratorEngine
from generator.core.validator import Validator

missing = Validator().validate()

if missing:
    print("Missing files:")
    for m in missing:
        print(" -", m)
    raise SystemExit(1)

GeneratorEngine().run()
