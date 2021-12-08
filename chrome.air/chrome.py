# -*- encoding=utf8 -*-
__author__ = "19617"

from airtest.core.api import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
driver = WebChrome()
driver.implicitly_wait(20)

driver.get("https://airlab-gl.163.com/b2b")

driver.maximize_window()


driver.switch_to_new_tab()

driver.switch_to_previous_tab()

driver.quit()