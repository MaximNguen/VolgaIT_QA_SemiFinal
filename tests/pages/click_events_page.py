from pages.base_page import BasePage
from pages.elements import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class EventsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def buttonCat(self):
        btn = self.find(BUTTONCAT[0], BUTTONCAT[1])
        self.scroll(btn)
        return btn

    def buttonCat_click(self):
        return self.buttonCat().click()

    def buttonDog(self):
        btn = self.find(BUTTONDOG[0], BUTTONDOG[1])
        self.scroll(btn)
        return btn

    def buttonDog_click(self):
        return self.buttonDog().click()

    def buttonPig(self):
        btn = self.find(BUTTONPIG[0], BUTTONPIG[1])
        self.scroll(btn)
        return btn

    def buttonPig_click(self):
        return self.buttonPig().click()

    def buttonCow(self):
        btn = self.find(BUTTONCOW[0], BUTTONCOW[1])
        self.scroll(btn)
        return btn

    def buttonCow_click(self):
        return self.buttonCow().click()


    def wait(self):
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((RESULT[0], RESULT[1]))
        )

    def receive(self):
        a = self.wait()
        res = self.find(RESULT[0], RESULT[1])
        self.scroll(res)
        return res.text