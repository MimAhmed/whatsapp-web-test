from Locator.locators import Locators


class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.three_icon_location = Locators.thee_dot_button_xpath
        self.logout_location = Locators.logout_xpath

    def click_three_icon(self):
        self.driver.find_element_by_xpath(self.three_icon_location).click()

    def logout_account(self):
        self.driver.find_element_by_xpath(self.logout_location).click()


