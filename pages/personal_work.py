# -*- coding: utf-8 -*-
# @Time    : 2020-5-26 18:24
# @Author  : suk
# @FileName: personal_work.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from pages.basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class PersonalWork(BasePage):
    def __init__(self):
        super().__init__()

    def click_menu(self, loc_type, attr_name):
        self.find_element(eval(loc_type), attr_name).click()

    def click_web_form(self, loc_type, attr_name):
        self.find_element(eval(loc_type), attr_name).click()

    def click_form_manager(self, loc_type, attr_name):
        self.find_element(eval(loc_type), attr_name).click()
