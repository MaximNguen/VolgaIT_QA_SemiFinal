from selenium.webdriver.common.by import By

# =============== Первый сайт ===============
FIRST_NAME = (By.XPATH, '//*[@id="register_form"]/fieldset[1]/p[1]/input')
LAST_NAME = (By.XPATH, '//*[@id="register_form"]/fieldset[1]/p[2]/input')

RADIO1 = (By.CSS_SELECTOR, '#register_form > fieldset:nth-child(2) > div > label:nth-child(1) > input[type=radio]')
RADIO2 = (By.XPATH, '//*[@id="register_form"]/fieldset[2]/div/label[2]/input')
RADIO3 = (By.XPATH, '//*[@id="register_form"]/fieldset[2]/div/label[3]/input')

CHECKBOX1 = (By.XPATH, '//*[@id="register_form"]/fieldset[3]/div/label[1]/input')
CHECKBOX2 = (By.XPATH, '//*[@id="register_form"]/fieldset[3]/div/label[2]/input')
CHECKBOX3 = (By.XPATH, '//*[@id="register_form"]/fieldset[3]/div/label[3]/input')

COUNTRYLIST = (By.XPATH, '//*[@id="register_form"]/fieldset[4]/select')
MONTHLIST = (By.XPATH, '//*[@id="register_form"]/fieldset[5]/div[1]/select')
DAYLIST = (By.XPATH, '//*[@id="register_form"]/fieldset[5]/div[2]/select')
YEARLIST = (By.XPATH, '//*[@id="register_form"]/fieldset[5]/div[3]/select')

PHONENUMBER = (By.XPATH, '//*[@id="register_form"]/fieldset[6]/input')
USERNAME = (By.XPATH, '//*[@id="register_form"]/fieldset[7]/input')
EMAIL = (By.XPATH, '//*[@id="register_form"]/fieldset[8]/input')

INPUTPHOTO = (By.XPATH, '//*[@id="register_form"]/fieldset[9]/input')

TEXTAREA = (By.XPATH, '//*[@id="register_form"]/fieldset[10]/textarea')
PASSWORD = (By.XPATH, '//*[@id="register_form"]/fieldset[11]/input')
CONFIRMPASSWORD = (By.XPATH, '//*[@id="register_form"]/fieldset[12]/input')
BUTTON = (By.XPATH, '//*[@id="register_form"]/fieldset[13]/input')

REQUIREDFIELD = (By.XPATH, '//*[@id="register_form"]/fieldset[1]/p[1]/label[2]')
INVALIDEMAIL = (By.XPATH, '//*[@id="register_form"]/fieldset[8]/label[2]')
LISTOFWARNINGS = (By.XPATH, "//label[@class='error_p']")