from pages.base_page import BasePage
from pages.elements import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

class EventsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def buttonCat(self):
        btn = self.find(BUTTONCAT[0], BUTTONCAT[1])
        self.scroll(btn)
        with allure.step("Поиск кнопки Cat"):
            return btn

    def buttonCat_click(self):
        with allure.step("Нажатие кнопки Cat"):
            return self.buttonCat().click()

    def buttonDog(self):
        btn = self.find(BUTTONDOG[0], BUTTONDOG[1])
        self.scroll(btn)
        with allure.step("Поиск кнопки Dog"):
            return btn

    def buttonDog_click(self):
        with allure.step("Нажатие кнопки Dog"):
            return self.buttonDog().click()

    def buttonPig(self):
        btn = self.find(BUTTONPIG[0], BUTTONPIG[1])
        self.scroll(btn)
        with allure.step("Поиск кнопки Pig"):
            return btn

    def buttonPig_click(self):
        with allure.step("Нажатие кнопки Pig"):
            return self.buttonPig().click()

    def buttonCow(self):
        btn = self.find(BUTTONCOW[0], BUTTONCOW[1])
        self.scroll(btn)
        with allure.step("Поиск кнопки Cow"):
            return btn

    def buttonCow_click(self):
        with allure.step("Нажатие кнопки Cow"):
            return self.buttonCow().click()


    def wait(self):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((RESULT[0], RESULT[1]))
        )

    def receive(self):
        a = self.wait()
        res = self.find(RESULT[0], RESULT[1])
        self.scroll(res)
        with allure.step("Получение текста нажатия кнопки"):
            return res.text