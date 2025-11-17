from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class WaitUtils:
    """Класс для хранения методов ожидания у selenium"""
    def  __init__(self, browser, timeout = 10):
        self.browser = browser
        self.timeout = timeout
        self.wait = WebDriverWait(self.browser, self.timeout)

    @allure.step("Ожидание элемента {element[0]}: {element[1]}")
    def wait(self, browser, element):
        return self.wait.until(
            EC.presence_of_element_located(element)
        )

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_clickable(self, browser, element):
        return self.wait.until(
            EC.element_to_be_clickable(element)
        )

    @allure.step("Ожидание появления Alert")
    def wait_For_alert(self):
        return self.wait.until(
            EC.alert_is_present()
        )

    @staticmethod
    def wait_static(browser, element, timeout=10):
        return WebDriverWait(browser, timeout).until(
            EC.presence_of_all_elements_located(element)
        )