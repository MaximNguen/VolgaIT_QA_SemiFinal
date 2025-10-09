import pytest
from pages.alerts_page import AlertsPage

class TestAlertsPage:

    @classmethod
    def setup_class(cls):
        print("\n============= Начало тестирования страницы с алертами =============")

    @classmethod
    def teardown_class(cls):
        print("\n================= Конец тестов страницы алертов =========")

    @pytest.fixture(autouse=True)
    def setup(self, browser, url = "https://practice-automation.com/popups/"):
        self.alert_page = AlertsPage(browser)
        self.alert_page.open(url)
        yield self.alert_page
        self.alert_page.quit()

    def test_alert1(self):
        self.alert_page.alert1_click()
        text = self.alert_page.get_alert1_text()
        self.alert_page.accept_alert1_text()
        assert text == "Hi there, pal!"

    def test_alert2_success(self):
        self.alert_page.alert2_click()
        self.alert_page.accept_alert2_text()
        assert self.alert_page.get_text_after_alert2() == "OK it is!"

    def test_alert2_failure(self):
        self.alert_page.alert2_click()
        self.alert_page.dismiss_alert2()
        assert self.alert_page.get_text_after_alert2() == "Cancel it is!"

    @pytest.mark.parametrize("name", ["Max"])
    def test_alert3_success(self, name):
        self.alert_page.alert3_click()
        self.alert_page.send_text_to_alert3(name)
        self.alert_page.accept_alert3()
        assert self.alert_page.get_text_after_alert3() == f"Nice to meet you, {name}!"

    def test_alert3_failure_without_name(self):
        self.alert_page.alert3_click()
        self.alert_page.accept_alert3()
        assert self.alert_page.get_text_after_alert3() == "Fine, be that way..."

    def test_alert3_failure(self):
        self.alert_page.alert3_click()
        self.alert_page.dismiss_alert3()
        assert self.alert_page.get_text_after_alert3() == "Fine, be that way..."

