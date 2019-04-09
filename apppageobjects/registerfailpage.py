from apppageobjects.basecase import Basecase
from selenium.webdriver.common.by import By
import time
class RegisterFailPage(Basecase):
    bookButton_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon")
    registerclick_loc=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    regiser_loc=(By.ID,"com.pdswp.su.smartcalendar:id/register")
    name_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    email_loc=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    pwd_loc=(By.ID,"com.pdswp.su.smartcalendar:id/password")
    regiserel_loc=(By.ID,"com.pdswp.su.smartcalendar:id/reguser")

    def registerfailfun(self,name,email,pwd):
        self.click(*self.bookButton_loc)
        self.click(*self.registerclick_loc)
        self.click(*self.regiser_loc)
        self.send_keys(name,*self.name_loc)
        self.send_keys(email,*self.email_loc)
        self.send_keys(pwd,*self.pwd_loc)
        self.click(*self.regiserel_loc)
        self.get_windows_img()