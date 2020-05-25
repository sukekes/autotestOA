# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 16:15
# @Author  : suk
# @FileName: loginpage.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import os
from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self):
        self.data = dict()
        # 获取文件名，文件名要求与testdata中对应的子集名称保持一致
        self.page = os.path.basename(__file__)[:-3]

    def type_username(self, *username_loc, username):
        self.find_element(*username_loc).clear()
        self.find_element(*username_loc).send_keys(username)

    def type_password(self, *password_loc, password):
        self.find_element(*password_loc).clear()
        self.find_element(*password_loc).send_keys(password)

    def login(self, *btn_loc):
        self.find_element(*btn_loc).click()

