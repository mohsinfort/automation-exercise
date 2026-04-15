import pytest

from pages.header import Header
from pages.modal import Modal
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class BaseCase:
    driver = None

    header = None
    modal = None
    home_page = None
    products_page = None
    cart_page = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver

        self.header = Header(driver=self.driver)
        self.modal = Modal(driver=self.driver)
        self.home_page = HomePage(driver=self.driver, open_on_init=True)
        self.products_page = ProductsPage(driver=self.driver)
        self.cart_page = CartPage(driver=self.driver)
