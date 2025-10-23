import pytest
from pages.landing_page import LandingPage
from utils.logger import get_logger

logger = get_logger()

def test_checkout_flow(driver, locators):
    logger.info("Starting Checkout Flow Test")

    landing = LandingPage(driver, locators)
    login = landing.go_to_login()
    logger.info("Navigated to Login Page")

    landing = login.login()
    logger.info("Login submitted with test credentials")

    assert landing is not None, "Landing page did not load after login"
    logger.info("Landing page loaded successfully")

    product = landing.select_first_product()
    logger.info("Selected first product")

    cart = product.add_to_cart().go_to_cart()
    logger.info("Product added to cart and navigated to cart page")

    checkout = cart.proceed_to_checkout()
    logger.info("Proceeded to checkout")

    payment = checkout.fill_details("Test User", "Test address", "Test City", "T1E5T0", "Canada")
    logger.info("Filled user details")

    review = payment.enter_payment("Test User", "4876024750235", "06/21", "123")
    logger.info("Entered payment details")

    complete = review.place_order()
    logger.info("Placed the order")

    complete.continue_shopping()
    logger.info("Continued shopping after order completion")

    assert landing.is_loaded(), "Landing page not visible after order completion"
    logger.info("Checkout flow test completed successfully")
