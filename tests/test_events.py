from pages.click_events_page import EventsPage
from utils.expected_conditions import ExpectedTexts as EC

import allure
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
        text = self.event_page.receive()
        with allure.step("Нажимаем на кнопку и подтверждаем, что нам выпал нужный текст"):
            assert text == EC.CAT_TEXT, f"Ожидалось вывод текста {EC.CAT_TEXT}, но получили {text}"

    @allure.feature("Events")
    @allure.story("Нажатие кнопки Dog с выводом текста Woof!")
    def test_get_woof(self):
        self.event_page.buttonDog_click()
        text = self.event_page.receive()
        with allure.step("Нажимаем на кнопку и подтверждаем, что нам выпал нужный текст"):
            assert text == EC.DOG_TEXT, f"Ожидалось вывод текста {EC.DOG_TEXT}, но получили {text}"

    @allure.feature("Events")
    @allure.story("Нажатие кнопки Pig с выводом текста Oink!")
    def test_get_oink(self):
        self.event_page.buttonPig_click()
        text = self.event_page.receive()
        with allure.step("Нажимаем на кнопку и подтверждаем, что нам выпал нужный текст"):
            assert text == EC.PIG_TEXT, f"Ожидалось вывод текста {EC.PIG_TEXT}, но получили {text}"

    @allure.feature("Events")
    @allure.story("Нажатие кнопки Cow с выводом текста Moo!")
    def test_get_moo(self):
        self.event_page.buttonCow_click()
        text = self.event_page.receive()
        with allure.step("Нажимаем на кнопку и подтверждаем, что нам выпал нужный текст"):
            assert text == EC.COW_TEXT, f"Ожидалось вывод текста {EC.COW_TEXT}, но получили {text}"