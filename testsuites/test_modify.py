from testsuites.base_testcase import BaseTestCase
from apppageobjects.modifynamepage import ModifyName
import unittest
import time
class TestModify(BaseTestCase):
    def test_modify(self):
        #修改用户名
        time.sleep(10)
        modify=ModifyName(self.driver)
        modify.modifyfun("admin111")
if __name__=="__main__":
    unittest.main(verbosity=2)