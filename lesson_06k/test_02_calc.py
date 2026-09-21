from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    # Настройка и запуск браузера Google Chrome, как требуется в задании
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        # 1. Открываем страницу медленного калькулятора
        # Выносим ссылку в переменную, чтобы убрать ошибку E501
        url = (
            "https://bonigarcia.dev"
            "slow-calculator.html"
        )
        driver.get(url)

        # 2. В поле ввода по локатору #delay вводим значение 45
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()  # Очищаем поле от старого значения
        # там по умолчанию стоит 5
        delay_input.send_keys("45")

        # 3. Нажимаем на кнопки: 7, +, 8, =
        # Находим кнопки по их тексту на элементах (внутри тегов span)
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # 4. Проверяем, что в окне отобразится результат 15 через 45 секунд
        # Создаем WebDriverWait с запасом (например, 50 секунд),
        # так как калькулятор считает ровно 45
        wait = WebDriverWait(driver, 50)

        # Окно с результатом имеет класс .screen
        # Ожидаем, пока в тексте этого элемента появится заветное число "15"
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )

        # Финальная проверка через assert
        result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result_text == "15", (
            f"Ожидался результат 15, но калькулятор показал: {result_text}"
        )

    finally:
        # Обязательно закрываем браузер после окончания теста
        driver.quit()
