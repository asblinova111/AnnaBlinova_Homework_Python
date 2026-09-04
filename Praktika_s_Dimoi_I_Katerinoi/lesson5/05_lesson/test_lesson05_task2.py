"""
Тест 2. Работа с текстовым полем и кнопкой
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Ваш код здесь

    driver.quit()

Используйте By.NAME для поиска поля по атрибуту name.
Используйте send_keys()для ввода текста.
Кнопка имеет текст "Submit", можно использовать By.XPATH с текстом.
После клика проверьте, что URL изменился с помощью driver.current_url.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    wait = WebDriverWait(driver, 10)

    # 1. Поиск поля ввода и вводим имя
    name_input = wait.until(
        EC.presence_of_element_located((By.NAME, "custname"))
        )
    name_input.send_keys("Анна")

    # 2. Находим кнопку и кликаем
    submit_button = wait.until(
        EC.element_to_be_clickable
        ((By.XPATH, "//button[text()='Submit order']"))
        )
    submit_button.click()

    # 3. Ожидаемый URL, адрес страницы результата
    expected_url = "https://httpbin.qa-territory.online/post"
    wait.until(EC.url_to_be(expected_url))

    # 4. Проверяем текущий URL
    assert driver.current_url == expected_url, (
        f"Ожидался URL {expected_url}",
        "но получили {driver.current_url}"
    )

    driver.quit()
