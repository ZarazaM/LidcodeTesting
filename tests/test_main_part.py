import pytest
import allure

from pages.lidcode_home_page import LidcodeHomePage
from pages.lidcode_rules_page import LidcodeRulesPage
from pages.lidcode_contest_page import LidcodeContestPage
from pages.lidcode_solo_register_page import LidcodeSoloRegisterPage
from pages.lidcode_team_register_page import LidcodeTeamRegisterPage
from pages.lidcode_archive_page import LidcodeArchivePage
from pages.lidcode_admin_login import LidcodeAdminLogin
from pages.admin_lidcode_contests import AdminLidcodeContests, AdminLidcodeContestView
from pages.admin_lidcode_materials import AdminLidcodeMaterials, AdminLidcodeMaterialView
from pages.admin_lidcode_organizers import AdminLidcodeOrganizers, AdminLidcodeOrganizerView
from pages.admin_lidcode_sponsors import AdminLidcodeSponsors, AdminLidcodeSponsorView
from pages.admin_lidcode_teams import AdminLidcodeTeams, AdminLidcodeTeamView
from settings import BASE_URL
from time import sleep
from playwright.sync_api import expect
import re


@pytest.mark.main
@allure.feature('Main part')
@allure.story('User interacts with interface')
class TestMainPart:

    def test_home_to_archive(self, lidcode_home_page: LidcodeHomePage,
                             lidcode_archive_page: LidcodeArchivePage):
        lidcode_home_page.visit(BASE_URL)
        lidcode_home_page.navbar.visit_archive()
        expect(lidcode_archive_page.page).to_have_url(BASE_URL+'basic')

    def test_home_to_contest(self, create_contest: None, lidcode_home_page: LidcodeHomePage,
                             lidcode_contest_page: LidcodeContestPage):
        lidcode_home_page.visit(BASE_URL)
        lidcode_home_page.visit_first_contest()
        expect(lidcode_contest_page.page).to_have_url(re.compile(f'^{BASE_URL+"event"}'))

    def test_archive_to_closed_contest(self, lidcode_archive_page: LidcodeArchivePage,
                                       lidcode_contest_page: LidcodeContestPage):
        lidcode_archive_page.visit(BASE_URL+'basic')
        lidcode_archive_page.visit_first_contest()
        expect(lidcode_contest_page.page).to_have_url(re.compile(f'^{BASE_URL+"event"}'))

    def test_open_and_close_rules(self, create_contest: None, lidcode_home_page: LidcodeHomePage,
                                  lidcode_contest_page: LidcodeContestPage,
                                  lidcode_rules_page: LidcodeRulesPage):
        lidcode_home_page.visit(BASE_URL)
        lidcode_home_page.visit_first_contest()
        lidcode_contest_page.visit_rules()
        expect(lidcode_rules_page.page).to_have_url(re.compile(f'^{BASE_URL+"rules"}'))
        lidcode_rules_page.click_back()
        expect(lidcode_contest_page.page).to_have_url(re.compile(f'^{BASE_URL+"event"}'))

    def test_visit_register(self, create_contest: None, lidcode_home_page: LidcodeHomePage,
                            lidcode_contest_page: LidcodeContestPage,
                            lidcode_solo_register_page: LidcodeSoloRegisterPage):
        lidcode_home_page.visit(BASE_URL)
        lidcode_home_page.visit_first_contest()
        lidcode_contest_page.visit_register()
        expect(lidcode_solo_register_page.page).to_have_url(re.compile(f'^{BASE_URL+"registration"}'))

    def test_fill_send_register(self, create_contest: None, lidcode_home_page: LidcodeHomePage,
                                lidcode_contest_page: LidcodeContestPage,
                                lidcode_solo_register_page: LidcodeSoloRegisterPage,
                                admin_lidcode_teams: AdminLidcodeTeams):
        lidcode_home_page.visit(BASE_URL)
        lidcode_home_page.visit_first_contest()
        lidcode_contest_page.visit_register()
        lidcode_solo_register_page.fill_name('some competitor')
        lidcode_solo_register_page.fill_phone('89998887766')
        lidcode_solo_register_page.fill_email('email@gmail.com')
        lidcode_solo_register_page.fill_course('4')
        lidcode_solo_register_page.fill_faculty('IVT')
        lidcode_solo_register_page.fill_organization('YarSU')
        lidcode_solo_register_page.send()
        sleep(1)
        expect(lidcode_solo_register_page.page.get_by_text('Заявка отправлена')).to_be_visible()
        # командное
        # lidcode_contest_page.visit_register()
        # lidcode_team_register_page.fill_team_name('super team')
        # lidcode_team_register_page.fill_name('Иван', 0)
        # lidcode_team_register_page.fill_phone('18441844184', 0)
        # lidcode_team_register_page.fill_email('ivan@gmail.com', 0)
        # lidcode_team_register_page.fill_course('4', 0)
        # lidcode_team_register_page.fill_faculty('IVT', 0)
        # lidcode_team_register_page.fill_organization('YarSU', 0)
        # lidcode_team_register_page.press_add_main()
        # lidcode_team_register_page.fill_name('Даниил', 1)
        # lidcode_team_register_page.fill_phone('89998887777', 1)
        # lidcode_team_register_page.fill_email('daniel@gmail.com', 1)
        # lidcode_team_register_page.fill_course('4', 1)
        # lidcode_team_register_page.fill_faculty('IVT', 1)
        # lidcode_team_register_page.fill_organization('YarSU', 1)
        # lidcode_team_register_page.press_add_main()
        # lidcode_team_register_page.fill_name('Леонид', 1)
        # lidcode_team_register_page.fill_phone('81112223333', 1)
        # lidcode_team_register_page.fill_email('leonid@gmail.com', 1)
        # lidcode_team_register_page.fill_course('4', 1)
        # lidcode_team_register_page.fill_faculty('IVT', 1)
        # lidcode_team_register_page.fill_organization('YarSU', 1)
        # lidcode_team_register_page.check_contact(0)
        # lidcode_team_register_page.check_coach(2)
        # lidcode_team_register_page.send()

