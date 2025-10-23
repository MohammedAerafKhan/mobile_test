"""
utils.py
--------
Contains the `DriverUtils` class, which wraps common Selenium/Appium
interactions with built-in waiting mechanisms for reliability.

Key Features:
- Encapsulates element interactions like click, type, visibility checks.
- Provides explicit waits to handle dynamic UI elements.
- Includes functionality for swipe/scroll to locate elements.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DriverUtils:
    """
    Utility wrapper for WebDriver to simplify element interactions
    with built-in waits and retry mechanisms.
    """

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def type(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        return element

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def scroll_to_element(self, locator, max_swipes=5):
        for _ in range(max_swipes):
            try:
                element = self.wait.until(EC.presence_of_element_located(locator))
                if element.is_displayed():
                    return element
            except:
                self._swipe_up()
        raise Exception(f"Element {locator} not found after scrolling")

    def _swipe_up(self):
        size = self.driver.get_window_size()
        start_y = int(size["height"] * 0.8)
        end_y = int(size["height"] * 0.3)
        x = int(size["width"] / 2)
        self.driver.swipe(x, start_y, x, end_y, 800)
