from Locator.locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = Locators.search_field_xpath
        self.number_input = Locators.search_field_xpath

    def click_search_bar(self):
        self.driver.find_element_by_xpath(self.search_bar).click()

    def search_number(self, contact):
        self.driver.find_element_by_xpath(self.search_bar).send_keys(contact)
