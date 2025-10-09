from pages.base_page import BasePage
from pages.elements import *
from selenium.webdriver.support.wait import WebDriverWait

class AlertsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
#alert1
    def alert1_click(self):
        alert = self.find(ALERT1[0], ALERT1[1])
        self.scroll(alert)
        return alert.click()

    def get_alert1_text(self):
        alert = self.browser.switch_to.alert
        return alert.text

    def accept_alert1_text(self):
        alert = self.browser.switch_to.alert
        alert.accept()
     # alert 2
    def alert2_click(self):
        alert = self.find(ALERT2[0], ALERT2[1])
        self.scroll(alert)
        return alert.click()

    def accept_alert2_text(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def dismiss_alert2(self):
        alert = self.browser.switch_to.alert
        alert.dismiss()

    def get_text_after_alert2(self):
        text1 = self.find(RESULTTEXT[0], RESULTTEXT[1])
        self.scroll(text1)
        return text1.text

    #alert3
    def alert3_click(self):
        alert = self.find(ALERT3[0], ALERT3[1])
        self.scroll(alert)
        return alert.click()

    def send_text_to_alert3(self, name):
        wait = WebDriverWait(self.browser, 10)
        alert = wait.until(lambda browser: browser.switch_to.alert)
        alert.send_keys(name)

    def accept_alert3(self):
        wait = WebDriverWait(self.browser, 10)
        alert = wait.until(lambda browser: browser.switch_to.alert)
        alert.accept()

    def dismiss_alert3(self):
        wait = WebDriverWait(self.browser, 10)
        alert = wait.until(lambda browser: browser.switch_to.alert)
        alert.dismiss()

    def get_text_after_alert3(self):
        text1 = self.find(RESULTTEXT1[0], RESULTTEXT1[1])
        self.scroll(text1)
        return text1.text
