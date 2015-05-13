'''
Created on May 12, 2015

@author: tester
'''
import time
import DriverLoad
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from DriverLoad import DriverLoad

d = DriverLoad("https://e-stempelki.pl/adminpanel/auth/login").importDriver()

assert "Stempelki" in d.title
login = d.find_element_by_id("login")
login.send_keys("robert@abastra.com")
    
password = d.find_element_by_id("passwd")
password.send_keys("Robert24")

messageBefore = d.find_element_by_class_name("form-message")
print messageBefore.text

buttonOK = d.find_element_by_name("submit_form")
buttonOK.click()

messageAfter = d.find_element_by_class_name("form-message")
print messageAfter.text

if ( messageAfter.text in "Login or password is incorrect." ): 
    d.close()
    d.quit()
else:
    assert "https://e-stempelki.pl/adminpanel/static/home/submit" in d.current_url()
    d.close()
    d.quit()