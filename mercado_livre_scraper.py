import requests

item_id = "MLB4032077443"

url = f"https://api.mercadolibre.com/items/{item_id}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    print(f"Produto: {dados['title']}")
    print(f"Preço: {dados['price']}")
    print(f"Quantidade disponível: {dados['available_quantity']}")
else:
    print("Ops, verifique o ID do produto ou a conexão.")