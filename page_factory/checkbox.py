import allure

from page_factory.component import Component


class Checkbox(Component):
    @property
    def type_of(self) -> str:
        return 'checkbox'

    def check(self, **kwargs):
        with allure.step(f'Marking {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.check()

    def check_first(self, **kwargs):
        with allure.step(f'Marking {self.type_of} with name "{self.name}"'):
            locator = self.get_locator_first(**kwargs)
            locator.check()

    def check_last(self, **kwargs):
        with allure.step(f'Marking {self.type_of} with name "{self.name}"'):
            locator = self.get_locator_last(**kwargs)
            locator.check()

    def check_nth(self, number: int, **kwargs):
        with allure.step(f'Marking {self.type_of} with name "{self.name}"'):
            locator = self.get_locator_nth(number=number, **kwargs)
            locator.check()
