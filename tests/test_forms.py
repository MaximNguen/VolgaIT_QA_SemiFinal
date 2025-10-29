import allure
import pytest

from utils.expected_conditions import ExpectedTexts as EC
from pages.forms_page import FormsPage

class TestFormsPage:
    @classmethod
    def setup_class(cls):
        print("\n============= Начало тестирования страницы с формами =============")

    @classmethod
    def teardown_class(cls):
        print("\n================= Конец тестов страницы формов =========")

    @pytest.fixture(autouse=True)
    def setup(self, browser, url = "https://practice-automation.com/form-fields/"):
        self.form_page = FormsPage(browser)
        self.form_page.open(url)
        yield self.form_page
        self.form_page.quit()

    @allure.feature("Forms")
    @allure.story("Ввод всех полей и нажитий ячеек")
    @pytest.mark.parametrize("name, password, email", [
        ("asdasd", "dasdasdsad", "dsadasdsad")
    ])
    def test_all(self, name, password, email):
        self.form_page.nameInput_send(name)
        self.form_page.passwordInput_send(password)
        self.form_page.checkbox1_click()
        self.form_page.checkbox2_click()
        self.form_page.checkbox3_click()
        self.form_page.checkbox4_click()
        self.form_page.checkbox5_click()
        self.form_page.radio1_click()
        self.form_page.email_send(email)
        self.form_page.select_click()
        self.form_page.message_send()
        self.form_page.submit_click()
        text = self.form_page.check_state_alert()
        with allure.step("Подтверждаем, что после нажатия Submit у нас выпало нужное предложение в Alert'е"):
            assert text == EC.FORM_SUCCESS, f"Ожидалось вывод текста {EC.FORM_SUCCESS}, но получили {text}"
