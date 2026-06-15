
from src.config import HEADERS
from src.database import inicializar_banco, salvar_produto
import requests

def buscar_e_salvar_produto(item_id):
    url = f"https://api.mercadolibre.com/items/{item_id}"

    resposta = requests.get(url, headers=HEADERS)

    if resposta.status_code == 200:
        dados = resposta.json()

        titulo = dados.get('title')
        preco = dados.get('price')

        print(f"Sucesso! Produto: {titulo} | Preço: R$ {preco}")

        salvar_produto(titulo, preco)
    else:
        print(f"Erro {resposta.status_code}: {resposta.text}")

if __name__ == "__main__":
    inicializar_banco()
    buscar_e_salvar_produto("MLB4032077443")