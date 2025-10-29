from pages.base_page import BasePage
from utils.elements import *
from utils.waitUtils import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

class EventsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def buttonCat(self):
        a = WaitUtils.wait(self.browser, (BUTTONCAT[0], BUTTONCAT[1]))
        btn = self.find(BUTTONCAT[0], BUTTONCAT[1])
        self.scroll(btn)
        with allure.step("Поиск кнопки Cat"):
            return btn

    def buttonCat_click(self):
        with allure.step("Нажатие кнопки Cat"):
            return self.buttonCat().click()

    def buttonDog(self):
        a = WaitUtils.wait(self.browser, (BUTTONDOG[0], BUTTONDOG[1]))
        btn = self.find(BUTTONDOG[0], BUTTONDOG[1])
        self.scroll(btn)
        with allure.step("Поиск кнопки Dog"):
            return btn

    def buttonDog_click(self):
        with allure.step("Нажатие кнопки Dog"):
            return self.buttonDog().click()

    def buttonPig(self):
        a = WaitUtils.wait(self.browser, (BUTTONPIG[0], BUTTONPIG[1]))
        btn = self.find(BUTTONPIG[0], BUTTONPIG[1])
        self.scroll(btn)
        with allure.step("Поиск кнопки Pig"):
            return btn

    def buttonPig_click(self):
        with allure.step("Нажатие кнопки Pig"):
            return self.buttonPig().click()

    def buttonCow(self):
        a = WaitUtils.wait(self.browser,(BUTTONCOW[0], BUTTONCOW[1]))
        btn = self.find(BUTTONCOW[0], BUTTONCOW[1])
        self.scroll(btn)
        with allure.step("Поиск кнопки Cow"):
            return btn

    def buttonCow_click(self):
        with allure.step("Нажатие кнопки Cow"):
            return self.buttonCow().click()

    def receive(self):
        a = WaitUtils.wait(self.browser, (RESULT[0], RESULT[1]))
        res = self.find(RESULT[0], RESULT[1])
        self.scroll(res)
        with allure.step("Получение текста нажатия кнопки"):
            return res.text