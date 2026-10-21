from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def click_checkout(self) -> None:
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
