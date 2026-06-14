from playwright.sync_api import sync_playwright
import re
import json
import os

DB_FILE = "database.json"

with open("sites.json", "r", encoding="utf-8") as f:
    sites = json.load(f)

if os.path.exists(DB_FILE):
    with open(DB_FILE, "r", encoding="utf-8") as f:
        old = json.load(f)
else:
    old = {}

print("PLIK ISTNIEJE:", os.path.exists(DB_FILE))
print("LICZBA GMIN:", len(sites))

current = {}

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    for city, url in sites.items():

        print("\n" + "=" * 60)
        print("SPRAWDZAM:", city)
        print(url)

        try:

            page = browser.new_page()

            page.goto(url, wait_until="networkidle", timeout=60000)

            text = page.locator("body").inner_text()

            page.close()

            matches = re.findall(
                r"Przejdź do:\s*(.*?)\s+(Ogłoszony|Zakończony)\s+(\d{4}-\d{2}-\d{2})",
                text,
                re.DOTALL
            )

            print("ZNALEZIONO:", len(matches), "ogłoszeń")

            current[city] = {}

            for title, status, date in matches:

                key = title.strip()

                current[city][key] = {
                    "status": status,
                    "date": date
                }

        except Exception as e:

            print("BLAD:", str(e))

            current[city] = {}

    browser.close()

new_ads = []

for city in current:

    old_city = old.get(city, {})
    current_city = current[city]

    for title in current_city:

        if title not in old_city:

            new_ads.append((city, title))

if new_ads:

    print("\n")
    print("=" * 60)
    print("NOWE OGLOSZENIA")
    print("=" * 60)

    for city, title in new_ads:

        print()
        print("GMINA:", city)
        print(title)

else:

    print("\nBrak nowych ogłoszeń.")

with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(current, f, ensure_ascii=False, indent=2)
