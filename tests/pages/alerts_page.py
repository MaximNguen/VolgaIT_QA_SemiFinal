from pages.base_page import BasePage
from utils.elements import *

from selenium.webdriver.support.wait import WebDriverWait
import allure

class AlertsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def alert1_click(self):
        alert = self.find(ALERT1[0], ALERT1[1])
        self.scroll(alert)
        with allure.step('Нажитие кнопки для вызова первого Alert'):
            return alert.click()

    def get_alert1_text(self):
        alert = self.browser.switch_to.alert
        with allure.step("Получение текста из Alert 1"):
            return alert.text

    def accept_alert1_text(self):
        alert = self.browser.switch_to.alert
        with allure.step("Подтвердить OK у Alert 1"):
            alert.accept()

    def alert2_click(self):
        alert = self.find(ALERT2[0], ALERT2[1])
        self.scroll(alert)
        with allure.step("Нажатие кнопки для вызова Alert 2"):
            return alert.click()

    def accept_alert2_text(self):
        alert = self.browser.switch_to.alert
        with allure.step("Подтвердить OK у Alert 2"):
            alert.accept()

    def dismiss_alert2(self):
        alert = self.browser.switch_to.alert
        with allure.step("Отменить Cancel у Alert 2"):
            alert.dismiss()

    def get_text_after_alert2(self):
        text1 = self.find(RESULTTEXT[0], RESULTTEXT[1])
        self.scroll(text1)
        with allure.step("Получить текст после нажатия Alert 2"):
            return text1.text

    def alert3_click(self):
        alert = self.find(ALERT3[0], ALERT3[1])
        self.scroll(alert)
        with allure.step("Нажатие кнопки для вызова Alert 3"):
            return alert.click()

    def send_text_to_alert3(self, name):
        wait = WebDriverWait(self.browser, 10)
        alert = wait.until(lambda browser: browser.switch_to.alert)
        with allure.step("Отправить текст в Alert 3"):
            alert.send_keys(name)

    def accept_alert3(self):
        wait = WebDriverWait(self.browser, 10)
        alert = wait.until(lambda browser: browser.switch_to.alert)
        with allure.step("Подтвердить OK у Alert 3"):
            alert.accept()

    def dismiss_alert3(self):
        wait = WebDriverWait(self.browser, 10)
        alert = wait.until(lambda browser: browser.switch_to.alert)
        with allure.step("Отменить Cancel у Alert 3"):
            alert.dismiss()

    def get_text_after_alert3(self):
        text1 = self.find(RESULTTEXT1[0], RESULTTEXT1[1])
        self.scroll(text1)
        with allure.step("Получить текст после нажатия Alert 3"):
            return text1.text