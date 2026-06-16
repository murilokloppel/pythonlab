from src.monitores.monitor_base import MonitorBase

class MercadoLivreMonitor(MonitorBase):
    def __init__(self):
        super().__init__()

    def executar(self):
        print("Acessando Mercado Livre...")
        self.page.goto("https://www.mercadolivre.com.br")
