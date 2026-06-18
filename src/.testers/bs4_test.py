from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

produto_pesquisa = "iphone 16"

dados_produtos = []

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    url = (
        "https://lista.mercadolivre.com.br/"
        + produto_pesquisa.replace(" ", "-")
    )

    page.goto(url)

    page.wait_for_timeout(3000)

    html = page.content()

    browser.close()

soup = BeautifulSoup(html, "html.parser")

with open("pagina_ml.html", "w", encoding="utf-8") as arquivo:
    arquivo.write(html)

print("HTML salvo com sucesso.")