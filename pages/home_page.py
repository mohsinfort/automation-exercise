from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    url = "https://www.automationexercise.com/"
    SLIDER_CAROUSEL = (By.XPATH, '//div[@id="slider-carousel"]')

    def is_opened(self) -> bool:
        return self.is_element_present(self.SLIDER_CAROUSEL)
