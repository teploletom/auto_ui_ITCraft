import random

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.element_page_locators import FormPageLocators, CheckBoxPageLocators, \
    RadioButtonPageLocators  # , CheckBoxPageLocators
from pages.base_pages import BasePage
from selenium import webdriver


class TextBoxPage(BasePage):
    locator = FormPageLocators()#экземпляр класса где храняться локаторы

    def fill_all_fields(self):#FULL_NAME через экземпляр класса locator где храняться локаторы
        person_info = next(generated_person())# итератор возьмет по одноому что вернет generated_person
        print("это персон инфо", type(person_info), person_info)
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locator.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locator.EMAIL).send_keys(email)
        self.element_is_visible(self.locator.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locator.PERMANENT_ADDRESS).send_keys(permanent_address)
        #кнопку не видно из-за рекламы, нужно проскролить.
        self.element_is_visible(self.locator.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locator.OUTPUT_FULL_NAME).text.split(":")[1]
        #возвращает Name: hggggg - отделить Name от значения через split по знаку : получим список ['Name', ' Ghrisha']
        #далее сделаем [1] чтоб получить только имя Ghrisha
        email = self.element_is_present(self.locator.OUTPUT_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(self.locator.OUTPUT_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(self.locator.OUTPUT_PERMANENT_ADDRESS).text.split(":")[1]
        return full_name, email, current_address, permanent_address

# TEST НЕ РАБОТАЕТ
class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):#хранится весь лист элеменов - чекбоксов
        item_list = self.elements_are_visible(self.locators.ITEM_LIST) #пишем self так как element_is_visible в base page а там __init__
        item = item_list[random.randint(1, 15)]
        item.click()

    def get_checked_checkboxes(self):# получаем выбранные чекбоксы для последующей проверки
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
       # print(checked_list)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        print(data)

class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()
    def click_on_the_radio_button(self, choice): #в choice передается Yes Impressive NO
        #создаем словарь с вариантами радиобатанов
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                  'impressive': self.locators.IMPRESSIVE_RADIBUTTON,
                  'no': self.locators.NO_RADIOBUTTON}

        self.element_is_visible(choices[choice]).click() #обращение к элменту словаря dict_sample["model"]

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text #вернет текст который будет assert





