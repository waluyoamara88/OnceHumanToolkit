import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="OnceHumanToolkit",
        description="Once Human Database Toolkit"
    )

    parser.add_argument(
        "command",
        choices=[
            "items",
            "weapons",
            "armor",
            "mods",
            "deviants",
            "recipes",
            "resources",
            "icons",
            "images",
            "build",
            "excel",
            "website",
            "update"
        ]
    )

    args = parser.parse_args()

    print(f"[RUN] {args.command}")

if __name__ == "__main__":
    main()