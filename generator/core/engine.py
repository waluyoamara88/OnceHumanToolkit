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
