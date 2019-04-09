from testsuites.base_testcase import BaseTestCase
import unittest
from apppageobjects.addonepage import AddOnePage
from apppageobjects.addtwopage import AddTwoPage
import time
class TestAdd(BaseTestCase):
    def test_add(self):
        time.sleep(5)
        addone=AddOnePage(self.driver)
        addone.addonefun("hello")

if __name__=="__main__":
    unittest.main(verbosity=2)
