from playwright.sync_api import Page

from pages.base_page import BasePage
from components.navigation.navbar import AdminNavbar


class AdminBasePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.navbar = AdminNavbar(page)
