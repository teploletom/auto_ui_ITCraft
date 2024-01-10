import random
import time

import pytest

from pages.base_pages import BasePage
from pages.elements_pages import TextBoxPage, CheckBoxPage, RadioButtonPage, \
    WebTablePage  # импорт наших созданых классов где содерж ф-ии


class TestElements:
    @pytest.mark.skip
    class TestTextBox: #Тест формы с ФИО и адресом
        def test_p(self, driver):
            page = TextBoxPage(driver, "https://demoqa.com/text-box") #создание экземпляра класса передаем в __init__
            page.open() #функция берется из BasePage но наследуется через TextBoxPage
            full_name, email, current_address, permanent_address = page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = page.check_filled_form()
            time.sleep(30)
            assert full_name == output_name
            assert email == output_email
            assert current_address == output_cur_addr
            assert permanent_address == output_per_addr

    @pytest.mark.skip # TEST НЕ РАБОТАЕТ
    class TestCheckBox: #Тест чекбокса
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox") #создание экземпляра класса передаем в __init__
            check_box_page.open() #функция берется из BasePage но наследуется через TextBoxPage
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            check_box_page.get_checked_checkboxes()
            time.sleep(5)

    @pytest.mark.skip
    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button") # создаем экземпляр класса RadioButtonPage из element_page где обявлены все методы
            radio_button_page.open() #функция берется из BasePage но наследуется через RadioButtonPage
            # вызов 3х методов с тремя значениями
            radio_button_page.click_on_the_radio_button("yes")
            #проверка output "You have selected Yes"
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("impressive")
            #проверка output "You have selected Impressive"
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button("no")
            # проверка output "You have selected No"
            output_no = radio_button_page.get_output_result()

            #можно сделать 2 массива и сравнивать их но делаем для каждого условия assert чтоб знать где именно возникла ошиюка
            assert output_yes == "Yes", "Yes has not been selected"
            assert output_impressive == "Impressive", "Impressive has not been selected"
            assert output_no == "No", "No has not been selected - Здесь баг на сайте он не выберится"

    class TestWebTable:
        @pytest.mark.skip
        def test_web_table_add_person(self, driver):
            #сначала создаем экземпляр класса WebTablePage затем реализуем сам класс WebTablePage
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open() # вызов метода через WebTablePage который наследуется от BasePage
            new_person = web_table_page.add_new_person() #создание нового персона
            table_result = web_table_page.check_new_added_person() #получание записей таболицы
            assert new_person in table_result, "НОВЫЙ ПЕРСОН НЕ ДОБАВИЛСЯ" #сравнение созданного персона с результирующей таблицей в которую он должен попасть

        @pytest.mark.skip
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            #вызов ф-ии add_new_person return возвращает 6 параметов, берем через рандом один из них
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word) # поиск человека по ключ слову
            table_result = web_table_page.check_search_person() # возвращает всю найденую строку
            print(key_word)
            print(table_result)
            assert key_word in table_result # находим вхождение ключевого слова в найденой строке

        @pytest.mark.skip
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1] #добавляем нового персон,  возыращает второй элемент [1] - lastname и записываем в переменную lastname
            web_table_page.search_some_person(lastname) #ищем элемент по lastname
            age = web_table_page.update_person_info() #вызоы метода update персона который возвращает age, который записываем в переменную для последующего сравнения
            row = web_table_page.check_search_person() #получить полученную строку для дальнейшего сравнения
            print(age)
            print(row)
            assert age in row, "Обновленное поле не содержится в строке"

        @pytest.mark.skip
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3] #добавляем нового персон,  возыращает второй элемент [3] - email и записываем в переменную email
            web_table_page.search_some_person(email) #ищем элемент по email
            web_table_page.delete_person() #вызоы метода delete персона
            text = web_table_page.check_deleted_person() #получить полученную строку для дальнейшего сравнения
            assert text == "No rows found", "Поле не удалено"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            time.sleep(5)
            count = web_table_page.change_count_observed_row()
            assert count == [5, 10, 20]
            time.sleep(5)












