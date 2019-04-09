from appium import webdriver
import os
from appium.webdriver.common.touch_action import TouchAction
from apppageobjects.basecase import Basecase
from selenium.webdriver.common.by import By


class AddTwoPage(Basecase):
    bookButton_loc = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon")
    add_loc=(By.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text")
    content_loc = (By.ID, "com.pdswp.su.smartcalendar:id/add_input_content")
    submit_loc = (By.ID, "com.pdswp.su.smartcalendar:id/quick_add")

    def addtwofun(self, content):
        self.click(*self.bookButton_loc)
        self.click(*self.add_loc)
        self.send_keys(content, *self.content_loc)
        self.click(*self.submit_loc)
        self.get_windows_img()

