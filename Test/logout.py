from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from Pages.logout_account import Logout
from Locator import locators


class SearchField(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/driver/chromedriver_win32_93/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_001_logout(self):
        driver = self.driver
        driver.get(locators.BASE_URl)
        logout = Logout(driver)
        logout.click_three_icon()
        time.sleep(2)
        logout.logout_account()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Joy/PycharmProjects/WhatsAppTest/Report'))
