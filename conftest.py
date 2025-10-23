"""
conftest.py
-----------
This file configures pytest for running Appium-based mobile automation tests.
It provides command-line options, fixtures, and hooks to manage test execution
on both Android and iOS platforms, supporting both local and Sauce Labs targets.

Key Features:
- Custom pytest options for selecting platform and target (`--platform`, `--target`).
- Session-level fixtures for platform, target, and locator loading.
- Driver fixture that dynamically configures and launches an Appium driver.
- Integration with Sauce Labs to report job pass/fail status.
- Hook implementation to capture test outcomes.
"""

import pytest
from appium import webdriver
from utils.capabilities import (
    get_local_android_options, get_local_ios_options,
    get_sauce_android_options, get_sauce_ios_options
)
from utils.data_utility import LocatorManager


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        required=True,
        choices=["android", "ios"],
        help="Choose platform: android or ios"
    )
    parser.addoption(
        "--target",
        action="store",
        required=True,
        choices=["local", "sauce"],
        help="Choose execution target: local or sauce"
    )


@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform").lower()


@pytest.fixture(scope="session")
def target(request):
    return request.config.getoption("--target").lower()


@pytest.fixture(scope="session")
def locators(platform):
    """Load locators from Excel once per test session."""
    locator_manager = LocatorManager(platform, file_path="data/locator_master.xlsx")
    return locator_manager.locators


@pytest.fixture(scope="function")
def driver(platform, target, request):
    # Pick capabilities based on flags
    if platform == "android" and target == "local":
        options = get_local_android_options()
        url = "http://127.0.0.1:4723/wd/hub"

    elif platform == "ios" and target == "local":
        options = get_local_ios_options()
        url = "http://127.0.0.1:4723/wd/hub"

    elif platform == "android" and target == "sauce":
        options = get_sauce_android_options()
        url = "https://ondemand.us-west-1.saucelabs.com/wd/hub"

    elif platform == "ios" and target == "sauce":
        options = get_sauce_ios_options()
        url = "https://ondemand.us-west-1.saucelabs.com/wd/hub"

    else:
        raise ValueError(f"Unsupported combination: {platform}, {target}")

    driver = webdriver.Remote(url, options=options)
    yield driver

    # SauceLabs job status reporting
    if target == "sauce":
        outcome = "passed" if request.node.rep_call.passed else "failed"
        driver.execute_script("sauce:job-result={}".format(outcome))

    driver.quit()


# Hook to record test outcome (used for sauce:job-result)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
