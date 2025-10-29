import allure
import pytest

from utils.expected_conditions import ExpectedTexts as EC
from pages.alerts_page import AlertsPage

class TestAlertsPage:

    @classmethod
    def setup_class(cls):
        print("\n============= Начало тестирования страницы с алертами =============")

    @classmethod
    def teardown_class(cls):
        print("\n================= Конец тестов страницы алертов =========")

    @pytest.fixture(autouse=True)
    def setup(self, browser, url = "https://practice-automation.com/popups/"):
        self.alert_page = AlertsPage(browser)
        self.alert_page.open(url)
        yield self.alert_page
        self.alert_page.quit()

    @allure.feature("Alerts")
    @allure.story("Тест первого Alert")
    def test_alert1(self):
        self.alert_page.alert1_click()
        text = self.alert_page.get_alert1_text()
        self.alert_page.accept_alert1_text()
        with allure.step("Подтверждаем, что бы получаем верный текст после закрытия Alert 1"):
            assert text == EC.ALERT1_TEXT, f"Ожидалось вывод текста {EC.ALERT1_TEXT}, но получили {text}"

    @allure.feature("Alerts")
    @allure.story("Тест второго Alert (Успешный - нажатие OK)")
    def test_alert2_success(self):
        self.alert_page.alert2_click()
        self.alert_page.accept_alert2_text()
        text = self.alert_page.get_text_after_alert2()
        with allure.step("Подтверждаем, что после нажатия OK у нас выпало нужное предложение"):
            assert text == EC.ALERT2_SUCCESS_TEXT, f"Ожидалось вывод текста {EC.ALERT2_SUCCESS_TEXT}, но получили {text}"

    @allure.feature("Alerts")
    @allure.story("Тест второго Alert (Негативный - нажатие отмены)")
    def test_alert2_failure(self):
        self.alert_page.alert2_click()
        self.alert_page.dismiss_alert2()
        text = self.alert_page.get_text_after_alert2()
        with allure.step("Подтверждаем, что после нажатия Отмены у нас выпало нужное предложение"):
            assert text == EC.ALERT2_FAILURE_TEXT, f"Ожидалось вывод текста {EC.ALERT2_FAILURE_TEXT}, но получили {text}"

    @allure.feature("Alerts")
    @allure.story("Тест третьего Alert (Успешный - ввод текста и нажатие OK)")
    @pytest.mark.parametrize("name", ["Max"])
    def test_alert3_success(self, name):
        self.alert_page.alert3_click()
        self.alert_page.send_text_to_alert3(name)
        self.alert_page.accept_alert3()
        text = self.alert_page.get_text_after_alert3()
        with allure.step("Подтверждаем, что после ввода текста и нажатия OK у нас выпало нужное предложение"):
            assert text == f"{EC.ALERT3_SUCCESS_PREFIX}{name}!", f"Ожидалось вывод текста {EC.ALERT3_SUCCESS_PREFIX}{name}!, получили {text}"

    @allure.feature("Alerts")
    @allure.story("Тест третьего Alert (Негативный - не ввели текст и нажатие OK)")
    def test_alert3_failure_without_name(self):
        self.alert_page.alert3_click()
        self.alert_page.accept_alert3()
        text = self.alert_page.get_text_after_alert3()
        with allure.step("Подтверждаем, что после нажатия OK у нас выпало нужное предложение"):
            assert text == EC.ALERT3_FAILURE_TEXT, f"Ожидалось вывод текста {EC.ALERT3_FAILURE_TEXT}, но получили {text}"

    @allure.feature("Alerts")
    @allure.story("Тест второго Alert (Негативный - нажатие Отмены)")
    def test_alert3_failure(self):
        self.alert_page.alert3_click()
        self.alert_page.dismiss_alert3()
        text = self.alert_page.get_text_after_alert3()
        with allure.step("Подтверждаем, что после нажатия Отмены у нас выпало нужное предложение"):
            assert text == EC.ALERT3_FAILURE_TEXT, f"Ожидалось вывод текста {EC.ALERT3_FAILURE_TEXT}, но получили {text}"