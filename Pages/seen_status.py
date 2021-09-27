from Locator.locators import Locators


class SeenStatus:
    def __init__(self, driver):
        self.driver = driver
        self.seen_status = Locators.seen_xpath

    def is_seen(self):
        btn = self.driver.find_element_by_xpath(self.seen_status).text()
        aria_label = btn.find_element_by_css_selector('span').get_attribute("aria-label")
        print(aria_label)
