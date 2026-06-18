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

        produtos = []

        for produto in dados["results"]:

            produto_info = {
                "titulo": produto["title"],
                "preco": produto["price"],
                "vendidos": produto["sold_quantity"],
                "link": produto["permalink"]
            }

            produtos.append(produto_info)

        return produtos

    else:
        print(f"Erro na busca: {resposta.status_code}")
        print(resposta.text)
        return []


if __name__ == "__main__":

    termo = input("Digite o nome do produto que deseja monitorar: ")

    produtos = buscar_produtos_por_termo(
        termo,
        quantidade=5
    )

    for produto in produtos:

        print("\n------------------------------")
        print(f"Título: {produto['titulo']}")
        print(f"Preço: R$ {produto['preco']}")
        print(f"Vendidos: {produto['vendidos']}")
        print(f"Link: {produto['link']}")

    session.close()