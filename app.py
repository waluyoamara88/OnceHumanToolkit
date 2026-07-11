import sys

from app.scrapers.items import ItemScraper


def main():

    if len(sys.argv) < 3:
        print("Usage:")
        print("python app.py update items")
        return

    command = sys.argv[1]
    target = sys.argv[2]

    if command == "update" and target == "items":
        ItemScraper().run()


if __name__ == "__main__":
    main()