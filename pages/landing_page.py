from pages.base_page import BasePage

class LandingPage(BasePage):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)

    def go_to_login(self):
        from pages.login_page import LoginPage
        self.utils.click(self.get_locator("landing_page_menu_btn"))
        self.utils.click(self.get_locator("landing_page_login_menu_item"))
        return LoginPage(self.driver, self.locators)

    def select_first_product(self):
        from pages.product_page import ProductPage
        self.utils.click(self.get_locator("landing_page_first_product"))
        return ProductPage(self.driver, self.locators)

    def is_loaded(self):
        return self.utils.is_visible(self.get_locator("landing_page_title"))
