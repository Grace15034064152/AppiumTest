from testsuites.base_testcase import BaseTestCase
from apppageobjects.registerfailpage import RegisterFailPage
import unittest

class TestRegister(BaseTestCase):
    def test_register(self):
        # #注册成功
        # register=RegisterPage(self.driver)
        # register.registerfun("admin","1130489267@qq.com","1234567")
        # 注册失败
        registerfail=RegisterFailPage(self.driver)
        registerfail.registerfailfun("admin","1130489267@qq.com","123456")
if __name__=="__main__":
    unittest.main(verbosity=2)
