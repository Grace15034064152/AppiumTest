from apppageobjects.basecase import Basecase
from appium.webdriver.common.mobileby import By
import time
class RegisterPage(Basecase):
    bookButton_loc=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon")
    registerclick_loc=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    regiser_loc=(By.ID,"com.pdswp.su.smartcalendar:id/register")
    name_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    email_loc=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    pwd_loc=(By.ID,"com.pdswp.su.smartcalendar:id/password")
    regiserel_loc=(By.ID,"com.pdswp.su.smartcalendar:id/reguser")

    def registerfun(self,name,email,pwd):
        time.sleep(5)
        self.click(*self.bookButton_loc)
        self.click(*self.registerclick_loc)
        self.click(*self.regiser_loc)
        self.send_keys(name,*self.name_loc)
        self.send_keys(email,*self.email_loc)
        self.send_keys(pwd,*self.pwd_loc)
        self.click(*self.regiserel_loc)
        self.get_windows_img()