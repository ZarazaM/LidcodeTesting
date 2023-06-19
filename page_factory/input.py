import allure
from playwright.sync_api import expect

from page_factory.component import Component
import re


class Input(Component):
    @property
    def type_of(self) -> str:
        return 'input'

    def fill(self, value: str, validate_value=False, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.fill(value)

            if validate_value:
                self.should_have_value(value, **kwargs)

    def should_have_value(self, value: str, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_value(value)

    def add_file(self, path_to_file: str, **kwargs):
        with allure.step(f'Adding file {path_to_file} to {self.type_of} "{self.name}"'):
            locator = self.locator.format(**kwargs)
            self.page.set_input_files(locator, path_to_file)

    def fill_date(self, value: str, **kwargs):
        """
        :param value: datetime-local value in format 'YYYY-MM-DDTHH:mm'
        :param kwargs: parameters of the locator
        :return: None
        """
        with allure.step(f'Fill {self.type_of} "{self.name}" with datetime "{value}"'):
            regex = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}')
            if regex.match(value):
                locator = self.get_locator(**kwargs)
                locator.fill(value)
            else:
                raise Exception('Wrong date format')
