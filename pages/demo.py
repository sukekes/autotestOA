# -*- coding: utf-8 -*-
# @Time    : 2020-5-20 19:02
# @Author  : suk
# @FileName: demo.py.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.remote.webelement import WebElement


# 家里电脑找不到Chromedriver路径，加上路径，Chrome非默认路径安装的问题？？？
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

driver.get("http://oa.simulate.com:8080/systemcenter/theme/newecidi/index.jsp#")

driver.maximize_window()

# driver.implicitly_wait(30)
# driver.find_element_by_id("username").clear()
#
# driver.find_element_by_id("username").send_keys("chen_m2")
# driver.find_element_by_id("username").send_keys(Keys.TAB)
# driver.implicitly_wait(30)
a = driver.find_element_by_id("username")

print(a.id)

# print(type(a))
# print(help(WebElement))
#
# sleep(5)
# driver.find_element_by_id("dsd").send_keys("chen_l3")
# driver.find_element_by_id("password").send_keys("chenl3test")


# driver.implicitly_wait(30)


# driver.find_element_by_id("loginbtn").click()

driver.quit()
