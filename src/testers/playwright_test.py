from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir=".playwright_profile",
        headless=False
    )

    page = context.new_page()

    page.goto("https://www.mercadolivre.com.br")

    input("Pressione ENTER para fechar...")

    context.close()