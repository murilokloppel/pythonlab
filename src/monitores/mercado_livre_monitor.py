import time
import random
from bs4 import BeautifulSoup
from src.monitores.monitor_base import MonitorBase


class MercadoLivreMonitor(MonitorBase):
    def __init__(self):
        super().__init__()
        # Mantive o seu User-Agent
        self.page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    def _espera_humana(self, min_seg=10, max_seg=20):
        time.sleep(random.uniform(min_seg, max_seg))

    def executar(self, lista_produtos):
        resultados_totais = []

        for produto in lista_produtos:
            print(f"Buscando por: {produto}...")
            busca_url = f"https://lista.mercadolivre.com.br/{produto.replace(' ', '-')}"
            self.page.goto(busca_url)

            # Aguarda a página carregar os resultados
            self.page.wait_for_selector('.ui-search-result')

            # Extração com BeautifulSoup
            html_conteudo = self.page.content()
            soup = BeautifulSoup(html_conteudo, 'html.parser')

            # Pega o primeiro item da busca
            item = soup.select_one('.ui-search-result')

            if item:
                nome = item.select_one('.ui-search-item__title').get_text(strip=True)
                # Tenta pegar o preço, tratando caso o elemento seja diferente
                preco_el = item.select_one('.price-tag-fraction')
                preco = preco_el.get_text(strip=True) if preco_el else "N/A"
                codigo = item.get('id')

                resultados_totais.append({
                    "codigo": codigo,
                    "nome": nome,
                    "preco": preco
                })
                print(f"Sucesso: {nome} - R$ {preco}")

            self._espera_humana(12, 18)

        return resultados_totais