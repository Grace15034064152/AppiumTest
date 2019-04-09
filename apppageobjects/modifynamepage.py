from appium import webdriver
import os
from appium.webdriver.common.touch_action import TouchAction
from apppageobjects.basecase import Basecase
from selenium.webdriver.common.by import By
class ModifyName(Basecase):
    bookButton_loc = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon")
    registerclick_loc = (By.ID, "com.pdswp.su.smartcalendar:id/email")
    modify_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    name_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    submit_loc=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")

    def modifyfun(self,name):
        self.click(*self.bookButton_loc)
        self.click(*self.registerclick_loc)
        self.click(*self.modify_loc)
        self.send_keys(name,*self.name_loc)
        self.click(*self.submit_loc)
        self.get_windows_img()
