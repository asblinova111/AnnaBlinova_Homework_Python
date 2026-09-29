from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    # Простые и надежные локаторы на основе ID и текста кнопок
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BTN_7 = (By.XPATH, "//span[text()='7']")
    BTN_8 = (By.XPATH, "//span[text()='8']")
    BTN_PLUS = (By.XPATH, "//span[text()='+']")
    BTN_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )

    def set_delay(self, seconds: str):
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_seven(self):
        self.driver.find_element(*self.BTN_7).click()

    def click_plus(self):
        self.driver.find_element(*self.BTN_PLUS).click()

    def click_eight(self):
        self.driver.find_element(*self.BTN_8).click()

    def click_equals(self):
        self.driver.find_element(*self.BTN_EQUALS).click()

    def get_result_after_wait(self, expected_value: str, timeout: int) -> str:
        # Ждем, пока в поле результата появится именно ожидаемое число (15)
        # Это защитит тест от падения во время 45-секундного ожидания
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.RESULT_SCREEN, expected_value)
        )
        return self.driver.find_element(*self.RESULT_SCREEN).text
