from src.database import inicializar_banco, salvar_produto

import requests
from bs4 import BeautifulSoup

url = "https://lojabrunamodas.com/?utm_source=chatgpt.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"}

resposta = requests.get(url, headers=headers)
soup = BeautifulSoup(resposta.text, 'html.parser')

precos = soup.select('span.price.price--highlight')

for p in precos:
    print(p.text.strip())

inicializar_banco()
salvar_produto(item['title'], item['price'])