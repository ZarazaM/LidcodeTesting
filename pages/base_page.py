import allure
from playwright.sync_api import Page, Response, expect

from components.navigation.navbar import Navbar
import re


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.navbar = Navbar(page)

    def visit(self, url: str) -> Response | None:
        with allure.step(f'Opening the url "{url}"'):
            return self.page.goto(url, wait_until='networkidle')

    def reload(self) -> Response | None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')

    def on_page(self, url: re.Pattern):
        with allure.step(f'Checking current page url match specified pattern'):
            expect(self.page).to_have_url(url)