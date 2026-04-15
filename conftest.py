import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")


@pytest.fixture(scope="session")
def config(request: pytest.FixtureRequest):
    """
    Set up browser configuration for the test session.

    Reads CLI inputs like browser type and headless mode, prepares the
    appropriate browser options, and returns everything needed to
    initialize the WebDriver.

    :param request: Pytest request object to read CLI arguments
    :return: Configuration dictionary for browser setup
    """
    browser: str = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    options = None

    if browser.lower() == "chrome":
        options = ChromeOptions()
    # add other supported browsers here
    else:
        raise ValueError(f"Browser {browser} is not supported yet!")

    options.add_argument("--window-size=1920,1080")

    if headless:
        options.add_argument("-headless")

    return {
        "driver": driver,
        "browser": browser,
        "headless": headless,
        "options": options,
    }


@pytest.fixture(scope="function")
def driver(config):
    """
    Initializes and manages the WebDriver for each test.

    Launches a browser instance based on the provided configuration and ensures
    it is properly closed after the test completes.

    :param config: Dictionary containing browser setup details
    :yield: WebDriver instance for test execution
    """
    driver = None
    browser = config.get("browser")
    options = config.get("options")

    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
    # elif browser == "xyz":
    # handle other supported browsers

    yield driver

    if driver:
        driver.quit()
