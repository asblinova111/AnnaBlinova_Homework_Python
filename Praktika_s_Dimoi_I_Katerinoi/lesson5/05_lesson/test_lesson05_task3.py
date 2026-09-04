"""
Тест 3. Проверка нескольких элементов
Задание:Откройте страницу https://httpbin.qa-territory.online/links/10.
Найдите все ссылки на странице (тег <a>).
Проверьте, что количество ссылок равно 9.
Проверьте, что все ссылки отображаются на странице.
Проверьте, что текст первой ссылки содержит "1".

Код для выполнения:

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    # Ваш код здесь

    driver.quit()

Не используйте time.sleep() без необходимости.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    # Настраиваем явное ожидание до 10 секунд
    wait = WebDriverWait(driver, 10)

    # 1. Жду загрузку хотя бы  одной ссылки
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))

    # 2. Находим все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # 3. Проверяем, что количество ссылок в списке равно 9
    assert len(links) == 9, f"Ожидалось 9 ссылок, но найдено {len(links)}"

    # 4. С помощью цикла проверяем, что каждая ссылка отображается на странице
    for link in links:
        assert link.is_displayed(), (
            f"Ссылка с текстом '{link.text}' не отображается на экране"
        )

    # 5. Проверяем, что текст первой ссылки (индекс) содержит "1"
    first_link_text = links[0].text
    assert "1" in first_link_text, (
         "Ожидалось,что 1я ссылка содержит '1'"
         f" но там: '{first_link_text}'"
    )

    print(
        "✅ Тест успешно пройден! Все 9 ссылок отображаются,"
        " первая ссылка содержит '1'."
        )

    driver.quit()
