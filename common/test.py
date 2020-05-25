# -*- coding: utf-8 -*-
# @Time    : 2020-5-25 14:09
# @Author  : suk
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
a = eval(("By" + ".ID"), "kw")

driver.find_element(a.send_keys("123"))
driver.find_element(eval("By" + ".ID"), "su").click()

driver.implicitly_wait(30)