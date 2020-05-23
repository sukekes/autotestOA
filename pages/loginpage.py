# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 16:15
# @Author  : suk
# @FileName: loginpage.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.basepage import BasePage
from common.parse import Parse


class LoginPage(BasePage):
    # 获取文件名，文件名要求与testdata中对应的子集名称保持一致
    page = os.path.basename(__file__)[:-3]
    data = None
    # 解析测试数据
    def get_data(self, yml):
        parse = Parse()
        self.data = parse.yml_parse(self.page, yml)
        return self.data

    # 判断是否有前置用例，如果有前置用例，则需要调用前置用例
    def is_pre(self, yml):
        self.get_data(self, yml)
        if self.data['pre_case'] is not None:
            for pre_case in self.data['pre_case']:

                




