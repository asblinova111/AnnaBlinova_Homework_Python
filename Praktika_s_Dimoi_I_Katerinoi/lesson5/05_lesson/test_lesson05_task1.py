"""
Тест 1. Навигация и проверка URL

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

# Ваш код здесь  Используйте driver.back()для возврата назад.
#Для проверки URL используйте driver.current_url.
#Ссылка HTML Form имеет текст "HTML Form", используйте By.LINK_TEXT.

    driver.quit()
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # 1. Открываю главную страницу
    driver.get("https://httpbin.qa-territory.online")

    # 2.Нахожу и кликаю на ссылку "HTML Form"
    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()

    # 3. Проверяем, что URL стал /forms/post
    assert "/forms/post" in driver.current_url

    # 4. Возвращаюсь назад
    driver.back()

    # 5. Проверяю, что вернулись на главную страницу
    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()
