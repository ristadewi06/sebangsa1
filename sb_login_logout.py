#import nose
import unittest
import xmlrunner
from time import sleep 
from unittest import TestCase
from selenium import webdriver
from nose.plugins.attrib import attr
from selenium.webdriver.common.by import By
from locators import *

class nosetest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        options = webdriver.ChromeOptions() #script  headless 
        options.add_argument('headless')    #script  headless 
        #self.driver = webdriver.Chrome('/home/okky/Documents/automated/nosetest/chromedriver',chrome_options=options ) #script  headless , script options untuk tanpa membuka google chrome
        self.driver = webdriver.Chrome('chromedriver') #script bukan headless
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("https://sebangsa4.jog.ojodowo.com/")

    @attr(speed='fast')
    def test(self):

        #login
        self.driver.find_element(By.XPATH,locator.button_formlogin1).click()
        self.driver.find_element(By.XPATH,locator.form_login)
        self.driver.find_element(By.XPATH,locator.field_nama_akun).send_keys('userdua')
        self.driver.find_element(By.XPATH,locator.field_password).send_keys('qwerty')
        self.driver.find_element(By.XPATH,locator.button_masuk).click()
        sleep(5)
        self.driver.get_screenshot_as_file("login.png")

        #logout
        self.driver.find_element(By.XPATH,locator.avaprofil).click()
        sleep(5)
        self.driver.find_element(By.XPATH,locator.dropdown_ava)
        self.driver.find_element(By.XPATH,locator.logout).click()
        sleep(5)
        self.driver.get_screenshot_as_file("logout.png")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
