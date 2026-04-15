from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Header(BasePage):
    HOME_LINK = (
        By.XPATH,
        '//ul[contains(@class, "navbar-nav")]//a[@href="/"]',
    )
    PRODUCTS_LINK = (
        By.XPATH,
        '//ul[contains(@class, "navbar-nav")]//a[@href="/products"]',
    )
    CART_LINK = (
        By.XPATH,
        '//ul[contains(@class, "navbar-nav")]//a[@href="/view_cart"]',
    )

    def navigate_to_home(self):
        self.find_clickable_element(self.HOME_LINK).click()

    def navigate_to_products(self):
        self.find_clickable_element(self.PRODUCTS_LINK).click()

    def navigate_to_cart(self):
        self.find_clickable_element(self.CART_LINK).click()

    # add other navigation options
