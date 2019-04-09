from testsuites.base_testcase import BaseTestCase
from apppageobjects.loginpage import LoginPage
import unittest
from apppageobjects.addonepage import AddOnePage
from apppageobjects.filepage import FilePage
import time
class TestFile(BaseTestCase):
    #归档
    def test_file(self):
        time.sleep(10)
        file=FilePage(self.driver)
        file.filefun()

if __name__=="__main__":
    unittest.main(verbosity=2)