from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd


produtos_pesquisa = [
    "monitor gamer lg ultragear",
    "mouse logitech g305",
    "ssd kingston nv3 1tb"
]

dados_produtos = []


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    for produto in produtos_pesquisa:

        url = (
            "https://lista.mercadolivre.com.br/"
            + produto.replace(" ", "-")
        )

        page.goto(url)

        html = page.content()

        soup = BeautifulSoup(html, "html.parser")

        cards = soup.find_all("div")

        print(f"\nPesquisando: {produto}")

        # Vamos descobrir a estrutura primeiro
        print(soup.title.text)

    browser.close()