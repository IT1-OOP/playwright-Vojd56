import os
from playwright.sync_api import sync_playwright, expect

def test_page_title():
    cesta = os.path.abspath("index.html")


    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file:///{cesta}")  # Načte lokální HTML soubor
        expect(page.locator('h1').first).to_be_visible()
        browser.close()
