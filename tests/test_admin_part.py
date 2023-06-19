import pytest
import allure

from pages.lidcode_admin_login import LidcodeAdminLogin
from pages.admin_lidcode_contests import AdminLidcodeContests, AdminLidcodeContestView
from pages.admin_lidcode_materials import AdminLidcodeMaterials, AdminLidcodeMaterialView
from pages.admin_lidcode_organizers import AdminLidcodeOrganizers, AdminLidcodeOrganizerView
from pages.admin_lidcode_sponsors import AdminLidcodeSponsors, AdminLidcodeSponsorView
from pages.admin_lidcode_teams import AdminLidcodeTeams, AdminLidcodeTeamView
from pages.admin_lidcode_admins import AdminLidcodeAdmins, AdminLidcodeAdminView
from settings import BASE_URL
from time import sleep
from playwright.sync_api import expect
import re
from utils.fakers import random_link, random_string, random_number, random_datetime, random_email, random_phone, \
    random_course


@pytest.mark.admin
@allure.feature('Admin part')
@allure.story('Admin create objects')
class TestAdminPart:

    def test_login(self, lidcode_admin_login: LidcodeAdminLogin):
        lidcode_admin_login.visit(BASE_URL + 'admin')
        expect(lidcode_admin_login.page).not_to_have_url(re.compile(f'^{BASE_URL + "admin/"}'))
        lidcode_admin_login.fill_login('admin')
        lidcode_admin_login.fill_password('admin')
        lidcode_admin_login.send()
        sleep(5)
        expect(lidcode_admin_login.page).to_have_url(re.compile(f'^{BASE_URL + "admin/"}'))

    def test_logout(self, lidcode_admin_login_completed: AdminLidcodeContests,
                    lidcode_admin_login: LidcodeAdminLogin):
        lidcode_admin_login_completed.navbar.visit_logout()
        expect(lidcode_admin_login.login.get_locator()).to_be_visible()
        expect(lidcode_admin_login.password.get_locator()).to_be_visible()
        expect(lidcode_admin_login.authorization_button.get_locator()).to_be_visible()
        expect(lidcode_admin_login.authorization_button.get_locator()).to_have_value('Авторизоваться')

    def test_events_create(self, lidcode_admin_login_completed: AdminLidcodeContests,
                           admin_lidcode_contest_view: AdminLidcodeContestView,
                           admin_lidcode_clean_contest: None):
        lidcode_admin_login_completed.navbar.visit_contests()
        lidcode_admin_login_completed.press_add()
        title = random_string(10, 20)
        admin_lidcode_contest_view.fill_title(title)
        admin_lidcode_contest_view.set_status_public()
        max_teams = random_number()
        admin_lidcode_contest_view.fill_max_teams(max_teams)
        min_participants = random_number(1, 3)
        admin_lidcode_contest_view.fill_min_participants(min_participants)
        max_participants = random_number(3, 5)
        admin_lidcode_contest_view.fill_max_participants(max_participants)
        description = random_string(30, 50)
        admin_lidcode_contest_view.fill_description(description)
        rules = random_string(20, 30)
        admin_lidcode_contest_view.fill_rules(rules)
        datetimes = []
        for _ in range(5):
            datetimes.append(random_datetime())
        datetimes.sort()
        admin_lidcode_contest_view.fill_date_open(datetimes[0])
        admin_lidcode_contest_view.fill_date_close(datetimes[1])
        admin_lidcode_contest_view.fill_date_start(datetimes[2])
        admin_lidcode_contest_view.fill_date_end(datetimes[3])
        admin_lidcode_contest_view.fill_date_material(datetimes[4])
        admin_lidcode_contest_view.press_save()
        lidcode_admin_login_completed.visit_first_elem()
        expect(admin_lidcode_contest_view.title.get_locator()).to_have_value(title)
        expect(admin_lidcode_contest_view.status.get_locator()).to_have_text('Опубликованное')
        expect(admin_lidcode_contest_view.max_teams.get_locator()).to_have_value(str(max_teams))
        expect(admin_lidcode_contest_view.min_participants.get_locator()).to_have_value(str(min_participants))
        expect(admin_lidcode_contest_view.max_participants.get_locator()).to_have_value(str(max_participants))
        expect(admin_lidcode_contest_view.description.get_locator()).to_have_value(description)
        expect(admin_lidcode_contest_view.rules.get_locator()).to_have_value(rules)
        expect(admin_lidcode_contest_view.date_open.get_locator()).to_have_value(datetimes[0])
        expect(admin_lidcode_contest_view.date_close.get_locator()).to_have_value(datetimes[1])
        expect(admin_lidcode_contest_view.date_start.get_locator()).to_have_value(datetimes[2])
        expect(admin_lidcode_contest_view.date_end.get_locator()).to_have_value(datetimes[3])
        expect(admin_lidcode_contest_view.date_material.get_locator()).to_have_value(datetimes[4])
        admin_lidcode_contest_view.press_back()

    def test_sponsors_create(self, lidcode_admin_login_completed: AdminLidcodeContests,
                             admin_lidcode_sponsor_view: AdminLidcodeSponsorView,
                             admin_lidcode_clean_sponsor: None):
        lidcode_admin_login_completed.navbar.visit_sponsors()
        lidcode_admin_login_completed.press_add()
        title = random_string()
        admin_lidcode_sponsor_view.fill_title(title)
        link = random_link()
        admin_lidcode_sponsor_view.fill_link(link)
        admin_lidcode_sponsor_view.load_img_default('testimage.jpg')
        admin_lidcode_sponsor_view.load_img_vertical('testimage.jpg')
        admin_lidcode_sponsor_view.load_img_horizontal('testimage.jpg')
        admin_lidcode_sponsor_view.press_save()
        lidcode_admin_login_completed.visit_first_elem()
        expect(admin_lidcode_sponsor_view.title.get_locator()).to_have_value(title)
        expect(admin_lidcode_sponsor_view.link.get_locator()).to_have_value(link)
        assert admin_lidcode_sponsor_view.page.get_by_alt_text(re.compile('^logo$')).count() == 3
        admin_lidcode_sponsor_view.press_back()

    def test_organizers_create(self, lidcode_admin_login_completed: AdminLidcodeContests,
                               admin_lidcode_organizer_view: AdminLidcodeOrganizerView,
                               admin_lidcode_clean_organizer: None):
        lidcode_admin_login_completed.navbar.visit_organizers()
        lidcode_admin_login_completed.press_add()
        title = random_string()
        admin_lidcode_organizer_view.fill_title(title)
        link = random_link()
        admin_lidcode_organizer_view.fill_link(link)
        admin_lidcode_organizer_view.load_img_default('testimage.jpg')
        admin_lidcode_organizer_view.load_img_vertical('testimage.jpg')
        admin_lidcode_organizer_view.load_img_horizontal('testimage.jpg')
        admin_lidcode_organizer_view.press_save()
        lidcode_admin_login_completed.visit_first_elem()
        expect(admin_lidcode_organizer_view.title.get_locator()).to_have_value(title)
        expect(admin_lidcode_organizer_view.link.get_locator()).to_have_value(link)
        assert admin_lidcode_organizer_view.page.get_by_alt_text(re.compile('^logo$')).count() == 3
        admin_lidcode_organizer_view.press_back()

    def test_teams_create_solo(self, lidcode_admin_login_completed: AdminLidcodeContests,
                               admin_lidcode_team_view: AdminLidcodeTeamView,
                               admin_lidcode_clean_team: None):
        lidcode_admin_login_completed.navbar.visit_teams()
        lidcode_admin_login_completed.press_add()
        team_name = random_string()
        admin_lidcode_team_view.fill_team_name(team_name)
        name = random_string()
        admin_lidcode_team_view.fill_name(name, 0)
        email = random_email()
        admin_lidcode_team_view.fill_email(email, 0)
        phone = random_phone()
        admin_lidcode_team_view.fill_phone(phone, 0)
        organization = random_string()
        admin_lidcode_team_view.fill_organization(organization, 0)
        faculty = random_string()
        admin_lidcode_team_view.fill_faculty(faculty, 0)
        course = random_course()
        admin_lidcode_team_view.fill_course(course, 0)
        admin_lidcode_team_view.press_save()
        lidcode_admin_login_completed.visit_first_elem()
        expect(admin_lidcode_team_view.team_name.get_locator()).to_have_value(team_name)
        expect(admin_lidcode_team_view.name.get_locator(parnumber=0)).to_have_value(name)
        expect(admin_lidcode_team_view.email.get_locator(parnumber=0)).to_have_value(email)
        expect(admin_lidcode_team_view.phone.get_locator(parnumber=0)).to_have_value(phone)
        expect(admin_lidcode_team_view.organization.get_locator(parnumber=0)).to_have_value(organization)
        expect(admin_lidcode_team_view.faculty.get_locator(parnumber=0)).to_have_value(faculty)
        expect(admin_lidcode_team_view.course.get_locator(parnumber=0)).to_have_value(course)
        admin_lidcode_team_view.press_back()

    # TODO сделать для нескольких участников
    def test_teams_create_team(self, lidcode_admin_login_completed: AdminLidcodeContests,
                               admin_lidcode_team_view: AdminLidcodeTeamView,
                               admin_lidcode_clean_team: None):
        lidcode_admin_login_completed.navbar.visit_teams()
        lidcode_admin_login_completed.press_add()
        team_name = random_string()
        admin_lidcode_team_view.fill_team_name(team_name)
        name = random_string()
        admin_lidcode_team_view.fill_name(name, 0)
        email = random_email()
        admin_lidcode_team_view.fill_email(email, 0)
        phone = random_phone()
        admin_lidcode_team_view.fill_phone(phone, 0)
        organization = random_string()
        admin_lidcode_team_view.fill_organization(organization, 0)
        faculty = random_string()
        admin_lidcode_team_view.fill_faculty(faculty, 0)
        course = random_course()
        admin_lidcode_team_view.fill_course(course, 0)
        admin_lidcode_team_view.press_save()
        lidcode_admin_login_completed.visit_first_elem()
        expect(admin_lidcode_team_view.team_name.get_locator()).to_have_value(team_name)
        expect(admin_lidcode_team_view.name.get_locator(parnumber=0)).to_have_value(name)
        expect(admin_lidcode_team_view.email.get_locator(parnumber=0)).to_have_value(email)
        expect(admin_lidcode_team_view.phone.get_locator(parnumber=0)).to_have_value(phone)
        expect(admin_lidcode_team_view.organization.get_locator(parnumber=0)).to_have_value(organization)
        expect(admin_lidcode_team_view.faculty.get_locator(parnumber=0)).to_have_value(faculty)
        expect(admin_lidcode_team_view.course.get_locator(parnumber=0)).to_have_value(course)
        admin_lidcode_team_view.press_back()

    def test_materials_create(self, lidcode_admin_login_completed: AdminLidcodeContests,
                              admin_lidcode_material_view: AdminLidcodeMaterialView,
                              admin_lidcode_clean_material: None):
        lidcode_admin_login_completed.navbar.visit_materials()
        lidcode_admin_login_completed.press_add()
        name = random_string()
        admin_lidcode_material_view.fill_title(name)
        link = random_link()
        admin_lidcode_material_view.fill_link(link)
        admin_lidcode_material_view.press_save()
        lidcode_admin_login_completed.visit_first_elem()
        expect(admin_lidcode_material_view.title.get_locator()).to_have_value(name)
        expect(admin_lidcode_material_view.link.get_locator()).to_have_value(link)
        admin_lidcode_material_view.press_back()

    def test_users_create(self, lidcode_admin_login_completed: AdminLidcodeContests,
                          admin_lidcode_admin_view: AdminLidcodeAdminView,
                          admin_lidcode_clean_admin: None):
        lidcode_admin_login_completed.navbar.visit_admins()
        lidcode_admin_login_completed.press_add()
        login = random_string()
        admin_lidcode_admin_view.fill_login(login)
        password = random_string()
        admin_lidcode_admin_view.fill_password(password)
        admin_lidcode_admin_view.press_save()
        expect(lidcode_admin_login_completed.elem.get_locator_first()).to_have_text(login)
