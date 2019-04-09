import yaml
from appium import webdriver
from framework.logger import Logger
import os.path
#创建一个日志记录器实例
logger=Logger(logger="BrowserEngin").getlog()


class BrowserEngin(object):

    def appium_desired(self):
        path = os.path.dirname(os.path.abspath("."))
        print(path)
        with open(path+'\config\config.yaml', 'r', encoding='utf-8') as file:
            data = yaml.load(file)
        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['sessionOverride'] = data['sessionOverride']
        desired_caps['app'] = path+data['app']
        desired_caps['noReset'] = data['noReset']
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        return driver

if __name__ == '__main__':
    browser=BrowserEngin()
    browser.appium_desired()
