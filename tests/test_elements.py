import time
from pages.base_pages import BasePage
from pages.elements_pages import TextBoxPage #, CheckBoxPage


class TestElements:
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

    # class TestCheckBox: #Тест чекбокса
    #     def test_check_box(self, driver):
    #         check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
    #         check_box_page.open_full_list()
    #         check_box_page.click_random_checkbox()


