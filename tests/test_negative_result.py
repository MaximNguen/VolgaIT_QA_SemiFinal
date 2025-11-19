import allure
import pytest

from pages.forms_page import FormsPage
from utils.testData import TestData as TD
from utils.expected_texts import ExpectedTexts as ET

class TestFormsPageNegativeCases:
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

    @allure.feature("Негативный тест-кейс №1")
    @allure.story("Заполнение не всех требующих полей")
    @pytest.mark.parametrize("last_name, phone_number, username, mail, password", TD.DataForNotAllRequiredFields)
    def test_not_all_required_fields(self, browser, last_name, phone_number, username, mail, password):
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

        get_text = self.form_page.required_text_find().text
        with allure.step("Достоверимся, что у нас вылез текст о том, что мы не все заполнили"):
            assert get_text == ET.REQUIRED_FIELD, f"Ожидалось, что будет сообщение {ET.REQUIRED_FIELD}, но получили {get_text}"

    @allure.feature("Негативный тест-кейс №2")
    @allure.story("Ввод всех требующих полей, но почта невалидная")
    @pytest.mark.parametrize("first_name, last_name, phone_number, username, mail, password", TD.DataForRequiredFieldWithNonValidEmail)
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

        get_email_notification = self.form_page.invalid_email_text_find().text
        with allure.step("Достоверимся, что появился текст о том, что у нас почта невалидна"):
            assert get_email_notification == ET.INVALID_EMAIL, f"Ожидалось, что будет сообщение {ET.INVALID_EMAIL}, но получили {get_email_notification}"

    @allure.feature("Негативный тест-кейс №3")
    @allure.story("Получение предупреждений при отсутствии каких-либо заполненных полей")
    def test_no_fields(self, browser):
        self.form_page.submit_click()

        get_list_of_warnings = self.form_page.get_list_of_warnings()
        assert len(get_list_of_warnings) == 7, f"При ручном тесте обнаружен 7 предупреждений, получены такие элементы {get_list_of_warnings}"