import requests
from src.config import HEADERS
from src.database import salvar_produto


session = requests.Session()
session.headers.update(HEADERS)


def buscar_produtos_por_termo(termo, quantidade=5):
    url = f"https://api.mercadolibre.com/sites/MLB/search"
    params = {"q": termo, "limit": quantidade}


    resposta = session.get(url, params=params)

    if resposta.status_code == 200:

        dados = resposta.json()

    else:
        print(f"Erro na busca: {resposta.status_code}")


if __name__ == "__main__":
    termo = input("Digite o nome do produto que deseja monitorar: ")
    buscar_produtos_por_termo(termo, quantidade=5)

    session.close()