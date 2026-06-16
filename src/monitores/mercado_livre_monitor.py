import time
import random
from src.monitores.monitor_base import MonitorBase


class MercadoLivreMonitor(MonitorBase):
    def __init__(self):
        super().__init__()
        self.page.set_extra_http_headers({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    def _espera_humana(self, min_seg=10, max_seg=20):
        tempo = random.uniform(min_seg, max_seg)
        time.sleep(tempo)

    def executar(self, lista_produtos):
        for produto in lista_produtos:
            busca_url = f"https://lista.mercadolivre.com.br/{produto.replace(' ', '-')}"
            self.page.goto(busca_url)

            self._espera_humana(12, 18)