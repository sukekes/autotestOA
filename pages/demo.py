# -*- coding: utf-8 -*-
# @Time    : 2020-5-20 19:02
# @Author  : suk
# @FileName: demo.py.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.remote.webelement import WebElement


# 家里电脑找不到Chromedriver路径，加上路径，Chrome非默认路径安装的问题？？？
driver = webdriver.Chrome()

driver.get("http://oa.simulate.com:8080/systemcenter/theme/newecidi/index.jsp")

driver.maximize_window()

# driver.implicitly_wait(30)
# driver.find_element_by_id("username").clear()
#
# driver.find_element_by_id("username").send_keys("chen_m2")
# driver.find_element_by_id("username").send_keys(Keys.TAB)
# driver.implicitly_wait(30)
driver.find_element_by_id("username").send_keys("chen_m2")
driver.find_element_by_id("password").send_keys("chenm2test")
driver.find_element_by_id("loginbtn").click()
driver.implicitly_wait(20)

# driver.find_element_by_partial_link_text("我的任务").click()
# driver.find_element_by_partial_link_text("论文专著").click()
# driver.find_element_by_partial_link_text("我的用例").click()

driver.find_element_by_partial_link_text("个人办公").click()
By.PARTIAL_LINK_TEXT


sleep(3)


# print(type(a))
# print(help(WebElement))
#
# sleep(5)
# driver.find_element_by_id("dsd").send_keys("chen_l3")
# driver.find_element_by_id("password").send_keys("chenl3test")


# driver.implicitly_wait(30)


# driver.find_element_by_id("loginbtn").click()

driver.quit()
