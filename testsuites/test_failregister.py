from testsuites.base_testcase import BaseTestCase
from apppageobjects.registerfailpage import RegisterFailPage
import unittest
import time

class TestFailRegister(BaseTestCase):
    def test_register(self):
        # 注册失败
        time.sleep(5)
        registerfail=RegisterFailPage(self.driver)
        registerfail.registerfailfun("admin","1130489267@qq.com","1234567")
if __name__=="__main__":
    unittest.main(verbosity=2)
