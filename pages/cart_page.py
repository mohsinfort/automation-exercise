from typing import List
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CartPage(BasePage):
    url = "https://automationexercise.com/view_cart"
    CART_ITEMS = (By.XPATH, '//div[contains(@class,"cart_info")]//tbody//tr')
    BUTTON_PROCEED_TO_CHECKOUT = (By.XPATH, '//a[contains(@class,"check_out")]')

    def is_opened(self) -> bool:
        return self.is_element_present(self.BUTTON_PROCEED_TO_CHECKOUT)

    def get_cart_items(self) -> List[WebElement]:
        return self.find_elements(self.CART_ITEMS)

    def is_product_in_cart(self) -> bool:
        return len(self.get_cart_items()) >= 1
