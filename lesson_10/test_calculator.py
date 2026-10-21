import pytest
import allure
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


@allure.title("Проверка работы калькулятора со встроенной задержкой")
@allure.description("Тест устанавливает задержку, "
                    "выполняет сложение 7 + 8 и дожидается результата 15")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(driver):
    # Каждая проверка должна создавать и использовать объект страницы
    calc_page = SlowCalculatorPage(driver)

    with allure.step("Открыть страницу медленного калькулятора"):
        calc_page.open()

    with allure.step("Установить задержку выполнения в 45 секунд"):
        calc_page.set_delay("45")

    with allure.step("Ввести первый операнд: 7"):
        calc_page.click_seven()

    with allure.step("Выбрать операцию: Плюс (+)"):
        calc_page.click_plus()

    with allure.step("Ввести второй операнд: 8"):
        calc_page.click_eight()

    with allure.step("Нажать кнопку Равно (=)"):
        calc_page.click_equals()

    with allure.step("Дождаться появления и получить итоговый результат"):
        # Получаем результат с явным ожиданием до 50 секунд
        result = calc_page.get_result_after_wait(expected_value="15",
                                                 timeout=50)

    with allure.step("Проверить, что итоговый результат равен 15"):
        # Проверка (assert) находится строго в коде теста
        assert result == "15"
