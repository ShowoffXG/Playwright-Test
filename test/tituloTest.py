import unittest
import asyncio
from playwright.sync_api import sync_playwright

class TituloTest(unittest.TestCase):
    async def test_titulo_should_be_true_when_web_title_are_equals(self):
        async with sync_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto("https://www.ucp.edu.ar/")
            titulo = await page.title()
            await browser.close()
        self.assertEqual("Universidad de la Cuenca del Plata -", titulo)

if __name__ == '__main__': unittest.main()