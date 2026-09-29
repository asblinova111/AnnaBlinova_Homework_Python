from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    # Ищем кнопки добавления по атрибутам data-test,
    # это самые стабильные селекторы
    ADD_BACKPACK = (
        By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']"
        )
    ADD_TSHIRT = (
        By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
        )
    ADD_ONESIE = (
        By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-onesie']"
        )
    CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_required_products(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()
        self.driver.find_element(*self.ADD_TSHIRT).click()
        self.driver.find_element(*self.ADD_ONESIE).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()
