
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://herokuapp.com
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Инициализируем явное ожидание (
    # таймаут до 15 секунд, так как текст грузится около 5 секунд)
    wait = WebDriverWait(driver, 15)

    # 2. Найдите и нажмите на кнопку "Start" с помощью CSS-селектора
    start_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    start_button.click()

    # 3. Дождитесь появления текста "Hello World!" на экране
    # Локатор #finish содержит скрытый текст, который становится
    #  видимым после загрузки
    success_text_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshot_hello_world.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    actual_text = success_text_element.text
    assert actual_text == "Hello World!", (
        f"Ожидался текст 'Hello World!',"
        f"но на странице отображается: '{actual_text}'"
    )

    driver.quit()
