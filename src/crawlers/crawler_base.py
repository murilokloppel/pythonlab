from playwright.sync_api import sync_playwright

STEALTH_JS = """
Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
Object.defineProperty(navigator, 'languages', { get: () => ['pt-BR','pt'] });
Object.defineProperty(navigator, 'plugins', { get: () => [1,2,3] });
window.chrome = window.chrome || { runtime: {} };
const _originalQuery = navigator.permissions && navigator.permissions.query;
if (_originalQuery) {
  navigator.permissions.query = function (parameters) {
    if (parameters && parameters.name === 'notifications') {
      return Promise.resolve({ state: Notification.permission });
    }
    return _originalQuery.apply(this, arguments);
  };
}
"""

class MonitorBase:
    def __init__(self, headless=False, user_agent=None):
        self.headless = headless
        self.user_agent = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context(
            user_agent=self.user_agent,
            locale="pt-BR",
            timezone_id="America/Sao_Paulo"
        )
        self.context.add_init_script(STEALTH_JS)
        self.page = self.context.new_page()

    def iniciar(self):
        if self.playwright is None:
            self.playwright = sync_playwright().start()
            self.browser = self.playwright.chromium.launch(headless=self.headless)
            self.context = self.browser.new_context(
                user_agent=self.user_agent,
                locale="pt-BR",
                timezone_id="America/Sao_Paulo"
            )
            self.context.add_init_script(STEALTH_JS)
            self.page = self.context.new_page()

    def executar(self, lista_produtos):
        raise NotImplementedError("As subclasses devem implementar o método 'executar'")

    def fechar(self):
        if getattr(self, "context", None):
            try:
                self.context.close()
            except Exception:
                pass
            self.context = None
        if getattr(self, "browser", None):
            try:
                self.browser.close()
            except Exception:
                pass
            self.browser = None
        if getattr(self, "playwright", None):
            try:
                self.playwright.stop()
            except Exception:
                pass
            self.playwright = None
