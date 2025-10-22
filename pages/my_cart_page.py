from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from pages.landing_page import LandingPage

class MyCartPage(BasePage):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)

    def proceed_to_checkout(self):
        self.utils.click(self.get_locator("my_cart_page_checkout_button"))
        return CheckoutPage(self.driver, self.locators)

    def remove_from_cart(self):
        self.utils.click(self.get_locator("my_cart_page_remove_item"))
        self.utils.is_visible(self.get_locator("my_cart_page_no_items"))
        self.utils.click(self.get_locator("my_cart_page_go_shopping_btn"))
        return LandingPage(self.driver, self.locators)
