from playwright.sync_api import sync_playwright
import json

with open("sites.json", "r", encoding="utf-8") as f:
    sites = json.load(f)

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    for city, url in sites.items():

        print("\n" + "=" * 80)
        print("SPRAWDZAM:", city)
        print("=" * 80)

        try:

            page = browser.new_page()

            page.goto(url, wait_until="networkidle", timeout=60000)

            text = page.locator("body").inner_text()

            print(text[:3000])

            page.close()

        except Exception as e:

            print("BLAD:", str(e))

    browser.close()
