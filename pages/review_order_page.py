from pages.base_page import BasePage
from pages.checkout_complete_page import CheckoutCompletePage

class ReviewOrderPage(BasePage):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)

    def place_order(self):
        self.utils.scroll_to_element(self.get_locator("review_order_page_place_order_button"))
        self.utils.click(self.get_locator("review_order_page_place_order_button"))
        return CheckoutCompletePage(self.driver, self.locators)
