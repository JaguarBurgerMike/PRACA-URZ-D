import requests
from bs4 import BeautifulSoup
import json
import os

print("=== NOWA WERSJA SKRYPTU ===")

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

        print("LINK:", title, "|", href)

    print("KONIEC TESTU")

with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(database, f, ensure_ascii=False, indent=2)
