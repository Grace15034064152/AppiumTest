from testsuites.base_testcase import BaseTestCase
from apppageobjects.loginpage import LoginPage
import unittest
from framework.util import Util
import time
class TestLogin(BaseTestCase):
    def test_login(self):
        #登录成功
        time.sleep(10)
        util=Util()
        dic=util.read_excel("E:/pythonWorkplace/AppiumTest/data/data.xlsx","Sheet1")
        login=LoginPage(self.driver)
        login.loginfun(dic[0]["name"],dic[0]["password"])

if __name__=="__main__":
    unittest.main(verbosity=2)