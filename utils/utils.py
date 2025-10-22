from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DriverUtils:
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
