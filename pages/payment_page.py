from pages.base_page import BasePage
from pages.review_order_page import ReviewOrderPage

class PaymentPage(BasePage):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)

    def enter_payment(self, card_name, card_number, expiry, cvv):
        self.utils.type(self.get_locator("payment_page_card_name"), card_name)
        self.utils.type(self.get_locator("payment_page_card_number"), card_number)

        # Click and scroll
        self.utils.click(self.get_locator("payment_page_checkout_title"))
        self.utils.scroll_to_element(self.get_locator("payment_page_cvv"))

        self.utils.type(self.get_locator("payment_page_expiry"), expiry)
        self.utils.type(self.get_locator("payment_page_cvv"), cvv)

        # Click and scroll
        self.utils.click(self.get_locator("payment_page_expiration_title"))
        self.utils.scroll_to_element(self.get_locator("payment_page_continue_button"))

        self.utils.click(self.get_locator("payment_page_continue_button"))
        return ReviewOrderPage(self.driver, self.locators)
