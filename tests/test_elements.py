import time

import pytest

from pages.base_pages import BasePage
from pages.elements_pages import TextBoxPage, CheckBoxPage, RadioButtonPage  # импорт наших созданых классов где содерж ф-ии


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




