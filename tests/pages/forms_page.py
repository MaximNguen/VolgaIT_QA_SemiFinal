from pages.base_page import BasePage
from pages.elements import *

from selenium.webdriver.support.ui import WebDriverWait, Select
import allure

class FormsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def nameInput(self):
        name = self.find(NAMEINPUT[0], NAMEINPUT[1])
        self.scroll(name)
        return name

    def nameInput_send(self, text):
        self.nameInput().send_keys(text)

    def passwordInput(self):
        password = self.find(PASSWORDINPUT[0], PASSWORDINPUT[1])
        self.scroll(password)
        return password

    def passwordInput_send(self, text):
        self.passwordInput().send_keys(text)

    def checkbox1(self):
        check1 = self.find(CHECKBOX1[0], CHECKBOX1[1])
        self.scroll(check1)
        return check1

    def checkbox1_click(self):
        self.checkbox1().click()

    def checkbox2(self):
        check2 = self.find(CHECKBOX2[0], CHECKBOX2[1])
        self.scroll(check2)
        return check2

    def checkbox2_click(self):
        self.checkbox1().click()

    def checkbox3(self):
        check3 = self.find(CHECKBOX3[0], CHECKBOX3[1])
        self.scroll(check3)
        return check3

    def checkbox3_click(self):
        self.checkbox1().click()

    def checkbox4(self):
        check4 = self.find(CHECKBOX4[0], CHECKBOX4[1])
        self.scroll(check4)
        return check4

    def checkbox4_click(self):
        self.checkbox1().click()

    def checkbox5(self):
        check5 = self.find(CHECKBOX5[0], CHECKBOX5[1])
        self.scroll(check5)
        return check5

    def checkbox5_click(self):
        self.checkbox1().click()

    def checkbox6(self):
        check6 = self.find(CHECKBOX6[0], CHECKBOX6[1])
        self.scroll(check6)
        return check6

    def checkbox6_click(self):
        self.checkbox1().click()

    def radio1(self):
        radio1 = self.find(RADIO1[0], RADIO1[1])
        self.scroll(radio1)
        return radio1

    def radio1_click(self):
        self.browser.execute_script('arguments[0].click()', self.radio1())

    def select(self):
        select = self.find(SELECT[0], SELECT[1])
        self.scroll(select)
        return select

    def select_click(self):
        return Select(self.select()).select_by_value("yes")

    def email(self):
        email1 = self.find(EMAILINPUT[0], EMAILINPUT[1])
        self.scroll(email1)
        return email1

    def email_send(self, mail):
        self.email().send_keys(mail)

    def message(self):
        message = self.find(MESSAGE[0], MESSAGE[1])
        self.scroll(message)
        return message

    def message_send(self):
        lst = self.find_elements_texts(LIST[0], LIST[1])
        texts = [element.text for element in lst]
        texts = sorted(texts, key=lambda x: len(x))
        with allure.step("Вводим нужный текст в поле сообщений"):
            return self.message().send_keys(texts[-1])

    def submit(self):
        submit = self.find(SUBMIT[0], SUBMIT[1])
        self.scroll(submit)
        return submit

    def submit_click(self):
        self.browser.execute_script('arguments[0].click()', self.submit())

    def check_state_alert(self):
        alert = self.browser.switch_to.alert
        alert.text