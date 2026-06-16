from playwright.sync_api import sync_playwright

class MonitorBase:
    def __init__(self):
        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def iniciar(self):
        if self.playwright is None:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=self.headless)
            self.page = self.browser.new_page()

    def executar(self):
        raise NotImplementedError("As subclasses devem implementar o método 'executar'")

    def fechar(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()