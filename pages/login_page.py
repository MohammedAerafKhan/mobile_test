from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)

    def login(self):
        from pages.landing_page import LandingPage
        self.utils.scroll_to_element(self.get_locator("login_page_sample_username"))
        self.utils.click(self.get_locator("login_page_sample_username"))
        self.utils.scroll_to_element(self.get_locator("login_page_login_btn"))
        self.utils.click(self.get_locator("login_page_login_btn"))
        return LandingPage(self.driver, self.locators)
