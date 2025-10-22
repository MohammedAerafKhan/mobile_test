from utils.utils import DriverUtils
from appium.webdriver.common.appiumby import AppiumBy


class BasePage:
    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators
        self.utils = DriverUtils(driver)

    def get_locator(self, locator_name):
        locator_info = self.locators.get(locator_name)
        if not locator_info:
            raise ValueError(f"Locator '{locator_name}' not found in Excel for {self.__class__.__name__}")

        strategy = locator_info["locate_by"].strip().lower().replace("_", " ")

        # Map to Selenium/Appium By constants
        by_map = {
            "id": AppiumBy.ID,
            "xpath": AppiumBy.XPATH,
            "accessibility id": AppiumBy.ACCESSIBILITY_ID,
            "class name": AppiumBy.CLASS_NAME,
            "name": AppiumBy.NAME,
        }

        by_value = by_map.get(strategy)
        if not by_value:
            raise ValueError(f"Unsupported locator strategy: {strategy}")

        return by_value, locator_info["locator"]