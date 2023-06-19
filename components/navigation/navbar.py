from playwright.sync_api import Page

from page_factory.button import Button
from page_factory.link import Link


class Navbar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.home_link = Link(page, locator='#logo', name='home')
        self.archive_link = Link(page, locator='#arxiv', name='archive')

    def visit_home(self):
        self.home_link.click()

    def visit_archive(self):
        self.archive_link.click()


class AdminNavbar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.home_link = Link(page, locator='#logo', name='home')
        self.logout_link = Link(page, locator='#logout', name='logout')
        self.contests = Link(page, locator='#event', name='contests')
        self.teams = Link(page, locator='#team', name='teams')
        self.materials = Link(page, locator='#material', name='materials')
        self.organizers = Link(page, locator='#organizators', name='organizers')
        self.sponsors = Link(page, locator='#sponsors', name='sponsors')

        self.admins = Link(page, locator='#admins', name='admins')

    def visit_home(self):
        self.home_link.click()

    def visit_logout(self):
        self.logout_link.click_first()

    def visit_contests(self):
        self.contests.click()

    def visit_teams(self):
        self.teams.click()

    def visit_materials(self):
        self.materials.click()

    def visit_organizers(self):
        self.organizers.click()

    def visit_sponsors(self):
        self.sponsors.click()

    def visit_admins(self):
        self.admins.click()
