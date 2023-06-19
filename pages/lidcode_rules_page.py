from playwright.sync_api import Page

from pages.base_page import BasePage
from page_factory.link import Link


class LidcodeRulesPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.contest = Link(page, locator='#back', name='contest')

    def click_back(self):
        self.contest.click()
