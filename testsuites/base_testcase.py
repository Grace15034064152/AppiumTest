import unittest
from framework.browser_engine import BrowserEngin
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngin()
        self.driver=browser.appium_desired()
        print("start")
    def tearDown(self):
        self.driver.quit()
        print("end")





