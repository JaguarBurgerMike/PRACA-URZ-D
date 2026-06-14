import requests

url = "https://bip.malopolska.pl/umbochnia,m,276530,nabor-na-stanowiska-urzednicze-konkursy.html"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print("STATUS:", r.status_code)
print()
print(r.text[:5000])
