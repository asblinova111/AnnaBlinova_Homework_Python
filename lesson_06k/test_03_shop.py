from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_purchase():
    # Настройка и запуск браузера FireFox, как требуется в задании
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()

    # Переменная для сохранения итоговой цены перед закрытием браузера
    total_price = ""

    try:
        # 1. Открываем сайт магазина
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 10)

        # 2. Авторизуемся как стандартный пользователь
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Добавляем в корзину три указанных товара
        # Локаторы разбиты на две строки, чтобы длина не превышала 79 символов
        el_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        wait.until(EC.element_to_be_clickable(el_backpack)).click()

        el_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        driver.find_element(*el_tshirt).click()

        el_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        driver.find_element(*el_onesie).click()

        # 4. Переходим в корзину (кликаем по иконке корзины)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 5. Нажимаем кнопку Checkout
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # 6. Заполняем форму своими данными
        el_first_name = (By.ID, "first-name")
        wait.until(EC.presence_of_element_located(el_first_name)).send_keys(
            "Анна"
        )
        driver.find_element(By.ID, "last-name").send_keys("Блинова")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # 7. Нажимаем кнопку Continue
        driver.find_element(By.ID, "continue").click()

        # 8. Читаем со страницы итоговую стоимость (Total)
        total_locator = (By.CLASS_NAME, "summary_total_label")
        total_element = wait.until(
            EC.presence_of_element_located(total_locator)
        )
        total_price = total_element.text
        # Текст будет в формате "Total: $58.29"

    finally:
        # 9. Закрываем браузер СТРОГО до проверки ассерта
        driver.quit()

    # 10. Проверяем, что итоговая сумма равна $58.29
    err_msg = f"Ожидалась сумма $58.29, но на странице было: '{total_price}'"
    assert "$58.29" in total_price, err_msg
