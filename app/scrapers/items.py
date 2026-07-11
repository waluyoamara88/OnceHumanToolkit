import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://once-human.fandom.com"
CATEGORY_URL = f"{BASE_URL}/wiki/Category:Item"

CACHE_DIR = Path("cache/html")
RAW_DIR = Path("data/raw/items")

CACHE_DIR.mkdir(parents=True, exist_ok=True)
RAW_DIR.mkdir(parents=True, exist_ok=True)


class ItemScraper:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "OnceHumanToolkit/1.0"
        })

    def download_category(self):
        r = self.session.get(CATEGORY_URL, timeout=30)
        r.raise_for_status()

        html = CACHE_DIR / "items_category.html"
        html.write_text(r.text, encoding="utf-8")

        return r.text

    def parse_items(self, html):

        soup = BeautifulSoup(html, "lxml")

        pages = []

        for a in soup.select("a.category-page__member-link"):

            name = a.get_text(strip=True)

            href = a.get("href")

            if href:
                pages.append({
                    "name": name,
                    "url": BASE_URL + href
                })

        return pages

    def save(self, items):

        out = RAW_DIR / "items.json"

        out.write_text(
            json.dumps(items, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

    def run(self):

        print("Downloading category...")

        html = self.download_category()

        print("Parsing...")

        items = self.parse_items(html)

        print(f"Found {len(items)} items")

        self.save(items)

        print("Done.")