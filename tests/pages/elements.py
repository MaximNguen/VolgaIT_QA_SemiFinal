from selenium.webdriver.common.by import By

# =============== Первый сайт ===============
NAMEINPUT = (By.XPATH, "//input[@id='name-input']")
PASSWORDINPUT = (By.CSS_SELECTOR, "input[type='password']")
CHECKBOX1 = (By.XPATH, f"//input[@type='checkbox' and @id='drink1']")
CHECKBOX2 = (By.XPATH, f"//input[@type='checkbox' and @id='drink2']")
CHECKBOX3 = (By.XPATH, f"//input[@type='checkbox' and @id='drink3']")
CHECKBOX4 = (By.XPATH, f"//input[@type='checkbox' and @id='drink4']")
CHECKBOX5 = (By.XPATH, f"//input[@type='checkbox' and @id='drink5']")
RADIO1 = (By.XPATH, f"//input[@type='radio' and @id='color3']")
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
