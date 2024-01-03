#фикстуры будут использовать все тесты до запуска, здесь будет фикстура драйвера

from selenium import webdriver
import pytest

@pytest.fixture() # иницииал драйвера
def driver():
    driver = webdriver.Chrome()
    yield driver # работает как return
    driver.quit()







