import requests
import time


session = requests.Session()

url = "https://api.mercadolibre.com/sites/MLB/search"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126.0.0.0 Safari/537.36"}
params = {"q": "iPhone 15", "limit": 5}

time.sleep(2)

res = session.get(url, params=params, headers=headers)

if res.status_code == 200:
    for item in res.json()['results']:
        print(f"{item['title']} - R${item['price']}")
else:
    print(f"Erro {res.status_code}: {res.text}")