import pytest
from pages.landing_page import LandingPage
from utils.logger import get_logger

logger = get_logger()

def test_add_remove_from_cart(driver, locators):
    logger.info("Starting add remove from cart test")

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

    cart.remove_from_cart()

    assert landing.is_loaded(), "Landing page not visible after order completion"
    logger.info("Checkout flow test completed successfully")
