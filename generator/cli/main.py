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
