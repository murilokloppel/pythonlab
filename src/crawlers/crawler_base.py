from playwright.sync_api import sync_playwright
import os
from datetime import datetime
from src.core.human_act import HumanAct

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


class CrawlerBase:
    def __init__(self, headless=False, user_agent=None, page=None):
        self.headless = headless
        self.user_agent = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(
            user_data_dir="browser_profile",
            headless=self.headless,
            user_agent=self.user_agent,
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
            args=["--start-maximized"]
        )

        self.context.add_init_script(STEALTH_JS)
        self.page = self.context.pages[0] if self.context.pages else self.context.new_page()
        self.ha = HumanAct(self.page)

    def executar(self, lista_produtos):
        raise NotImplementedError

    def salvar_print_erro(self, nome="erro"):
        pasta = "assets"
        if not os.path.exists(pasta):
            os.makedirs(pasta)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        caminho = os.path.join(pasta, f"{nome}_{timestamp}.png")
        self.page.screenshot(path=caminho)
        print(f"Print salvo em: {caminho}")

    def fechar(self):
        if self.context:
            try:
                self.context.close()
            except:
                pass
        if self.playwright is not None:
            try:
                self.playwright.stop()
            except:
                pass