from testsuites.base_testcase import BaseTestCase
from apppageobjects.loginpage import LoginPage
import unittest
from framework.util import Util
from apppageobjects.addonepage import AddOnePage
from apppageobjects.searchpage import SearchPage
import time
class TestSearch(BaseTestCase):
    def test_search(self):
        time.sleep(10)
        search=SearchPage(self.driver)
        search.searchfun("hello")

if __name__=="__main__":
    unittest.main(verbosity=2)


