from appium import webdriver
import os
from appium.webdriver.common.touch_action import TouchAction
from apppageobjects.basecase import Basecase
from appium.webdriver.common.mobileby import By

class SearchPage(Basecase):
    search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_search")
    content_loc=(By.ID,"android:id/search_src_text")

    def searchfun(self,content):
        self.click(*self.search_loc)
        self.send_keys(content,*self.content_loc)
        self.driver.keyevent(66)
        self.get_windows_img()





