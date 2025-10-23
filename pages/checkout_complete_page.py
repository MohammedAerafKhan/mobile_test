from pages.base_page import BasePage
from pages.landing_page import LandingPage

class CheckoutCompletePage(BasePage):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)

    def continue_shopping(self):
        self.utils.scroll_to_element(self.get_locator("checkout_complete_page_continue_button"))
        self.utils.click(self.get_locator("checkout_complete_page_continue_button"))
        return LandingPage(self.driver, self.locators)
