from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:
    """Класс для хранения методов ожидания у selenium"""

    @staticmethod
    def wait_for_presence(browser, element):
        return WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(element)
        )

    @staticmethod
    def wait_for_clickable(browser, element):
        return WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(element)
        )

    @staticmethod
    def wait_for_all_presence(browser, element):
        return WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located(element)
        )