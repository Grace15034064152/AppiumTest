from appium import webdriver
import os
from appium.webdriver.common.touch_action import TouchAction
from apppageobjects.basecase import Basecase
from appium.webdriver.common.mobileby import By

class DeletePage(Basecase):
    content_loc=(By.ID,"com.pdswp.su.smartcalendar:id/note_title")
    delete_loc=(By.NAME,"删除备忘")
    bookButton_loc = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon")
    recycle_loc=(By.NAME,"回收站")
    clear_loc=(By.ID,"com.pdswp.su.smartcalendar:id/button")
    submit_loc=(By.NAME,"确定")

    def deletefun(self):
        self.long_press(*self.content_loc)
        self.click(*self.delete_loc)
        self.click(*self.bookButton_loc)
        self.click(*self.recycle_loc)
        self.click(*self.clear_loc)
        self.click(*self.submit_loc)
        self.get_windows_img()




