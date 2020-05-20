# -*- coding: utf-8 -*-
# @Time    : 2020-5-20 19:02
# @Author  : xjin
# @FileName: demo.py.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver =webdriver.Chrome()

driver.get("http://oa.ecidi.com/systemcenter/theme/newecidi/index.jsp")

driver.maximize_window()

# driver.implicitly_wait(30)

driver.find_element_by_id("username").send_keys("chen_m2")
driver.find_element_by_id("username").send_keys(Keys.TAB)
#driver.implicitly_wait(30)


sleep(5)

#driver.find_element_by_id("password").send_keys("chenm2test")

sleep(10)

# driver.implicitly_wait(30)


#driver.find_element_by_id("loginbtn").click()

#driver.quit()




