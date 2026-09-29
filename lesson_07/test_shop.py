import pytest
from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    # Настраиваем и запускаем именно браузер FireFox, как требует задание
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    # Браузер гарантированно закроется после теста
    driver.quit()


def test_saucedemo_shopping_flow(driver):
    # 1. Создаем объекты страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 2. Выполняем шаги сценария
    login_page.open()
    login_page.login_as("standard_user", "secret_sauce")

    inventory_page.add_required_products()
    inventory_page.go_to_cart()

    cart_page.click_checkout()

    # Заполняем форму своими произвольными данными
    checkout_page.fill_user_data(
        first_name="Иван", last_name="Иванов", zip_code="141407"
        )

    # 3. Считываем итоговую стоимость
    total_text = checkout_page.get_total_price()

    # 4. Проверяем (assert), что итоговая сумма равна $58.29
    # Так как метод возвращает строку "Total: $58.29",
    #  проверяем вхождение подстроки
    assert "$58.29" in total_text
