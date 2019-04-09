from testsuites.base_testcase import BaseTestCase
from apppageobjects.loginpage import LoginPage
import unittest
from framework.util import Util
from apppageobjects.registerfailpage import RegisterFailPage
class TestRegister(BaseTestCase):
    def test_register(self):
        #登录成功
        util=Util()
        dic=util.read_excel("E:/pythonWorkplace/AppiumTest/data/data.xlsx","Sheet1")
        login=LoginPage(self.driver)
        login.loginfun(dic[0]["name"],dic[0]["password"])
        #登录失败
        # registerfail=RegisterFailPage(self.driver)
        # registerfail.registerfailfun("admin","1130489267@qq.com","123456")
if __name__=="__main__":
    unittest.main(verbosity=2)