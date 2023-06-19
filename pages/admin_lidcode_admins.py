from playwright.sync_api import Page

from pages.admin_base_page import AdminBasePage
from page_factory.checkbox import Checkbox
from page_factory.button import Button
from page_factory.link import Link
from page_factory.input import Input
from page_factory.list_item import ListItem


class AdminLidcodeAdmins(AdminBasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.add = Link(page, locator='#add', name='add')
        self.delete = Button(page, locator='#remove', name='delete')
        # self.back =
        # self.next =
        self.check_all = Checkbox(page, locator='#all_check', name='check_all')
        self.check = Checkbox(page, locator="[id*='check_']", name='check')
        self.elem = Link(page, locator="[id*='elem_']", name='elem')

    def visit_first_elem(self):
        self.elem.click_first()

    def press_add(self):
        self.add.click()

    def press_delete(self):
        self.delete.click()

    def check_first(self, **kwargs):
        self.check.check_first(**kwargs)


class AdminLidcodeAdminView(AdminBasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.back = Link(page, locator='#back', name='back')
        self.save = Button(page, locator='#save', name='save')

        self.access = Button(page, locator="[id$='access']", name='access')
        self.access_default = ListItem(page, locator='#access_item_0', name='access without admin management')
        self.access_upgrade = ListItem(page, locator='#access_item_1', name='access to create basic admin')
        self.access_full = ListItem(page, locator='#accesss_item_2', name='full access')
        self.login = Input(page, locator='input#login', name='login')
        self.password = Input(page, locator='#password', name='password')

    def press_back(self):
        self.back.click()

    def press_save(self):
        self.save.click()

    def fill_login(self, value: str):
        self.login.should_be_visible()
        self.login.fill(value)

    def fill_password(self, value: str):
        self.password.should_be_visible()
        self.password.fill(value)

    def set_access_default(self):
        self.access.click()
        self.access_default.should_be_visible()
        self.access_default.click()

    def set_access_upgrade(self):
        self.access.click()
        self.access_upgrade.should_be_visible()
        self.access_upgrade.click()

    def set_access_full(self):
        self.access.click()
        self.access_full.should_be_visible()
        self.access_full.click()
