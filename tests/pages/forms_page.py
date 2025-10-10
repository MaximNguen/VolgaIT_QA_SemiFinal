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
        with allure.step("Находим поле для имени"):
            return name

    def nameInput_send(self, text):
        with allure.step("Отправляем текст в поле имени"):
            self.nameInput().send_keys(text)

    def passwordInput(self):
        password = self.find(PASSWORDINPUT[0], PASSWORDINPUT[1])
        self.scroll(password)
        with allure.step("Находим поле для пароля"):
            return password

    def passwordInput_send(self, text):
        with allure.step("Вставляем пароль в поле"):
            self.passwordInput().send_keys(text)

    def checkbox1(self):
        check1 = self.find(CHECKBOX1[0], CHECKBOX1[1])
        self.scroll(check1)
        with allure.step("Находим ЧекБокс1"):
            return check1

    def checkbox1_click(self):
        with allure.step("Нажимаем ЧекБокс1"):
            self.checkbox1().click()

    def checkbox2(self):
        check2 = self.find(CHECKBOX2[0], CHECKBOX2[1])
        self.scroll(check2)
        with allure.step("Находим ЧекБокс2"):
            return check2

    def checkbox2_click(self):
        with allure.step("Нажимаем ЧекБокс2"):
            self.checkbox1().click()

    def checkbox3(self):
        check3 = self.find(CHECKBOX3[0], CHECKBOX3[1])
        self.scroll(check3)
        with allure.step("Находим ЧекБокс3"):
            return check3

    def checkbox3_click(self):
        with allure.step("Нажимаем ЧекБокс3"):
            self.checkbox1().click()

    def checkbox4(self):
        check4 = self.find(CHECKBOX4[0], CHECKBOX4[1])
        self.scroll(check4)
        with allure.step("Находим ЧекБокс4"):
            return check4

    def checkbox4_click(self):
        with allure.step("Нажимаем ЧекБокс4"):
            self.checkbox1().click()

    def checkbox5(self):
        check5 = self.find(CHECKBOX5[0], CHECKBOX5[1])
        self.scroll(check5)
        with allure.step("Находим ЧекБокс5"):
            return check5

    def checkbox5_click(self):
        with allure.step("Нажимаем ЧекБокс5"):
            self.checkbox1().click()

    def checkbox6(self):
        check6 = self.find(CHECKBOX6[0], CHECKBOX6[1])
        self.scroll(check6)
        with allure.step("Находим ЧекБокс6"):
            return check6

    def checkbox6_click(self):
        with allure.step("Нажимаем ЧекБокс6"):
            self.checkbox1().click()

    def radio1(self):
        radio1 = self.find(RADIO1[0], RADIO1[1])
        self.scroll(radio1)
        with allure.step("Находим РадиоБокс"):
            return radio1

    def radio1_click(self):
        with allure.step("Нажимаем на РадиоБокс"):
            self.browser.execute_script('arguments[0].click()', self.radio1())

    def select(self):
        select = self.find(SELECT[0], SELECT[1])
        self.scroll(select)
        with allure.step("Находим список выбора"):
            return select

    def select_click(self):
        with allure.step("Выбираем 1 значение из списка"):
            return Select(self.select()).select_by_value("yes")

    def email(self):
        email1 = self.find(EMAILINPUT[0], EMAILINPUT[1])
        self.scroll(email1)
        with allure.step("Находим поле для Почты"):
            return email1

    def email_send(self, mail):
        with allure.step("Вводим почту"):
            self.email().send_keys(mail)

    def message(self):
        message = self.find(MESSAGE[0], MESSAGE[1])
        self.scroll(message)
        with allure.step("Находим поле для сообщения"):
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
        with allure.step("Ищем кнопку для подтверждения"):
            return submit

    def submit_click(self):
        with allure.step("Подтверждаем"):
            self.browser.execute_script('arguments[0].click()', self.submit())

    def check_state_alert(self):
        alert = self.browser.switch_to.alert
        with allure.step("Получаем текст из Alert после ввода форм"):
            return alert.text