'''
Created on May 12, 2015

@author: tester
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DriverLoad:
    'Return driver'

    def __init__(self, param):
        self.driver = webdriver.Firefox()
        self.driver.get(param)
        
    def importDriver(self):
        return self.driver
        
    def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "destroyed"
        