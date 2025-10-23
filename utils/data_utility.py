"""
data_utility.py
---------------
This module defines the `LocatorManager` class, which is responsible for loading
UI element locators from an external Excel spreadsheet.

Rationale:
----------
To keep the framework **modular and maintainable**, all selectors have been
moved out of the Python code and into a central Excel file. This separation
ensures that:
- UI changes can be managed easily without editing code.
- Locators are data-driven and centralized.
- Android and iOS selectors are stored in **two separate sheets**, making it
  simple to support both platforms within the same test suite.

Excel File Structure:
---------------------
- File: `data/locator_master.xlsx`
- Each platform has its own sheet:
    - `android` → Contains locators specific to the Android app.
    - `ios` → Contains locators specific to the iOS app.
- Expected columns in each sheet:
    - `locator_name` → Logical name for the element (e.g., "login_button").
    - `locate_by` → Locator strategy (e.g., "id", "xpath", "accessibility_id").
    - `locator` → The actual locator string used to find the element.

P.S: User data such a username, password, Card Details, ect should also be stored in Excel
        so that we can test the interface with more data.
"""

import openpyxl

class LocatorManager:
    def __init__(self, platform, file_path="data/locator_master.xlsx"):
        platform = platform.lower()
        if platform == "android":
            self.platform = "android"
        elif platform == "ios":
            self.platform = "ios"
        else:
            raise ValueError(f"Unsupported platform: {platform}. Must be 'android' or 'ios'.")

        self.locators = self._load_locators(file_path)

    def _load_locators(self, file_path):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[self.platform]
        locators = {}

        # Assuming columns: page_name, locator_name, locate_by, locator
        for row in sheet.iter_rows(min_row=2, values_only=True):
            locator_name, locate_by, locator = row
            locators[locator_name] = {
                "locate_by": locate_by,
                "locator": locator
            }
        return locators
