import requests
from bs4 import BeautifulSoup
import json
import os

DB_FILE = "database.json"

with open("sites.json", "r", encoding="utf-8") as f:
    sites = json.load(f)

if os.path.exists(DB_FILE):
    with open(DB_FILE, "r", encoding="utf-8") as f:
        database = json.load(f)
else:
    database = {}

for name, url in sites.items():

    print(f"\nSprawdzam: {name}")

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=20
    )

    soup = BeautifulSoup(r.text, "html.parser")

    current = {}

for a in soup.find_all("a", href=True):

    href = a["href"]
    title = a.get_text(" ", strip=True)

    if href.startswith("#"):
        continue

    if len(title) < 20:
        continue

    current[href] = title

    previous = database.get(name, {})

    new_items = []

    for href, title in current.items():
        if href not in previous:
            new_items.append((title, href))

    if new_items:
        print("\nNOWE WPISY:")

        for title, href in new_items:
            print(title)
            print(href)
            print()

    else:
        print("Brak nowych wpisów.")

    database[name] = current

with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(database, f, ensure_ascii=False, indent=2)
