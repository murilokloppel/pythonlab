import random
import time
from src.crawlers.crawler_base import CrawlerBase


class WarmupCrawler(CrawlerBase):
    def __init__(self, page=None, headless=False):
        super().__init__(headless=headless, page=page)

    def executar(self, sites=None):
        if not sites:
            sites = [
                "https://g1.globo.com",
                "https://www.uol.com.br",
                "https://www.estadao.com.br",
                "https://pt.wikipedia.org/wiki/Especial:Página_aleatória",
                "https://www.cnnbrasil.com.br"
            ]

        random.shuffle(sites)

        for url in sites:
            try:
                print(f"Aquecendo perfil em: {url}")
                self.page.goto(url, wait_until="load", timeout=30000)
                time.sleep(2)
                self.ha.scroll()
                time.sleep(random.uniform(3, 6))
            except Exception as e:
                print(f"Erro em {url}: {e}")
                self.salvar_print_erro(f"erro_warmup_{url.split('//')[-1]}")