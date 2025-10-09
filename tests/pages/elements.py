from selenium.webdriver.common.by import By

# =============== Первый сайт ===============
NAMEINPUT = (By.XPATH, "//input[@id='name-input']")
PASSWORDINPUT = (By.CSS_SELECTOR, "input[type='password']")
CHECKBOX1 = (By.ID, "drink1")
CHECKBOX2 = (By.ID, "drink2")
CHECKBOX3 = (By.ID, "drink3")
CHECKBOX4 = (By.ID, "drink4")
CHECKBOX5 = (By.ID, "drink5")
CHECKBOX6 = (By.ID, "drink6")
RADIO1 = (By.ID, "color3")
SELECT = (By.ID, "automation")
EMAILINPUT = (By.ID, "email")
LIST = (By.TAG_NAME, "li")
MESSAGE = (By.ID, "message")
SUBMIT = (By.ID, "submit-btn")

# =============== Второй сайт ===============

BUTTONCAT = (By.XPATH, "//button[@class='custom_btn btn_hover' and @onclick='catSound()']")
BUTTONDOG = (By.XPATH, "//button[@class='custom_btn btn_hover' and @onclick='dogSound()']")
BUTTONPIG = (By.XPATH, "//button[@class='custom_btn btn_hover' and @onclick='pigSound()']")
BUTTONCOW = (By.XPATH, "//button[@class='custom_btn btn_hover' and @onclick='cowSound()']")
RESULT = (By.ID, "demo")

# =============== Третий сайт ==============

ALERT1 = (By.XPATH, '//button[@onclick="alertPopup()"]')
ALERT2 = (By.XPATH, '//button[@onclick="confirmPopup()"]')
RESULTTEXT = (By.ID, "confirmResult")
ALERT3 = (By.XPATH, '//button[@onclick="promptPopup()"]')
RESULTTEXT1 = (By.ID, "promptResult")
