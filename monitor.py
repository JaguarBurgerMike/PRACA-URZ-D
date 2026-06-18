from playwright.sync_api import sync_playwright
import json
import re
import os
import requests

DB_FILE = "database.json"

with open("sites.json", "r", encoding="utf-8") as f:
    sites = json.load(f)

if os.path.exists(DB_FILE):
    with open(DB_FILE, "r", encoding="utf-8") as f:
        old = json.load(f)
else:
    old = {}

current = {}
new_ads = []

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    for city, url in sites.items():

        print("\n" + "=" * 70)
        print("SPRAWDZAM:", city)
        print("=" * 70)

        current[city] = {}

        try:

            page = browser.new_page()

            page.goto(
                url,
                wait_until="networkidle",
                timeout=60000
            )

            text = page.locator("body").inner_text()

            page.close()

            matches = re.findall(
                r"Przejdź do:\s*(.*?)\s+(\d{4}-\d{2}-\d{2})",
                text,
                re.DOTALL
            )

            print("ZNALEZIONO:", len(matches), "pozycji")

            for title, date in matches:

                title = " ".join(title.split())

                if len(title) < 15:
                    continue

                current[city][title] = {
                    "date": date
                }

                if title not in old.get(city, {}):
                    new_ads.append((city, date, title, url))

        except Exception as e:

            print("BLAD:", city)
            print(e)

    browser.close()

print("\n")
print("=" * 70)

if new_ads:

    print("NOWE OGLOSZENIA")

    message = "🚨 NOWE OGŁOSZENIA 🚨\n\n"

    for city, date, title, url in new_ads:

        print()
        print(f"[{city}] {date}")
        print(title)

        message += (
            f"🏢 {city}\n"
            f"📅 {date}\n"
            f"📄 {title}\n"
            f"🔗 {url}\n\n"
        )

    response = requests.post(
        os.environ["DISCORD_WEBHOOK"],
        json={"content": message}
    )

    print("STATUS:", response.status_code)

else:

    print("BRAK NOWYCH OGLOSZEN")

print("=" * 70)

with open(DB_FILE, "w", encoding="utf-8") as f:
    json.dump(
        current,
        f,
        ensure_ascii=False,
        indent=2
    )
