"""
capabilities.py
---------------
This module centralizes the definition of Appium capabilities for both local
and remote (Sauce Labs) test execution. It allows switching between Android
and iOS platforms as well as execution targets with minimal changes.

Environment:
- Reads Sauce Labs credentials (`SAUCE_USERNAME`, `SAUCE_ACCESS_KEY`)
  from a `.env` file using `python-dotenv`.

Key Features:
- Provides local capabilities for Android (UiAutomator2) and iOS (XCUITest).
- Provides Sauce Labs capabilities for Android and iOS.
- Encapsulates configuration logic in functions for easier reuse.

Usage Example:
--------------
```python
from utils.capabilities import get_local_android_options
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=get_local_android_options())
"""


from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
import os
from dotenv import load_dotenv

load_dotenv()

SAUCE_USERNAME = os.getenv("SAUCE_USERNAME")
SAUCE_ACCESS_KEY = os.getenv("SAUCE_ACCESS_KEY")


# ========== LOCAL CAPABILITIES ==========
def get_local_android_options():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "platformVersion": "12",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "app": "/Users/aerafkhan/Desktop/Seneca/my-demo-app-android-main/app/build/outputs/apk/debug/app-debug.apk",
        "newCommandTimeout": 300,
        "autoGrantPermissions": True
    })
    return options


def get_local_ios_options():
    options = XCUITestOptions().load_capabilities({
        "platformName": "iOS",
        "platformVersion": "26.0",
        "deviceName": "iPhone 17 Pro",
        "automationName": "XCUITest",
        "app": "/Users/aerafkhan/Library/Developer/Xcode/DerivedData/My_Demo_App-bftxznsdkfiecjhlchguqckvrlzr/Build/Products/Debug-iphonesimulator/My Demo App.app",
        "newCommandTimeout": 300,
        "connectHardwareKeyboard": True
    })
    return options


# ========== SAUCE LABS CAPABILITIES ==========

def get_sauce_android_options():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "appium:platformVersion": "12.0",
        "appium:deviceName": "Android GoogleAPI Emulator",
        "appium:automationName": "UiAutomator2",
        "appium:app": "storage:filename=mda-2.2.0-25.apk",
        "sauce:options": {
            "username": SAUCE_USERNAME,
            "accessKey": SAUCE_ACCESS_KEY,
            "build": "appium-build-android-final",
            "name": "Android Checkout Flow",
            "deviceOrientation": "PORTRAIT"
        }
    })
    return options


def get_sauce_ios_options():
    options = XCUITestOptions().load_capabilities({
        "platformName": "iOS",
        "appium:platformVersion": "16",
        "appium:deviceName": "iPhone 14 Simulator",
        "appium:automationName": "XCUITest",
        "appium:app": "storage:filename=SauceLabs-Demo-App-Runner.Simulator.XCUITest.zip",
        "sauce:options": {
            "username": SAUCE_USERNAME,
            "accessKey": SAUCE_ACCESS_KEY,
            "build": "appium-build-ios-final",
            "name": "iOS Checkout Flow",
            "deviceOrientation": "PORTRAIT"
        }
    })
    return options
