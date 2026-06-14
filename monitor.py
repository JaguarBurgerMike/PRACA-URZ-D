from playwright.sync_api import sync_playwright
import re

URL = "https://bip.malopolska.pl/umbochnia,m,276530,nabor-na-stanowiska-urzednicze-konkursy.html"

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

print("\nZNALEZIONE OGŁOSZENIA:\n")

for title, status, date in matches:
    print(f"[{date}] [{status}]")
    print(title.strip())
    print("-" * 50)
