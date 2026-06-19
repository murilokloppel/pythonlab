from src.crawlers.warmup import WarmupCrawler

if __name__ == "__main__":

    warmup = WarmupCrawler(headless=False)
    warmup.executar()
    warmup.fechar()