import pytest
import allure
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


@allure.title("Сквозной сценарий покупки товаров в интернет-магазине")
@allure.description("Тест проверяет полный цикл: "
                    "авторизацию, добавление трех товаров в корзину,"
                    "оформление заказа и сверку финальной стоимости")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_shopping_flow(driver):
    # 1. Создаем объекты страниц
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 2. Выполняем шаги сценария
    with allure.step("Открыть главную страницу магазина Saucedemo"):
        login_page.open()

    with allure.step("Авторизоваться под стандартным пользователем"):
        login_page.login_as("standard_user", "secret_sauce")

    with allure.step("Добавить необходимые товары в корзину"):
        inventory_page.add_required_products()

    with allure.step("Перейти в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Нажать кнопку перехода к оформлению заказа (Checkout)"):
        cart_page.click_checkout()

    with allure.step("Заполнить форму персональными данными покупателя"):
        # Заполняем форму своими произвольными данными
        checkout_page.fill_user_data(
            first_name="Иван", last_name="Иванов", zip_code="141407"
        )

    # 3. Считываем итоговую стоимость
    with allure.step("Получить итоговую стоимость заказа"
                     " с экрана суммарной информации"):
        total_text = checkout_page.get_total_price()

    # 4. Проверяем (assert), что итоговая сумма равна $58.29
    with allure.step("Проверить, что итоговая сумма заказа составляет $58.29"):
        # Так как метод возвращает строку "Total: $58.29",
        # проверяем вхождение подстроки
        assert "$58.29" in total_text
