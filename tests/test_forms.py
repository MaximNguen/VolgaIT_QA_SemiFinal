import pytest
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

    @pytest.mark.parametrize("name, password, email, message", [
        ("asdasd", "dasdasdsad", "dsadasdsad", "sdasdasdasd")
    ])
    def test_all(self, name, password, email, message):
        self.form_page.nameInput_send(name)
        self.form_page.passwordInput_send(password)
        self.form_page.checkbox1_click()
        self.form_page.checkbox2_click()
        self.form_page.checkbox3_click()
        self.form_page.checkbox4_click()
        self.form_page.checkbox5_click()
        self.form_page.checkbox6_click()
        self.form_page.radio1_click()
        self.form_page.select_click()
        self.form_page.email_send(email)
        self.form_page.message_send(message)
        self.form_page.submit_click()
        assert self.form_page.check_state_alert() == "Message received!"

