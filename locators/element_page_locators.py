from selenium.webdriver.common.by import By


class FormPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.ID, "submit")

#check output after submit form
    OUTPUT_FULL_NAME = (By.CSS_SELECTOR, "p[id='name']")
    OUTPUT_EMAIL = (By.CSS_SELECTOR, "p[id='email']")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p[id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p[id='permanentAddress']")

class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEN_LIST = (By.CSS_SELECTOR, "span[class='rct-checkbox']")



