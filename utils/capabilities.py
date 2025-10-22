from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

def get_android_options():
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

def get_ios_options():
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
