from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    USER_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login_as(self, username, password):
        self.driver.find_element(*self.USER_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
