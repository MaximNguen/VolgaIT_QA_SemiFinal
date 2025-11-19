import allure
import pytest

from pages.forms_page import FormsPage
from utils.testData import TestData as TD
from utils.expected_texts import ExpectedTexts as ET

class TestFormsPage:
    @classmethod
    def setup_class(cls):
        print("\n============= Начало тестирования страницы с формами =============")

    @classmethod
    def teardown_class(cls):
        print("\n================= Конец тестов страницы формов =========")

    @pytest.fixture(autouse=True)
    def setup(self, browser, url = "https://way2automation.com/way2auto_jquery/registration.php#load_box"):
        self.form_page = FormsPage(browser)
        self.form_page.open(url)
        yield self.form_page
        self.form_page.quit()

    @allure.feature("Положительный тест-кейс №1")
    @allure.story("Ввод всех требующих полей")
    @pytest.mark.parametrize("first_name, last_name, phone_number, username, mail, password", TD.DataForRequiredField)
    def test_required_field(self, browser, first_name, last_name, phone_number, username, mail, password):
        self.form_page.first_name_input(first_name)
        self.form_page.last_name_input(last_name)
        self.form_page.checkbox1_click()
        self.form_page.checkbox2_click()
        self.form_page.checkbox3_click()
        self.form_page.phone_number_input(phone_number)
        self.form_page.username_input(username)
        self.form_page.email_input(mail)
        self.form_page.password_input(password)
        self.form_page.password_confirm_input(password)
        self.form_page.submit_click()

        first_name_field_status = ET.expected_text(self.form_page.first_name_find(), "")
        last_name_field_status = ET.expected_text(self.form_page.last_name_find(), "")
        checkbox1_field_status = ET.boxState(self.form_page.checkbox1_find())
        checkbox2_field_status = ET.boxState(self.form_page.checkbox2_find())
        checkbox3_field_status = ET.boxState(self.form_page.checkbox3_find())
        phone_number_field_status = ET.expected_text(self.form_page.phone_number_find(), "")
        username_field_status = ET.expected_text(self.form_page.username_find(), "")
        email_field_status = ET.expected_text(self.form_page.email_find(), "")
        password_field_status = ET.expected_text(self.form_page.password_find(), "")
        confirm_password_field_status = ET.expected_text(self.form_page.password_confirm_find(), "")

        expected_url = TD.EXPECTED_URL
        current_url = browser.current_url
        with allure.step("Достоверимся, что все поля ранее заполненные, теперь пустые после подтверждения"):
            assert expected_url == current_url, \
                f"Ожидалось, что после подтверждения браузер перейдет нa - {expected_url}, но браузер перешел на {current_url}"
            assert first_name_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.first_name_find().text}"
            assert last_name_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.last_name_find().text}"
            assert checkbox1_field_status == True, ET.COMMENT_ABOUT_BOX
            assert checkbox2_field_status == True, ET.COMMENT_ABOUT_BOX
            assert checkbox3_field_status == True, ET.COMMENT_ABOUT_BOX
            assert phone_number_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.phone_number_find().text}"
            assert username_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.username_find().text}"
            assert email_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.email_find().text}"
            assert password_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.password_find().text}"
            assert confirm_password_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.password_confirm_find().text}"

    @allure.feature("Положительный тест-кейс №2")
    @allure.story("Ввод всех полей")
    @pytest.mark.parametrize("first_name, last_name, radio, phone_number, username, mail, photo, about, password", TD.DataForAllField)
    def test_all_fields(self, browser, first_name, last_name, radio, phone_number, username, mail, photo, about, password):
        self.form_page.first_name_input(first_name)
        self.form_page.last_name_input(last_name)
        match radio:
            case 1:
                self.form_page.radiobox1_click()
            case 2:
                self.form_page.radiobox2_click()
            case 3:
                self.form_page.radiobox3_click()
        self.form_page.checkbox1_click()
        self.form_page.checkbox2_click()
        self.form_page.checkbox3_click()
        self.form_page.day_list_click()
        self.form_page.month_list_click()
        self.form_page.year_list_click()
        self.form_page.phone_number_input(phone_number)
        self.form_page.username_input(username)
        self.form_page.email_input(mail)
        self.form_page.picture_input(photo)
        self.form_page.about_input(about)
        self.form_page.password_input(password)
        self.form_page.password_confirm_input(password)
        self.form_page.submit_click()

        first_name_field_status = ET.expected_text(self.form_page.first_name_find(), "")
        last_name_field_status = ET.expected_text(self.form_page.last_name_find(), "")
        radiobox1_field_status = ET.expected_text(self.form_page.radiobox1_find(), "")
        radiobox2_field_status = ET.expected_text(self.form_page.radiobox2_find(), "")
        radiobox3_field_status = ET.expected_text(self.form_page.radiobox3_find(), "")
        checkbox1_field_status = ET.boxState(self.form_page.checkbox1_find())
        checkbox2_field_status = ET.boxState(self.form_page.checkbox2_find())
        checkbox3_field_status = ET.boxState(self.form_page.checkbox3_find())
        phone_number_field_status = ET.expected_text(self.form_page.phone_number_find(), "")
        username_field_status = ET.expected_text(self.form_page.username_find(), "")
        email_field_status = ET.expected_text(self.form_page.email_find(), "")
        about_field_status = ET.expected_text(self.form_page.about_find(), "")
        password_field_status = ET.expected_text(self.form_page.password_find(), "")
        confirm_password_field_status = ET.expected_text(self.form_page.password_confirm_find(), "")

        expected_url = TD.EXPECTED_URL
        current_url = browser.current_url
        with allure.step("Достоверимся, что все поля ранее заполненные, теперь пустые после подтверждения"):
            assert expected_url == current_url, \
                f"Ожидалось, что после подтверждения браузер перейдет нa - {expected_url}, но браузер перешел на {current_url}"
            assert first_name_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.first_name_find().text}"
            assert last_name_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.last_name_find().text}"
            assert radiobox1_field_status == True, ET.COMMENT_ABOUT_BOX
            assert radiobox2_field_status == True, ET.COMMENT_ABOUT_BOX
            assert radiobox3_field_status == True, ET.COMMENT_ABOUT_BOX
            assert checkbox1_field_status == True, ET.COMMENT_ABOUT_BOX
            assert checkbox2_field_status == True, ET.COMMENT_ABOUT_BOX
            assert checkbox3_field_status == True, ET.COMMENT_ABOUT_BOX
            assert phone_number_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.phone_number_find().text}"
            assert username_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.username_find().text}"
            assert email_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.email_find().text}"
            assert about_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.about_find().text}"
            assert password_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.password_find().text}"
            assert confirm_password_field_status == True, f"{ET.EXPECTED_EMPTY_TEXT} {self.form_page.password_confirm_find().text}"