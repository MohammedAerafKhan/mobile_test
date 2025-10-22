import pytest
from appium import webdriver
from utils.capabilities import get_android_options, get_ios_options
from utils.data_utility import LocatorManager
from pytest_html import extras


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        required=True,
        choices=["android", "ios"],
        help="Choose platform: android or ios"
    )

@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform").lower()

@pytest.fixture(scope="session")
def locators(platform):
    """Load locators from Excel based on platform (once per test session)."""
    locator_manager = LocatorManager(platform, file_path="data/locator_master.xlsx")
    return locator_manager.locators

@pytest.fixture(scope="function")
def driver(platform):
    if platform == "android":
        options = get_android_options()
    elif platform == "ios":
        options = get_ios_options()
    else:
        raise ValueError(f"Unsupported platform: {platform}. Must be 'android' or 'ios'.")

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

