class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def find(self, *args):
        return self.browser.find_element(*args)

    def scroll(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def click(self, element):
        self.browser.execute_script("arguments[0].click();", element)

    def quit(self):
        self.browser.quit()