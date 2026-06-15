import requests

token = " "
item_id = "MLB4032077443"

url = f"https://api.mercadolibre.com/items/{item_id}"

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "data_monitor (Estudo de Integracao e Dados)"
}

resposta = requests.get(url, headers=headers)

print(f"Status Code: {resposta.status_code}")

if resposta.status_code == 200:
    dados = resposta.json()
    print(f"Produto: {dados['title']}")
    print(f"Preço: {dados['price']}")
    print(f"Quantidade disponível: {dados['available_quantity']}")
else:
    print(f"Erro ao acessar: {resposta.text}")