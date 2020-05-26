# -*- coding: utf-8 -*-
# @Time    : 2020-5-25 14:09
# @Author  : suk
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://oa.simulate.com:8080/systemcenter/theme/newecidi/loginform.html")
driver.maximize_window()



sleep(3)
driver.find_element(eval("By" + ".ID"), "password").clear()
driver.find_element(eval("By" + ".ID"), "password").send_keys("chenl3test")
sleep(5)
driver.find_element(eval("By.ID"), "username").send_keys("chen_l3")
driver.find_element(eval("By" + ".ID"), "loginbtn").click()
sleep(5)

By.PARTIAL_LINK_TEXT
driver.implicitly_wait(30)
driver.quit()