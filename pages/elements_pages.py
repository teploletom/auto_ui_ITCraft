import time

from generator.generator import generated_person
from locators.element_page_locators import FormPageLocators #, CheckBoxPageLocators
from pages.base_pages import BasePage


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
