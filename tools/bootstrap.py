from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

folders = [
    "app",
    "app/core",
    "app/models",
    "app/utils",
    "app/scrapers",
    "app/downloaders",
    "app/builders",
    "app/calculators",
    "app/planner",
    "app/website",

    "assets/icons",
    "assets/images",
    "assets/maps",
    "assets/ui",

    "cache/html",
    "cache/json",

    "logs",

    "data/raw/items",
    "data/raw/weapons",
    "data/raw/armor",
    "data/raw/deviants",
    "data/raw/mods",
    "data/raw/resources",
    "data/raw/recipes",

    "data/processed",

    "data/export/json",
    "data/export/excel",
    "data/export/website",

    "tests"
]

files = [
    "app.py",

    "requirements.txt",
    "README.md",
    ".gitignore",

    "app/__init__.py",

    "app/core/__init__.py",
    "app/core/config.py",
    "app/core/logger.py",
    "app/core/http.py",
    "app/core/cache.py",
    "app/core/constants.py",

    "app/utils/__init__.py",
    "app/utils/filesystem.py",
    "app/utils/helpers.py",

    "app/models/__init__.py",
    "app/models/item.py",

    "app/scrapers/__init__.py",
    "app/scrapers/base.py",
    "app/scrapers/items.py",
    "app/scrapers/weapons.py",
    "app/scrapers/armor.py",
    "app/scrapers/deviants.py",
    "app/scrapers/resources.py",
    "app/scrapers/recipes.py",

    "app/downloaders/__init__.py",
    "app/downloaders/icons.py",
    "app/downloaders/images.py",

    "app/builders/__init__.py",
    "app/builders/database.py",
    "app/builders/wiki.py",
    "app/builders/excel.py",

    "app/calculators/__init__.py",
    "app/calculators/resource.py",
    "app/calculators/weapon.py",

    "app/planner/__init__.py",
    "app/planner/territory.py",
    "app/planner/thermal.py",

    "app/website/__init__.py",
    "app/website/generator.py"
]

for folder in folders:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)

for file in files:
    path = ROOT / file
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text("", encoding="utf-8")

print("=" * 50)
print(" Once Human Toolkit Bootstrap Complete ")
print("=" * 50)
print()
print("Folders :", len(folders))
print("Files   :", len(files))