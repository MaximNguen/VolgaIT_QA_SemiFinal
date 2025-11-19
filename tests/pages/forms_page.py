from tests.pages.base_page import BasePage
from tests.utils.elements import *
from tests.utils.waitUtils import WaitUtils as WU

from selenium.webdriver.support.ui import Select
import allure
import random as rd

from tests.utils.elements import FIRST_NAME, LAST_NAME, CHECKBOX1, COUNTRYLIST


class FormsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.wait = WU

    def first_name_find(self):
        name = self.find(FIRST_NAME[0], FIRST_NAME[1])
        self.scroll(name)
        with allure.step("Поиск поле для ввода имени"):
            return name

    def first_name_input(self, text):
        with allure.step("Ввод имени в поле"):
            self.first_name_find().send_keys(text)

    def last_name_find(self):
        name = self.find(LAST_NAME[0], LAST_NAME[1])
        self.scroll(name)
        with allure.step("Поиск поле для ввода фамилии"):
            return name

    def last_name_input(self, text):
        with allure.step("Ввод фамилии в поле"):
            self.last_name_find().send_keys(text)

    def radiobox1_find(self):
        checkbox = self.find(RADIO1[0], RADIO1[1])
        self.scroll(checkbox)
        with allure.step("Поиск первого Radio для нажатия"):
            return checkbox

    def radiobox1_click(self, text):
        with allure.step("Нажатие Radio первого"):
            self.radiobox1_find().click()

    def radiobox2_find(self):
        checkbox = self.find(RADIO2[0], RADIO2[1])
        self.scroll(checkbox)
        with allure.step("Поиск второго Radio для нажатия"):
            return checkbox

    def radiobox2_click(self, text):
        with allure.step("Нажатие второго Radio"):
            self.radiobox2_find().click()

    def radiobox3_find(self):
        checkbox = self.find(RADIO3[0], RADIO3[1])
        self.scroll(checkbox)
        with allure.step("Поиск третьего Radio для нажатия"):
            return checkbox

    def radiobox3_click(self, text):
        with allure.step("Нажатие третьего Radio"):
            self.radiobox3_find().click()

    def checkbox1_find(self):
        checkbox = self.find(CHECKBOX1[0], CHECKBOX1[1])
        self.scroll(checkbox)
        with allure.step('Поиск первого checkbox для нажатия'):
            return checkbox

    def checkbox1_click(self, text):
        with allure.step("Нажатие первого checkbox"):
            self.checkbox1_find().click()

    def checkbox2_find(self):
        checkbox = self.find(CHECKBOX2[0], CHECKBOX2[1])
        self.scroll(checkbox)
        with allure.step('Поиск второго checkbox для нажатия'):
            return checkbox

    def checkbox2_click(self, text):
        with allure.step("Нажатие второго checkbox"):
            self.checkbox2_find().click()

    def checkbox3_find(self):
        checkbox = self.find(CHECKBOX3[0], CHECKBOX3[1])
        self.scroll(checkbox)
        with allure.step('Поиск третьего checkbox для нажатия'):
            return checkbox

    def checkbox3_click(self, text):
        with allure.step("Нажатие третьего checkbox"):
            self.checkbox1_find().click()

    def country_list_find(self):
        lst = self.find(COUNTRYLIST[0], COUNTRYLIST[1])
        self.scroll(lst)
        with allure.step('Поиск списка стран'):
            return lst

    def country_list_click(self, text):
        with allure.step("Выбор любой страны"):
            Select(self.country_list_find()).select_by_index(rd.randint(0, 1))

    def month_list_find(self):
        lst = self.find(MONTHLIST[0], MONTHLIST[1])
        self.scroll(lst)
        with allure.step("Поиск списка месяцев"):
            return lst

    def month_list_click(self):
        with allure.step("Выбор месяца"):
            Select(self.month_list_find()).select_by_index(1)

    def day_list_find(self):
        lst = self.find(DAYLIST[0], DAYLIST[1])
        self.scroll(lst)
        with allure.step("Поиск списка дней"):
            return lst

    def day_list_click(self):
        with allure.step("Выбор дня"):
            Select(self.day_list_find()).select_by_index(1)

    def year_list_find(self):
        lst = self.find(MONTHLIST[0], MONTHLIST[1])
        self.scroll(lst)
        with allure.step("Поиск списка года"):
            return lst

    def year_list_click(self):
        with allure.step("Выбор года"):
            Select(self.month_list_find()).select_by_index(1)

    def phone_number_find(self):
        phone = self.find(PHONENUMBER[0], PHONENUMBER[1])
        self.scroll(phone)
        with allure.step("Поиск поля для ввода номера телефона"):
            return phone

    def phone_number_input(self, text):
        with allure.step('Ввод номер телефона'):
            self.phone_number_find().send_keys(text)

    def username_find(self):
        username = self.find(USERNAME[0], USERNAME[1])
        self.scroll(username)
        with allure.step("Поиск поля для ввода username"):
            return username

    def username_input(self, text):
        with allure.step('Ввод username'):
            self.username_find().send_keys(text)

    def email_find(self):
        email = self.find(EMAIL[0], EMAIL[1])
        self.scroll(email)
        with allure.step('Поиск поля ввода почты'):
            return email

    def email_input(self, text):
        with allure.step("Ввод email"):
            self.email_find().send_keys(text)

    def picture_input_find(self):
        photo = self.find(INPUTPHOTO[0], INPUTPHOTO[1])
        self.scroll(photo)
        with allure.step("Поиск вставки фото"):
            return photo

    def picture_input(self, path):
        with allure.step("Вставка пути к файла"):
            self.picture_input_find().send_keys(path)

    def password_find(self)
        password = self.find(PASSWORD[0], PASSWORD[1])
        self.scroll(password)
        with allure.step("Поиск поле ввода пароля"):
            return password

    def password_input(self, pass_text):
        with allure.step('Ввод пароля'):
            self.password_find().send_keys(pass_text)

    def password_confirm_find(self):
        password = self.find(CONFIRMPASSWORD[0], CONFIRMPASSWORD[1])
        self.scroll(password)
        with allure.step("Поиск поле ввода пароля для подтверждения"):
            return password

    def password_confirm_input(self, pass_text):
        with allure.step('Ввод пароля для потверждения'):
            self.password_confirm_find().send_keys(pass_text)

    def submit(self):
        submit = self.find(BUTTON[0], BUTTON[1])
        self.scroll(submit)
        with allure.step("Ищем кнопку для подтверждения"):
            return submit

    def submit_click(self):
        with allure.step("Подтверждаем"):
            self.click(self.submit())