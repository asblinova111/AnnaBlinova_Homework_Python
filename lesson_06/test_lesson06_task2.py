from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Открываем главную страницу сайта, чтобы задать домен для кук
    driver.get("https://gitflic.ru")

    # 2. Устанавливаем собственную куку для имитации пользователя 1
    user1_cookie = {"name": "user1_session", "value": "authenticated_active"}
    driver.add_cookie(user1_cookie)

    # 3. Обновляем страницу для симуляции применения сессии
    driver.refresh()

    # 4. Переходим на реальную страницу вашего ПЕРВОГО профиля
    # Обязательно замените 'ваш_никнейм_1' на имя вашего первого аккаунта
    driver.get("https://gitflic.ru/user/zara111")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # 5. Сохраняем текущий URL первого пользователя
    url_user1 = driver.current_url

    # 6. Разлогиниваемся (очищаем все куки)
    driver.delete_all_cookies()

    # 7. Устанавливаем собственную куку для имитации пользователя 2
    user2_cookie = {"name": "user2_session", "value": "authenticated_active"}
    driver.add_cookie(user2_cookie)

    # 8. Обновляем страницу
    driver.refresh()

    # 9. Переходим на реальную страницу вашего ВТОРОГО профиля
    # Обязательно замените 'ваш_никнейм_2' на имя вашего второго аккаунта
    driver.get("https://gitflic.ru/user/shushu")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # 10.Сохраняем текущий URL второго пользователя
    url_user2 = driver.current_url

    # 11. Проверяем, что URL для пользователя 1 и пользователя 2 различаются
    assert url_user1 != url_user2, (
        f"Ошибка: URL профилей совпадают ({url_user1}). "
        f"Тест не зафиксировал смену пользователей."
    )

    driver.quit()
