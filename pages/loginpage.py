# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 16:15
# @Author  : suk
# @FileName: loginpage.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import os
from pages.basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, base_url):
        self.driver = webdriver.Chrome()
        self.open(base_url)

    def type_username(self, *username_loc, username):
        self.driver.find_element(*username_loc).clear()
        self.driver.find_element(*username_loc).send_keys(username)

    def type_password(self, *password_loc, password):
        self.find_element(*password_loc).clear()
        self.find_element(*password_loc).send_keys(password)

    def login(self, *btn_loc):
        self.find_element(*btn_loc).click()

