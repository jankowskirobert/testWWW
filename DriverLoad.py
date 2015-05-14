'''
Created on May 12, 2015

@author: tester
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class DriverLoad:
    'Return driver'

    def __init__(self, param):
        self.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",desired_capabilities={ "browserName": "firefox", "platform": "LINUX",})
        self.driver.get(param)

#         Remote(
#    command_executor='http://127.0.0.1:4445/wd/hub',
#    desired_capabilities=DesiredCapabilities.FIREFOX)
        
        
    def importDriver(self):
        return self.driver
        
    def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "destroyed"
        