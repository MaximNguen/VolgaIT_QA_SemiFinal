from pages.click_events_page import EventsPage
import pytest

class TestEvents:
    @classmethod
    def setup_class(cls):
        print("\n============= Начало тестирования страницы с ивентами =============")

    @classmethod
    def teardown_class(cls):
        print("\n================= Конец тестов страницы ивентов =========")

    @pytest.fixture(autouse=True)
    def setup(self, browser, url="https://practice-automation.com/click-events/"):
        self.event_page = EventsPage(browser)
        self.event_page.open(url)
        yield self.event_page
        self.event_page.quit()

    def test_get_meow(self):
        self.event_page.buttonCat_click()
        assert self.event_page.receive() == "Meow!"

    def test_get_woof(self):
        self.event_page.buttonDog_click()
        assert self.event_page.receive() == "Woof!"

    def test_get_oink(self):
        self.event_page.buttonPig_click()
        assert self.event_page.receive() == "Oink!"

    def test_get_moo(self):
        self.event_page.buttonCow_click()
        assert self.event_page.receive() == "Moo!"