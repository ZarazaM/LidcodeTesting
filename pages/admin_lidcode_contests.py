from playwright.sync_api import Page

from pages.admin_base_page import AdminBasePage
from page_factory.checkbox import Checkbox
from page_factory.button import Button
from page_factory.link import Link
from page_factory.input import Input
from page_factory.list_item import ListItem


class AdminLidcodeContests(AdminBasePage):
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


class AdminLidcodeContestView(AdminBasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.back = Link(page, locator='#back', name='back')
        self.save = Button(page, locator='#save', name='save')

        self.title = Input(page, locator='#title', name='title')
        self.status = Button(page, locator='#status', name='status')
        self.status_hidden = ListItem(page, locator='#status_item_1', name='status hidden')
        self.status_public = ListItem(page, locator='#status_item_2', name='status public')
        self.max_teams = Input(page, locator='#maxTeam', name='max teams')
        self.min_participants = Input(page, locator='#minParticipant', name='min participants')
        self.max_participants = Input(page, locator='#maxParticipant', name='max participants')
        self.img_default = Input(page, locator='#imgD', name='image default')
        self.img_vertical = Input(page, locator='#imgV', name='image vertical')
        self.img_horizontal = Input(page, locator='#imgH', name='image horizontal')

        self.description = Input(page, locator='#description', name='description')
        self.rules = Input(page, locator='#rules', name='rules')
        self.results = Input(page, locator='#file', name='results')

        self.date_open = Input(page, locator='#dateOpen', name='date open')
        self.date_close = Input(page, locator='#dateClose', name='date close')
        self.date_start = Input(page, locator='#dateStart', name='date start')
        self.date_end = Input(page, locator='#dateEnd', name='date end')
        self.date_material = Input(page, locator='#dateMaterial', name='date material')

        self.choose_teams = Button(page, locator='setTeam', name='choose team')
        self.team = ListItem(page, locator="[id*='setTeam_item_']", name='team')
        self.close_team = Button(page, locator="[id*='close_selTeam_item_']", name='close team')
        self.choose_materials = Button(page, locator='#selMat', name='choose material')
        self.material = ListItem(page, locator="[id*='selMat_item_']", name='material')
        self.close_material = Button(page, locator="[id*='close_selMat_item_']", name='close material')
        self.choose_sponsors = Button(page, locator='#selSpon', name='choose sponsor')
        self.sponsor = ListItem(page, locator="[id*='selSpon_item_']", name='sponsor')
        self.close_sponsor = Button(page, locator="[id*='close_selSpon_']", name='close sponsor')
        self.choose_organizers = Button(page, locator='#selOrg', name='choose organizers')
        self.organizer = ListItem(page, locator="[id*='selOrg_item_']", name='organizer')
        self.close_organizer = Button(page, locator="[id*='close_selOrg_item_']", name='close organizer')

    def press_back(self, **kwargs):
        self.back.should_be_visible(**kwargs)
        self.back.click(**kwargs)

    def press_save(self, **kwargs):
        self.save.should_be_visible(**kwargs)
        self.save.click(**kwargs)

    def fill_title(self, name: str, **kwargs):
        self.title.should_be_visible(**kwargs)
        self.title.fill(name, **kwargs)

    def fill_description(self, description: str, **kwargs):
        self.description.should_be_visible(**kwargs)
        self.description.fill(description, **kwargs)

    def fill_rules(self, rules: str, **kwargs):
        self.rules.should_be_visible(**kwargs)
        self.rules.fill(rules, **kwargs)

    def fill_date_open(self, date: str, **kwargs):
        self.date_open.should_be_visible(**kwargs)
        self.date_open.fill_date(date, **kwargs)

    def fill_date_close(self, date: str, **kwargs):
        self.date_close.should_be_visible(**kwargs)
        self.date_close.fill_date(date, **kwargs)

    def fill_date_start(self, date: str, **kwargs):
        self.date_start.should_be_visible(**kwargs)
        self.date_start.fill_date(date, **kwargs)

    def fill_date_end(self, date: str, **kwargs):
        self.date_end.should_be_visible(**kwargs)
        self.date_end.fill_date(date, **kwargs)

    def fill_date_material(self, date: str, **kwargs):
        self.date_material.should_be_visible(**kwargs)
        self.date_material.fill_date(date, **kwargs)

    def set_status_hidden(self, **kwargs):
        self.status.should_be_visible(**kwargs)
        self.status.click(**kwargs)
        self.status_hidden.should_be_visible(**kwargs)
        self.status_hidden.click(**kwargs)

    def set_status_public(self, **kwargs):
        self.status.should_be_visible(**kwargs)
        self.status.click(**kwargs)
        self.status_public.should_be_visible(**kwargs)
        self.status_public.click(**kwargs)

    def fill_max_teams(self, number: int, **kwargs):
        self.max_teams.should_be_visible(**kwargs)
        self.max_teams.fill(str(number), True, **kwargs)

    def fill_min_participants(self, number: int, **kwargs):
        self.min_participants.should_be_visible(**kwargs)
        self.min_participants.fill(str(number), True, **kwargs)

    def fill_max_participants(self, number: int, **kwargs):
        self.max_participants.should_be_visible(**kwargs)
        self.max_participants.fill(str(number), True, **kwargs)

    def load_img_default(self, path_to_file: str, **kwargs):
        self.img_default.add_file(path_to_file=path_to_file, **kwargs)

    def load_img_vertical(self, path_to_file: str, **kwargs):
        self.img_vertical.add_file(path_to_file=path_to_file, **kwargs)

    def load_img_horizontal(self, path_to_file: str, **kwargs):
        self.img_horizontal.add_file(path_to_file=path_to_file, **kwargs)

    def choose_team(self, number: int, **kwargs):
        self.choose_teams.should_be_visible(**kwargs)
        self.choose_teams.click(**kwargs)
        self.team.click_nth(number=number, **kwargs)

    def choose_material(self, number: int, **kwargs):
        self.choose_materials.should_be_visible(**kwargs)
        self.choose_materials.click(**kwargs)
        self.material.click_nth(number=number, **kwargs)

    def choose_sponsor(self, number: int, **kwargs):
        self.choose_sponsors.should_be_visible(**kwargs)
        self.choose_sponsors.click_first(**kwargs)
        self.sponsor.click_nth(number=number, **kwargs)

    def choose_organizer(self, number: int, **kwargs):
        self.choose_organizers.should_be_visible(**kwargs)
        self.choose_organizers.click(**kwargs)
        self.organizer.click_nth(number=number, **kwargs)

    def close_team(self, number: int, **kwargs):
        self.close_team.click_nth(number=number, **kwargs)

    def close_material(self, number: int, **kwargs):
        self.close_material.click_nth(number=number, **kwargs)

    def close_sponsor(self, number: int, **kwargs):
        self.close_sponsor.click_nth(number=number, **kwargs)

    def close_organizer(self, number: int, **kwargs):
        self.close_organizer.click_nth(number, **kwargs)
