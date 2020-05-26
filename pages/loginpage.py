# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 16:15
# @Author  : suk
# @FileName: loginpage.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/

from pages.basepage import BasePage
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, base_url):
        super().__init__()
        super().open(base_url)

    def type_username(self, loc_type, attr_name, username):
        # self.driver.find_element(username_loc).clear()
        self.find_element(eval(loc_type), attr_name).send_keys(username)

    def type_password(self, loc_type, attr_name, password):
        # pass
        # self.driver.find_element(password_loc).clear()
        self.find_element(eval(loc_type), attr_name).send_keys(password)

    def submit(self, loc_type, attr_name):
        # pass
        self.find_element(eval(loc_type), attr_name).click()

