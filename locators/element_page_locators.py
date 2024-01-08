import time

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

# TEST НЕ РАБОТАЕТ
class CheckBoxPageLocators: # # TEST НЕ РАБОТАЕТ
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-checkbox']") #  чекбок ыбор ALL элеметов
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = "//ancestor::span[@class='rct-title']"

class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class*='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIBUTTON = (By.CSS_SELECTOR, "label[class*='custom-control'][for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class*='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")




