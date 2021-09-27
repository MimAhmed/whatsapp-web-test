from Locator.locators import Locators
from selenium.webdriver.common.keys import Keys


class SendMessage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = Locators.search_field_xpath
        self.number_input = Locators.search_field_xpath
        self.click_on_number = Locators.target_number_xpath
        self.message_field = Locators.message_box_xpath

        self.seen_status = Locators.seen_xpath

    def click_search_bar(self):
        self.driver.find_element_by_xpath(self.search_bar).click()

    def search_number(self, contact):
        self.driver.find_element_by_xpath(self.search_bar).send_keys(contact)

    def click_number_filed(self):
        self.driver.find_element_by_xpath(self.click_on_number).click()

    def send_message(self):
        message_box = self.driver.find_element_by_xpath(self.message_field)
        message_box.send_keys("Hello.Testing")
        message_box.send_keys(Keys.ENTER)

    def write_excel(self):
        pass

    # def is_seen(self):
    #     btn = self.driver.find_element_by_xpath(self.seen_status)
    #     aria_label = btn.find_element_by_css_selector('span').get_attribute("aria-label")
    #     print(aria_label)



