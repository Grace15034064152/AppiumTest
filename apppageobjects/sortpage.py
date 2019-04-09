from appium import webdriver
import os
from appium.webdriver.common.touch_action import TouchAction
from apppageobjects.basecase import Basecase
from appium.webdriver.common.mobileby import By
import time
class SortPage(Basecase):
    tag_loc= (By.NAME,"hello")
    sort_loc=(By.NAME,"排序")

    def sortfun(self):
        self.long_press(*self.tag_loc)
        time.sleep(10)
        self.click(*self.sort_loc)
        time.sleep(10)
        self.swipe(624,498,624,306,1000)
        self.get_windows_img()





