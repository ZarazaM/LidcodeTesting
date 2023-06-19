from playwright.sync_api import Page, Locator

from pages.admin_base_page import AdminBasePage
from page_factory.checkbox import Checkbox
from page_factory.button import Button
from page_factory.link import Link
from page_factory.input import Input


class AdminLidcodeMaterials(AdminBasePage):
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


class AdminLidcodeMaterialView(AdminBasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.back = Link(page, locator='#back', name='back')
        self.save = Button(page, locator='#save', name='save')

        self.title = Input(page, locator='#title', name='title')
        self.link = Input(page, locator='#link', name='link')
        self.file = Input(page, locator='#file', name='file')

    def press_back(self, **kwargs):
        self.back.should_be_visible(**kwargs)
        self.back.click(**kwargs)

    def press_save(self, **kwargs):
        self.save.should_be_visible(**kwargs)
        self.save.click(**kwargs)

    def fill_title(self, name: str, **kwargs):
        self.title.should_be_visible(**kwargs)
        self.title.fill(name, **kwargs)

    def fill_link(self, link: str, **kwargs):
        self.link.should_be_visible(**kwargs)
        self.link.fill(link, **kwargs)

    def load_file(self, path_to_file):
        self.file.add_file(path_to_file=path_to_file)
