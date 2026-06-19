import random
import os
import time ,datetime
from playwright.sync_api import Page


class HumanAct:
    def __init__(self, page: Page):
        self.page = page

    def scroll(self):
        total_height = self.page.evaluate("document.body.scrollHeight")
        current_position = 0

        while current_position < total_height:
            scroll_step = random.randint(300, 800)
            self.page.mouse.wheel(0, scroll_step)
            current_position += scroll_step

            time.sleep(random.uniform(0.5, 2.5))

            if random.random() < 0.15:
                self.page.mouse.wheel(0, -random.randint(50, 200))

    def click(self, selector: str):
        elemento = self.page.locator(selector).first
        if elemento.is_visible():
            time.sleep(random.uniform(0.5, 1.2))
            elemento.hover()

            elemento.click()

    def aceitar_cookies(self, selector="button:has-text('Aceitar')"):
        try:
            cookie_banner = self.page.locator(selector).first
            if cookie_banner.is_visible(timeout=3000):
                cookie_banner.click()
                print("Banner de cookies aceito.")
        except Exception:
            print("Nenhum banner de cookies encontrado, prosseguindo...")

    def salvar_erro(self, nome="erro"):
        pasta = "assets"
        if not os.path.exists(pasta):
            os.makedirs(pasta)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        caminho = os.path.join(pasta, f"{nome}_{timestamp}.png")

        self.page.screenshot(path=caminho)
        print(f"Erro capturado e salvo em: {caminho}")