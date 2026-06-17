from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://www.mercadolivre.com.br")

    print(page.title())

    input("Pressione Enter para fechar...")

    browser.close()