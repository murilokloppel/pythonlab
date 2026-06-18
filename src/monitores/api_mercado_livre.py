import requests
from src.config import HEADERS

session = requests.Session()
session.headers.update(HEADERS)


def buscar_produtos_por_termo(termo, quantidade=5):
    url = "https://api.mercadolibre.com/sites/MLB/search"
    params = {
        "q": termo,
        "limit": quantidade
    }
    resposta = session.get(url, params=params)

    if resposta.status_code == 200:
        dados = resposta.json()

        for produto in dados["results"]:
            titulo = produto["title"]
            preco = produto["price"]
            link = produto["permalink"]

            print(f"Título: {titulo}")
            print(f"Preço: R$ {preco}")
            print(f"Link: {link}")
            print("-" * 50)

    else:
        print(f"Erro na busca: {resposta.status_code}")
        print(resposta.text)

if __name__ == "__main__":
    termo = input("Digite o nome do produto que deseja monitorar: ")

    buscar_produtos_por_termo(termo)
    session.close()