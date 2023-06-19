from playwright.sync_api import Page

from pages.admin_base_page import AdminBasePage
from page_factory.checkbox import Checkbox
from page_factory.button import Button
from page_factory.link import Link
from page_factory.input import Input


class AdminLidcodeOrganizers(AdminBasePage):
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


class AdminLidcodeOrganizerView(AdminBasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.back = Link(page, locator='#back', name='back')
        self.save = Button(page, locator='#save', name='save')

        self.title = Input(page, locator='#title', name='title')
        self.link = Input(page, locator='#link', name='link')
        self.img_default = Input(page, locator='#imgD', name='image default')
        self.img_vertical = Input(page, locator='#imgV', name='image vertical')
        self.img_horizontal = Input(page, locator='#imgH', name='image horizontal')

    def press_back(self):
        self.back.click()

    def press_save(self):
        self.save.click()

    def fill_title(self, value: str):
        self.title.fill(value)

    def fill_link(self, value: str):
        self.link.fill(value)

    def load_img_default(self, path_to_file: str, **kwargs):
        self.img_default.add_file(path_to_file=path_to_file, **kwargs)

    def load_img_vertical(self, path_to_file: str, **kwargs):
        self.img_vertical.add_file(path_to_file=path_to_file, **kwargs)

    def load_img_horizontal(self, path_to_file: str, **kwargs):
        self.img_horizontal.add_file(path_to_file=path_to_file, **kwargs)
