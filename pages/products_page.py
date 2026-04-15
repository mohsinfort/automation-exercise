from typing import List
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class ProductsPage(BasePage):
    url = "https://www.automationexercise.com/products"

    PRODUCT_CARD = (By.XPATH, '//div[@class="product-image-wrapper"]')
    BUTTON_VIEW_PRODUCT = (
        By.XPATH,
        '//div[@class="product-image-wrapper"]'
        '//a[contains(@href, "product_details")]',
    )
    BUTTON_ADD_TO_CART = (
        By.XPATH,
        '//div[@class="product-image-wrapper"]'
        '//div[contains(@class, "productinfo")]'
        '//a[contains(@class, "add-to-cart")]',
    )
    INPUT_SEARCH_PRODUCT = (By.XPATH, '//input[@id="search_product"]')
    BUTTON_SEARCH_PRODUCT = (By.XPATH, '//button[@id="submit_search"]')

    def is_opened(self) -> bool:
        return self.is_element_present(self.PRODUCT_CARD)

    def view_product(self, productIndex: int = 0):
        view_product_buttons = self.find_elements(self.BUTTON_VIEW_PRODUCT)
        view_product_buttons[productIndex].click()

    def get_products_list(self) -> List[WebElement]:
        return self.find_elements(self.PRODUCT_CARD)

    def search_product(self, productName: str):
        input_search = self.find_element(self.INPUT_SEARCH_PRODUCT)
        input_search.clear()
        input_search.send_keys(productName)
        self.find_element(self.BUTTON_SEARCH_PRODUCT).click()

    def add_product_to_cart(self, productIndex: int = 0):
        add_product__to_cart_buttons = self.find_elements(self.BUTTON_ADD_TO_CART)
        add_product__to_cart_buttons[productIndex].click()
