import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.element_page_locators import FormPageLocators, CheckBoxPageLocators, \
    RadioButtonPageLocators, WebTablePageLocator  # , CheckBoxPageLocators
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

class WebTablePage(BasePage):
    locators = WebTablePageLocator() #сначала создаем экземпляр класса затем реализуем сам класс WebTablePageLocator

    def add_new_person(self):
        count = random.randint(2, 4)
        while count !=0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -=1
            #возвращаем сгенерированные данные имя, емайл и т п для поседующего сравнения с рузультирующей таблицей
            #изменили местами вывод параметров так как при српавнении из таблицы там параметры в другом порядке
            #преобразовали в тип str так как при сравнении из таблицы все данные типа str
            #преобразовали в list так как при сравнении из таблицы все данные list
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines()) #разбиваем строку и получаем такой вид ['Cierra', 'Vega', '39', 'cierra@example.com', '10000', 'Insurance']
        return data # возвращаем список из полученных элементов таблицы

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)#поиск в строке поиска по ключевому слову

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON) #по кнопке DELETE ищем строку-результат поиска (другого локатора не нашли)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT) # берем всю строку по локатору всей строки
        return row.text.splitlines() #разбиваем строку чтоб потом использовать для сравнения - Return a list of the lines in the string

    def update_person_info(self):
        person_info = next(generated_person()) #генерируем нового Персон с помощью faker
        age = person_info.age # берем только age у сгененрированого Персона
        self.element_is_visible(self.locators.UPDATE_ICON).click() #Нажать на иконку абдейта
        self.element_is_visible(self.locators.AGE_INPUT).clear() #найти поле Аge и очистить поле так как без очистки не получается вставить новое значение
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age) #найти поле Аge и вставить полученный age
        self.element_is_visible(self.locators.SUBMIT).click() #нажать submit
        return str(age) # возвращаем age для последующего сравнения в тесте

    def delete_person(self):
        self.element_is_present(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        return self.element_is_visible(self.locators.NO_ROWS_FOUND).text

    def change_count_observed_row(self):
        count = [5, 10, 20]
        data = []
        #выбор значений из списка каунт из выпадающего списка
        for x in count:
            count_row_button=self.element_is_visible(self.locators.COUNT_ROWS_LIST)
            #self.element_is_visible(self.locators.COUNT_ROWS_LIST)
            #self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{x}']")).click() #выбираем количество строк для отображения
            data.append(self.check_count_rows()) #вызов ф-ии подсчета колиества строк и добавляем ее в список , который далее используем в assert
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)








