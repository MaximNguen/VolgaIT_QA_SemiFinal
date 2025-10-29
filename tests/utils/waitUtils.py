from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:
    """Класс для хранения методов ожидания у selenium"""

    def wait(browser, element):
        return WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(element)
        )