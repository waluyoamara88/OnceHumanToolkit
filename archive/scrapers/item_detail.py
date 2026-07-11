import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup


CACHE_DIR = Path("cache/html/items")
RAW_DIR = Path("data/raw/items")

CACHE_DIR.mkdir(parents=True, exist_ok=True)
RAW_DIR.mkdir(parents=True, exist_ok=True)


class ItemDetailScraper:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "OnceHumanToolkit/1.0"
        })

    def scrape(self, item):

        name = item["name"]
        url = item["url"]

        print(name)

        html = self.session.get(url, timeout=30).text

        filename = re.sub(r'[\\/:*?"<>|]', "_", name)

        (CACHE_DIR / f"{filename}.html").write_text(
            html,
            encoding="utf-8"
        )

        soup = BeautifulSoup(html, "lxml")

        data = {
            "name": name,
            "url": url,
            "description": "",
            "image": "",
            "infobox": {}
        }

        meta = soup.find("meta", attrs={"name": "description"})
        if meta:
            data["description"] = meta.get("content", "")

        img = soup.select_one(".pi-image-thumbnail")
        if img:
            data["image"] = img.get("src", "")

        for row in soup.select("section.pi-item"):
            label = row.select_one(".pi-data-label")
            value = row.select_one(".pi-data-value")

            if label and value:
                data["infobox"][label.get_text(strip=True)] = value.get_text(" ", strip=True)

        (RAW_DIR / f"{filename}.json").write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )