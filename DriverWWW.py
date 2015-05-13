
'''
Created on May 12, 2015

@author: Robert
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

def driverConnect():
    return webdriver.Firefox()

def test_driverConnect():
    assert test_driverConnect() == webdriver.Firefox()