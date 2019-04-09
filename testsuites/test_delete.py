from testsuites.base_testcase import BaseTestCase
import unittest
from apppageobjects.deletePage import DeletePage
import time
class TestDelete(BaseTestCase):
    def test_add(self):
        time.sleep(5)
        delete=DeletePage(self.driver)
        delete.deletefun()

if __name__=="__main__":
    unittest.main(verbosity=2)