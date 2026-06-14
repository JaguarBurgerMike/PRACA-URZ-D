from playwright.sync_api import sync_playwright
import json
import re
import os
import requests

DB_FILE = "database.json"

def send_discord(message):

    webhook = os.environ["DISCORD_WEBHOOK"]

    print("WEBHOOK:", "USTAWIONY" if webhook else "BRAK")

    response = requests.post(
        webhook,
        json={"content": message}
    )

    print("STATUS:", response.status_code)
    print("ODPOWIEDZ:", response.text)

message = "🧪 TEST DISCORDA\n\nJeżeli widzisz tę wiadomość, webhook działa poprawnie."

send_discord(message)
