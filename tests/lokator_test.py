import os
from playwright.sync_api import sync_playwright, expect

def test_page_title():
    cesta = os.path.abspath("index.html")


    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file:///{cesta}")  # Načte lokální HTML soubor
        expect(page.locator('h1').first).to_be_visible()
        nadpis_1 = page.locator('h1').first
        nadpis_text = page.locator('text="Nadpis 1"')
        div_1 = page.locator('.container')
        odkaz = page.locator('a')

        expect(odkaz).to_be_visible()
        expect(nadpis_1).to_be_visible()
        expect(nadpis_text).to_be_visible()
        expect(div_1).to_be_visible()
        expect(nadpis_text).to_be_visible()
        odkaz.click()
        browser.close()
