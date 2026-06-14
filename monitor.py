from playwright.sync_api import sync_playwright
import re
import json
import os

URL = "https://bip.malopolska.pl/umbochnia,m,276530,nabor-na-stanowiska-urzednicze-konkursy.html"

print("PLIK ISTNIEJE:", os.path.exists(DB_FILE))

if os.path.exists(DB_FILE):
    with open(DB_FILE, "r", encoding="utf-8") as f:
        print("ZAWARTOSC BAZY:")
        print(f.read()[:500])

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    text = page.locator("body").inner_text()

    browser.close()

matches = re.findall(
    r"Przejdź do:\s*(.*?)\s+(Ogłoszony|Zakończony)\s+(\d{4}-\d{2}-\d{2})",
    text,
    re.DOTALL
)

current = {}

for title, status, date in matches:

    key = title.strip()

    current[key] = {
        "status": status,
        "date": date
    }

if os.path.exists(DB_FILE):

    with open(DB_FILE, "r", encoding="utf-8") as f:
        old = json.load(f)

else:
    old = {}

new_ads = []

for title in current:

    if title not in old:
        new_ads.append(title)

if new_ads:

    print("\nNOWE OGŁOSZENIA:\n")

    for ad in new_ads:
        print(ad)
        print()

else:

    print("Brak nowych ogłoszeń.")

with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(current, f, ensure_ascii=False, indent=2)
