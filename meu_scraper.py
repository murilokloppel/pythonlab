import requests
from bs4 import BeautifulSoup

url = "https://lojabrunamodas.com/?utm_source=chatgpt.com"
headers = {"User-Agent": "Mozilla/5.0"}

resposta = requests.get(url, headers=headers)
soup = BeautifulSoup(resposta.text, 'html.parser')

precos = soup.select('span.price.price--highlight')

for p in precos:
    print(p.text.strip())