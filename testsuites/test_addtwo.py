from testsuites.base_testcase import BaseTestCase
import unittest
from apppageobjects.addonepage import AddOnePage
from apppageobjects.addtwopage import AddTwoPage
import time

class TestAddTwo(BaseTestCase):
    def test_addtwo(self):
        # addone = AddOnePage(self.driver)
        # addone.addonefun("hello")
        time.sleep(5)
        addtwo = AddTwoPage(self.driver)
        addtwo.addtwofun("world")


if __name__ == "__main__":
    unittest.main(verbosity=2)