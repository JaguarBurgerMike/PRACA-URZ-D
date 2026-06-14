from playwright.sync_api import sync_playwright

URL = "https://bip.malopolska.pl/umbochnia,m,276530,nabor-na-stanowiska-urzednicze-konkursy.html"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle")

    print(page.title())

    print(page.locator("body").inner_text()[:5000])

    browser.close()
