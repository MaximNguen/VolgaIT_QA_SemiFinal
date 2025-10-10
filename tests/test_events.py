import allure

from pages.click_events_page import EventsPage
import pytest

class TestEvents:
    @classmethod
    def setup_class(cls):
        print("\n============= Начало тестирования страницы с ивентами =============")

    @classmethod
    def teardown_class(cls):
        print("\n================= Конец тестов страницы ивентов =========")

    @pytest.fixture(autouse=True)
    def setup(self, browser, url="https://practice-automation.com/click-events/"):
        self.event_page = EventsPage(browser)
        self.event_page.open(url)
        yield self.event_page
        self.event_page.quit()

    @allure.feature("Events")
    @allure.story("Нажатие кнопки Cat с выводом текста Meow!")
    def test_get_meow(self):
        self.event_page.buttonCat_click()
        with allure.step("Нажимаем на кнопку и подтверждаем, что нам выпал нужный текст"):
            assert self.event_page.receive() == "Meow!"

    @allure.feature("Events")
    @allure.story("Нажатие кнопки Dog с выводом текста Woof!")
    def test_get_woof(self):
        self.event_page.buttonDog_click()
        with allure.step("Нажимаем на кнопку и подтверждаем, что нам выпал нужный текст"):
            assert self.event_page.receive() == "Woof!"

    @allure.feature("Events")
    @allure.story("Нажатие кнопки Pig с выводом текста Oink!")
    def test_get_oink(self):
        self.event_page.buttonPig_click()
        with allure.step("Нажимаем на кнопку и подтверждаем, что нам выпал нужный текст"):
            assert self.event_page.receive() == "Oink!"

    @allure.feature("Events")
    @allure.story("Нажатие кнопки Cow с выводом текста Moo!")
    def test_get_moo(self):
        self.event_page.buttonCow_click()
        with allure.step("Нажимаем на кнопку и подтверждаем, что нам выпал нужный текст"):
            assert self.event_page.receive() == "Moo!"