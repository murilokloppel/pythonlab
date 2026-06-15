import requests

url = "https://api.mercadolibre.com/sites/MLB/search"
params = {
    "q": "iPhone 15",
    "limit": 5
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
}

resposta = requests.get(url, params=params, headers=headers)

if resposta.status_code == 200:
    dados = resposta.json()

    for item in dados['results']:
        print(f"Produto: {item['title']}")
        print(f"Preço: {item['price']}")
        print("-" * 30)
else:
    print(f"Erro: {resposta.status_code}")