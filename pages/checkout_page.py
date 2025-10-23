from pages.base_page import BasePage
from pages.payment_page import PaymentPage

class CheckoutPage(BasePage):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)

    def fill_details(self, name, address, city, postal_code, country):
        self.utils.type(self.get_locator("checkout_page_name"), name)
        self.utils.type(self.get_locator("checkout_page_address"), address)

        self.utils.scroll_to_element(self.get_locator("checkout_page_postal_code"))

        self.utils.type(self.get_locator("checkout_page_city"), city)
        self.utils.type(self.get_locator("checkout_page_postal_code"), postal_code)

        self.utils.scroll_to_element(self.get_locator("checkout_page_continue_button"))

        self.utils.type(self.get_locator("checkout_page_country"), country)
        self.utils.click(self.get_locator("checkout_page_continue_button"))

        return PaymentPage(self.driver, self.locators)
