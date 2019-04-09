from apppageobjects.basecase import Basecase
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.touch_action import TouchAction
import time
class FilePage(Basecase):
    content_loc=(By.ID,"com.pdswp.su.smartcalendar:id/note_title")
    filebutton_loc=(By.NAME,"归档")
    bookButton_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon")
    file_loc=(By.ID,"com.pdswp.su.smartcalendar:id/note_time")
    recover_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu")
    def filefun(self):
        self.long_press(*self.content_loc)
        self.click(*self.filebutton_loc)
        self.click(*self.bookButton_loc)
        self.click(*self.file_loc)
        self.swipe(629,111,530,111,1000)
        self.click(*self.recover_loc)
        self.get_windows_img()

