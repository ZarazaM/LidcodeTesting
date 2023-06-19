import pytest
from playwright.sync_api import Browser, Page, sync_playwright

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
from pages.admin_lidcode_admins import AdminLidcodeAdmins, AdminLidcodeAdminView
from settings import BASE_URL
from time import sleep
import datetime


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        yield chromium.new_page()


@pytest.fixture(scope='function')
def lidcode_home_page(chromium_page: Page) -> LidcodeHomePage:
    return LidcodeHomePage(chromium_page)


@pytest.fixture(scope='function')
def lidcode_contest_page(chromium_page: Page) -> LidcodeContestPage:
    return LidcodeContestPage(chromium_page)


@pytest.fixture(scope='function')
def lidcode_rules_page(chromium_page: Page) -> LidcodeRulesPage:
    return LidcodeRulesPage(chromium_page)


@pytest.fixture(scope='function')
def lidcode_solo_register_page(chromium_page: Page) -> LidcodeSoloRegisterPage:
    return LidcodeSoloRegisterPage(chromium_page)


@pytest.fixture(scope='function')
def lidcode_team_register_page(chromium_page: Page) -> LidcodeTeamRegisterPage:
    return LidcodeTeamRegisterPage(chromium_page)


@pytest.fixture(scope='function')
def lidcode_archive_page(chromium_page: Page) -> LidcodeArchivePage:
    return LidcodeArchivePage(chromium_page)


@pytest.fixture(scope='function')
def lidcode_admin_login(chromium_page: Page) -> LidcodeAdminLogin:
    return LidcodeAdminLogin(chromium_page)


@pytest.fixture(scope='function')
def lidcode_admin_login_completed(chromium_page: Page) -> AdminLidcodeContests:
    page = LidcodeAdminLogin(chromium_page)
    page.visit(BASE_URL+'admin')
    page.fill_login('admin')
    page.fill_password('admin')
    page.send()
    return AdminLidcodeContests(page.page)


@pytest.fixture(scope='function')
def admin_lidcode_contests(chromium_page: Page) -> AdminLidcodeContests:
    return AdminLidcodeContests(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_clean_contest(admin_lidcode_contests: AdminLidcodeContests) -> None:
    yield
    sleep(2)
    admin_lidcode_contests.check_first()
    admin_lidcode_contests.press_delete()
    sleep(2)


@pytest.fixture(scope='function')
def admin_lidcode_clean_sponsor(admin_lidcode_sponsors: AdminLidcodeSponsors) -> None:
    yield
    sleep(2)
    admin_lidcode_sponsors.check_first()
    admin_lidcode_sponsors.press_delete()
    sleep(2)


@pytest.fixture(scope='function')
def admin_lidcode_clean_organizer(admin_lidcode_organizers: AdminLidcodeOrganizers) -> None:
    yield
    sleep(2)
    admin_lidcode_organizers.check_first()
    admin_lidcode_organizers.press_delete()
    sleep(2)


@pytest.fixture(scope='function')
def admin_lidcode_clean_team(admin_lidcode_teams: AdminLidcodeTeams) -> None:
    yield
    sleep(2)
    admin_lidcode_teams.check_first()
    admin_lidcode_teams.press_delete()
    sleep(2)


@pytest.fixture(scope='function')
def admin_lidcode_clean_material(admin_lidcode_materials: AdminLidcodeMaterials) -> None:
    yield
    sleep(2)
    admin_lidcode_materials.check_first()
    admin_lidcode_materials.press_delete()
    sleep(2)


@pytest.fixture(scope='function')
def admin_lidcode_admins(chromium_page: Page) -> AdminLidcodeAdmins:
    return AdminLidcodeAdmins(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_admin_view(chromium_page: Page) -> AdminLidcodeAdminView:
    return AdminLidcodeAdminView(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_clean_admin(admin_lidcode_admins: AdminLidcodeAdmins) -> None:
    yield
    sleep(2)
    admin_lidcode_admins.check_first()
    admin_lidcode_admins.press_delete()
    sleep(2)


@pytest.fixture(scope='function')
def admin_lidcode_materials(chromium_page: Page) -> AdminLidcodeMaterials:
    return AdminLidcodeMaterials(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_organizers(chromium_page: Page) -> AdminLidcodeOrganizers:
    return AdminLidcodeOrganizers(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_sponsors(chromium_page: Page) -> AdminLidcodeSponsors:
    return AdminLidcodeSponsors(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_teams(chromium_page: Page) -> AdminLidcodeTeams:
    return AdminLidcodeTeams(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_contest_view(chromium_page: Page) -> AdminLidcodeContestView:
    return AdminLidcodeContestView(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_material_view(chromium_page: Page) -> AdminLidcodeMaterialView:
    return AdminLidcodeMaterialView(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_organizer_view(chromium_page: Page) -> AdminLidcodeOrganizerView:
    return AdminLidcodeOrganizerView(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_sponsor_view(chromium_page: Page) -> AdminLidcodeSponsorView:
    return AdminLidcodeSponsorView(chromium_page)


@pytest.fixture(scope='function')
def admin_lidcode_team_view(chromium_page: Page) -> AdminLidcodeTeamView:
    return AdminLidcodeTeamView(chromium_page)


@pytest.fixture(scope='function')
def create_contest(lidcode_admin_login_completed: AdminLidcodeContests,
                   admin_lidcode_contest_view: AdminLidcodeContestView) -> None:
    lidcode_admin_login_completed.press_add()
    admin_lidcode_contest_view.fill_title('Test competition')
    admin_lidcode_contest_view.set_status_public()
    admin_lidcode_contest_view.fill_max_teams(5)
    admin_lidcode_contest_view.fill_min_participants(1)
    admin_lidcode_contest_view.fill_max_participants(1)
    admin_lidcode_contest_view.fill_description('desctiption of competition')
    admin_lidcode_contest_view.fill_rules('rules of competition')
    admin_lidcode_contest_view.fill_date_open((datetime.datetime.today() - datetime.timedelta(5)).replace(microsecond=0).isoformat('T', timespec='minutes'))
    admin_lidcode_contest_view.fill_date_close((datetime.datetime.today() + datetime.timedelta(1)).replace(microsecond=0).isoformat('T', timespec='minutes'))
    admin_lidcode_contest_view.fill_date_start((datetime.datetime.today() + datetime.timedelta(2)).replace(microsecond=0).isoformat('T', timespec='minutes'))
    admin_lidcode_contest_view.fill_date_end((datetime.datetime.today() + datetime.timedelta(3)).replace(microsecond=0).isoformat('T', timespec='minutes'))
    admin_lidcode_contest_view.fill_date_material((datetime.datetime.today() + datetime.timedelta(4)).replace(microsecond=0).isoformat('T', timespec='minutes'))
    admin_lidcode_contest_view.press_save()
    sleep(3)

    yield

    lidcode_admin_login_completed.visit(BASE_URL+'admin/event')
    lidcode_admin_login_completed.check_first()
    lidcode_admin_login_completed.press_delete()
    sleep(3)



