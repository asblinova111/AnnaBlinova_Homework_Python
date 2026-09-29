import pytest
from selenium import webdriver
from calculator_page import SlowCalculatorPage


@pytest.fixture
def driver():
    # Тест может только создавать, настраивать и закрывать драйвер
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # Каждая проверка должна создавать и использовать объект страницы
    calc_page = SlowCalculatorPage(driver)

    # Шаги теста (никаких методов Selenium вроде click или text здесь нет)
    calc_page.open()
    calc_page.set_delay("45")

    calc_page.click_seven()
    calc_page.click_plus()
    calc_page.click_eight()
    calc_page.click_equals()

    # Получаем результат с явным ожиданием до 50 секунд
    # (с запасом под задержку в 45 сек)
    result = calc_page.get_result_after_wait(expected_value="15", timeout=50)

    # Проверка (assert) находится строго в коде теста
    assert result == "15"
