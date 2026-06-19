import time
import random
from bs4 import BeautifulSoup
from src.crawlers.crawler_base import CrawlerBase
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError


class MercadoLivreCrawler(CrawlerBase):
    def __init__(self, headless=False, user_agent=None, page=None):
        super().__init__(headless=headless, user_agent=user_agent, page=page)

    def _espera_humana(self, min_seg=10, max_seg=20):
        time.sleep(random.uniform(min_seg, max_seg))

    def executar(self, lista_produtos):
        resultados_totais = []
        for produto in lista_produtos:
            try:
                busca = produto.strip()
                if not busca:
                    continue

                print(f"Buscando por: {busca}...")
                busca_url = f"https://lista.mercadolivre.com.br/{busca.replace(' ', '-')}"

                self.page.goto(busca_url, wait_until="load")
                self.ha.aceitar_cookies()

                try:
                    self.page.wait_for_selector('.ui-search-result', timeout=10000)
                except PlaywrightTimeoutError:
                    self.salvar_print_erro(f"erro_busca_{busca.replace(' ', '_')}")
                    print(f"Atenção: resultados não encontrados para '{busca}'.")
                    self._espera_humana(5, 8)
                    continue

                html_conteudo = self.page.content()
                soup = BeautifulSoup(html_conteudo, 'html.parser')
                item = soup.select_one('.ui-search-result')

                if item:
                    nome_el = item.select_one('.ui-search-item__title')
                    nome = nome_el.get_text(strip=True) if nome_el else "N/A"
                    preco_el = item.select_one('.price-tag-fraction')
                    preco = preco_el.get_text(strip=True) if preco_el else "N/A"
                    codigo = item.get('id') or "N/A"

                    resultados_totais.append({
                        "codigo": codigo,
                        "nome": nome,
                        "preco": preco
                    })
                    print(f"Sucesso: {nome} - R$ {preco}")
                else:
                    print(f"Nenhum item encontrado para '{busca}'.")

            except Exception as e:
                self.salvar_print_erro(f"erro_critico_{busca.replace(' ', '_')}")
                print(f"Erro ao processar '{produto}': {e}")

            self._espera_humana(12, 18)

        return resultados_totais