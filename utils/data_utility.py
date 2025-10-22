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
