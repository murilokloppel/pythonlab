import random
import time
from src.crawlers.crawler_base import CrawlerBase
from src.core.human_act import HumanAct


class WarmupCrawler(CrawlerBase):
    def __init__(self, page=None, headless=False):
        if page:
            self.page = page
            self.ha = HumanAct(self.page)
            self.context = self.page.context
            self.playwright = None
        else:
            super().__init__(headless=headless)

    def executar(self, sites=None):
        if not sites:
            sites = [
                "https://www.youtube.com/results?search_query=unboxing+eletronicos",
                "https://www.mercadolivre.com.br/ofertas",
                "https://www.techtudo.com.br",
                "https://www.buscape.com.br",
                "https://www.zoom.com.br",
                "https://www.linkedin.com"
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