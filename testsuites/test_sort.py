from testsuites.base_testcase import BaseTestCase
import unittest
from apppageobjects.sortpage import SortPage
import time

class TestSort(BaseTestCase):
    def test_sort(self):
        time.sleep(10)
        sort=SortPage(self.driver)
        sort.sortfun()
if __name__=="__main__":
    unittest.main(verbosity=2)