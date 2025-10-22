from pages.base_page import BasePage
from pages.my_cart_page import MyCartPage

class ProductPage(BasePage):
    def __init__(self, driver, locators):
        super().__init__(driver, locators)

    def add_to_cart(self):
        self.utils.click(self.get_locator("product_page_add_to_cart_button"))
        return self

    def go_to_cart(self):
        self.utils.click(self.get_locator("product_page_cart_icon"))
        return MyCartPage(self.driver, self.locators)
