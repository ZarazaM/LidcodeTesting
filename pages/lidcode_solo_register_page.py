from playwright.sync_api import Page

from pages.base_page import BasePage
from page_factory.input import Input
from page_factory.button import Button


class LidcodeSoloRegisterPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.name = Input(page, locator='#fullName', name='name')
        self.email = Input(page, locator='#email', name='email')
        self.phone = Input(page, locator='#phone', name='phone')
        self.organization = Input(page, locator='#organization', name='organization')
        self.faculty = Input(page, locator='#faculty', name='faculty')
        self.course = Input(page, locator='#course', name='course')
        self.send_button = Button(page, locator='#button', name='send button')

    def send(self):
        self.send_button.should_be_visible()

        self.send_button.hover()
        self.send_button.click()

    def fill_name(self, name: str):
        self.name.should_be_visible()
        self.name.fill(name, validate_value=True)

    def fill_email(self, email: str):
        self.email.should_be_visible()
        self.email.fill(email, validate_value=True)

    def fill_phone(self, phone: str):
        self.phone.should_be_visible()
        self.phone.fill(phone, validate_value=True)

    def fill_organization(self, organization):
        self.organization.should_be_visible()
        self.organization.fill(organization, validate_value=True)

    def fill_faculty(self, faculty):
        self.faculty.should_be_visible()
        self.faculty.fill(faculty, validate_value=True)

    def fill_course(self, course):
        self.course.should_be_visible()
        self.course.fill(course, validate_value=True)

    def on_register_page(self):
        self.send_button.should_be_visible()
        self.send_button.should_have_text('Отправить заявку на участие')
