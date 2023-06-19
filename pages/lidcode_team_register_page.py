from playwright.sync_api import Page

from pages.base_page import BasePage
from page_factory.input import Input
from page_factory.button import Button
from page_factory.checkbox import Checkbox


class LidcodeTeamRegisterPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.team_name = Input(page, locator='#name', name='team name')
        self.many_members = Checkbox(page, locator='#scales', name='many members')
        self.contact = Checkbox(page, locator="[id*='[{parnumber}].contact']", name='contact person')
        self.coach = Checkbox(page, locator="[id*='[{parnumber}].coach']", name='coach')
        self.name = Input(page, locator="[id*='[{parnumber}].name']", name='name')
        self.email = Input(page, locator="[id*='[{parnumber}].emailAdress']", name='email')
        self.phone = Input(page, locator="[id*='[{parnumber}].phoneNumber']", name='phone')
        self.organization = Input(page, locator="[id*='[{parnumber}].organization']", name='organization')
        self.faculty = Input(page, locator="[id*='[{parnumber}].universityFaculty']", name='faculty')
        self.course = Input(page, locator="[id*='[{parnumber}].universityCourse']", name='course')
        self.add_main = Button(page, locator="[id*='add_main']", name='add main')
        self.add_reserve = Button(page, locator="[id*='add_reserve']", name='add reserve')
        self.send_button = Button(page, locator="[id*='button']", name='send button')
        self.close = Button(page, locator='#close_{parnumber}', name='close button')

    def send(self):
        self.send_button.should_be_visible()

        self.send_button.hover()
        self.send_button.click()

    def fill_team_name(self, team_name: str):
        self.team_name.should_be_visible()
        self.team_name.fill(team_name, validate_value=True)

    def fill_name(self, name: str, form_number: int):
        self.name.should_be_visible(parnumber=form_number)
        self.name.fill(name, validate_value=True, parnumber=form_number)

    def fill_email(self, email: str, form_number: int):
        self.email.should_be_visible(parnumber=form_number)
        self.email.fill(email, validate_value=True, parnumber=form_number)

    def fill_phone(self, phone: str, form_number: int):
        self.phone.should_be_visible(parnumber=form_number)
        self.phone.fill(phone, validate_value=True, parnumber=form_number)

    def fill_organization(self, organization: str, form_number: int):
        self.organization.should_be_visible(parnumber=form_number)
        self.organization.fill(organization, validate_value=True, parnumber=form_number)

    def fill_faculty(self, faculty: str, form_number: int):
        self.faculty.should_be_visible(parnumber=form_number)
        self.faculty.fill(faculty, validate_value=True, parnumber=form_number)

    def fill_course(self, course: str, form_number: int):
        self.course.should_be_visible(parnumber=form_number)
        self.course.fill(course, validate_value=True, parnumber=form_number)

    def check_contact(self, form_number: int):
        self.contact.should_be_visible(parnumber=form_number)
        self.contact.check(parnumber=form_number)

    def check_coach(self, form_number: int):
        self.coach.should_be_visible(parnumber=form_number)
        self.coach.check(parnumber=form_number)

    def press_add_main(self):
        self.add_main.should_be_visible()
        self.add_main.click()

    def press_add_reserve(self):
        self.add_reserve.should_be_visible()
        self.add_reserve.click()

    def press_close(self, form_number: int):
        self.close.should_be_visible(parnumber=form_number)
        self.close.click(parnumber=form_number)
