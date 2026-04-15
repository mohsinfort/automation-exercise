from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Modal(BasePage):
    MODAL_ELEMENT = (
        By.XPATH,
        '//ul[contains(@class, "navbar-nav")]//a[@href="/"]',
    )

    BUTTON_SUCCESS_MODAL = (
        By.XPATH,
        '//button[contains(@class,"btn-success")]',
    )

    def is_opened(self) -> bool:
        return self.is_element_present(self.MODAL_ELEMENT)

    def close_modal(self):
        successButton = self.find_clickable_element(self.BUTTON_SUCCESS_MODAL)
        successButton.click()
