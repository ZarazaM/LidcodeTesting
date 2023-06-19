from playwright.sync_api import Page

from page_factory.link import Link
from pages.base_page import BasePage


class LidcodeContestPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.register = Link(page, locator='#reg', name='register')
        self.rules = Link(page, locator='#open', name='rules')
        self.materials = Link(page, locator="[id*='mat']", name='materials')
        self.organizers = Link(page, locator="[id*='org']", name='organizers')
        self.sponsors = Link(page, locator="[id*='spon']", name='sponsors')

    def visit_rules(self):
        self.rules.should_be_visible()
        self.rules.click()

    def visit_register(self):
        self.register.should_be_visible()
        self.register.click()
