from playwright.sync_api import Page

from pages.base_page import BasePage

from page_factory.link import Link


class LidcodeHomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # self.contest_button = Link(page, locator="//a[text()='Посмотреть подробнее']", name='contest buttons')
        # self.contest_name = Link(page, locator="//a[text()='Соревнование'", name='contest name')

        self.contest_button = Link(page, locator="[id*='button']", name='contest buttons')
        self.contest_name = Link(page, locator="[id*='link']", name='contest name')
        self.contest_img = Link(page, locator="[id*='img']", name='contest images')

    def visit_first_contest(self, **kwargs):
        self.contest_button.click_first(**kwargs)


