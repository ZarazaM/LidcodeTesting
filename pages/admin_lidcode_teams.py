from playwright.sync_api import Page

from pages.admin_base_page import AdminBasePage
from page_factory.checkbox import Checkbox
from page_factory.button import Button
from page_factory.link import Link
from page_factory.input import Input
from page_factory.list_item import ListItem


class AdminLidcodeTeams(AdminBasePage):
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


class AdminLidcodeTeamView(AdminBasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.back = Link(page, locator='#back', name='back')
        self.save = Button(page, locator='#save', name='save')

        self.state = Button(page, locator="[id$='status']", name='state')
        self.state_waiting = ListItem(page, locator='#status_item_1', name='state waiting')
        self.state_declined = ListItem(page, locator='#status_item_2', name='state declined')
        self.state_accepted = ListItem(page, locator='#status_item_3', name='state accepted')
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
        self.close = Button(page, locator='#close_{parnumber}', name='close button')

    def press_back(self):
        self.back.click()

    def press_save(self):
        self.save.click()

    def select_state_waiting(self):
        self.state.click()
        self.state_waiting.should_be_visible()
        self.state_waiting.click()

    def select_state_declined(self):
        self.state.click()
        self.state_declined.should_be_visible()
        self.state_declined.click()

    def select_state_accepted(self):
        self.state.click()
        self.state_accepted.should_be_visible()
        self.state_accepted.click()

    def check_many_members(self):
        self.many_members.should_be_visible()
        self.many_members.check()

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
