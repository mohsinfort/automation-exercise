from typing import Optional, List, Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    url = "https://www.automationexercise.com/"
    driver = None
    wait_timeout = 5

    def __init__(
        self,
        driver: WebDriver,
        url: Optional[str] = None,
        open_on_init: bool = False,
    ):
        self.driver = driver
        self.url = url or self.url

        if open_on_init:
            self.open(self.url)

    def wait(self, timeout: int = None) -> WebDriverWait:
        """
        Explicit Waits Setup
        :param timeout:  max time to wait for the element (in seconds)
        :
        :return: WebDriverWait
        """
        if timeout is None:
            timeout = self.wait_timeout
        return WebDriverWait(driver=self.driver, timeout=timeout)

    def find_element(self, locator: Tuple[str, str], timeout: int = None) -> WebElement:
        """
        Find element by locator
        :param locator: Tuple (By, selector)
        :param timeout:  max time to wait for the element (in seconds)
        :
        :return: WebElement
        """
        return self.wait(timeout=timeout).until(EC.presence_of_element_located(locator))

    def find_clickable_element(
        self, locator: Tuple[str, str], timeout: int = None
    ) -> WebElement:
        """
        Find clickable element by locator
        :param locator: Tuple (By, selector)
        :param timeout:  max time to wait for the element (in seconds)
        :
        :return: WebElement
        """
        return self.wait(timeout=timeout).until(EC.element_to_be_clickable(locator))

    def find_elements(
        self, locator: Tuple[str, str], timeout: int = None
    ) -> List[WebElement]:
        """
        FInd multiple elements by their locator
        :param locator: Tuple (By, selector)
        :param timeout:  max time to wait for the element (in seconds)
        :
        :return: List[WebElement]
        """
        return self.wait(timeout=timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def is_element_present(self, locator: Tuple[str, str], timeout: int = None) -> bool:
        """
        Check if element is present
        :param locator: Tuple (By, selector)
        :param timeout: max time to wait for the element (in seconds)
        :
        :return: bool
        """
        try:
            self.find_element(locator=locator, timeout=timeout)
        except TimeoutException:
            return False
        return True

    def open(self, url: str):
        """
        Open the given URL in the browser.
        """
        self.driver.get(url)

    def type_text(self, locator: Tuple[str, str], inputText: str, timeout: int = None):
        """
        Enter text into an input field after clearing it.

        :param locator: Tuple (By, selector) to locate element
        :param inputText: Text value to input
        :param timeout:  max time to wait for the element (in seconds)
        """
        element = self.wait(timeout=timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(inputText)

    def get_element_text(self, locator: Tuple[str, str], timeout: int = None) -> str:
        """
        Retrieve visible text from an element.

        :param locator: Tuple (By, selector) to locate element
        :param timeout:  max time to wait for the element (in seconds)
        :return: Element text as string
        """
        return (
            self.wait(timeout=timeout)
            .until(EC.visibility_of_element_located(locator))
            .text
        )
