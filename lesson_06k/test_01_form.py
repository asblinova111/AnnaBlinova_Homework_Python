from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_form():
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.maximize_window()

    try:
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "data-types.html"
        )
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # Нажимаем кнопку Submit через JS, чтобы избежать перехвата клика
        submit_btn_locator = (By.CSS_SELECTOR, "button[type='submit']")
        submit_button = wait.until(
            EC.presence_of_element_located(submit_btn_locator)
        )
        driver.execute_script("arguments[0].click();", submit_button)

        wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

        zip_field = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_field.get_attribute("class"), (
            "Поле Zip code должно быть подсвечено красным!"
        )

        green_fields_ids = [
            "first-name", "last-name", "address",
            "city", "country", "e-mail", "phone",
            "job-position", "company"
        ]

        for field_id in green_fields_ids:
            field = driver.find_element(By.ID, field_id)
            assert "alert-success" in field.get_attribute("class"), (
                f"Поле {field_id} должно быть подсвечено зеленым!"
            )

    finally:
        driver.quit()
