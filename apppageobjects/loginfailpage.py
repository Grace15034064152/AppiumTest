from appium import webdriver
import os
from appium.webdriver.common.touch_action import TouchAction
from apppageobjects.basecase import Basecase
from appium.webdriver.common.mobileby import By
import time
class LoginPage(Basecase):
    bookButton_loc = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon")
    login_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    name_loc=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    pwd_loc=(By.ID,"com.pdswp.su.smartcalendar:id/password")
    loginbutton_loc=(By.ID,"com.pdswp.su.smartcalendar:id/login")

    def loginfun(self,name,password):
        self.click(*self.bookButton_loc)
        self.click(*self.login_loc)
        self.send_keys(name,*self.name_loc)
        self.send_keys(password,*self.pwd_loc)
        self.click(*self.loginbutton_loc)
        self.get_windows_img()




