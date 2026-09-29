from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")
    TOTAL_PRICE_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill_user_data(self, first_name: str, last_name: str, zip_code: str):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_price(self) -> str:
        # Метод забирает строку вида "Total: $58.29"
        return self.driver.find_element(*self.TOTAL_PRICE_LABEL).text
