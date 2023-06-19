from playwright.sync_api import Page

from pages.base_page import BasePage
from page_factory.input import Input
from page_factory.button import Button


class LidcodeAdminLogin(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.login = Input(page, locator='#login', name='login')
        self.password = Input(page, locator='#password', name='password')
        self.authorization_button = Button(page, locator='#go', name='authorization button')

    def send(self):
        self.authorization_button.should_be_visible()

        self.authorization_button.hover()
        self.authorization_button.click()

    def fill_login(self, login: str):
        self.login.should_be_visible()
        self.login.fill(login, validate_value=True)

    def fill_password(self, password: str):
        self.password.should_be_visible()
        self.password.fill(password, validate_value=True)
