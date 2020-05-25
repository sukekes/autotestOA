# -*- coding: utf-8 -*-
# @Time    : 2020-5-25 12:58
# @Author  : suk
# @FileName: login_by_manager.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from common.parse import Parse
from pages.loginpage import LoginPage
from selenium.webdriver.common.by import By


def login_by_manager(page, yml):
    parse = Parse()

    parse.call_pre_case(page, yml)

    # 用户名定位方式，name,要输入的数据
    username_loc = (eval("By." + str.upper(parse.data['test_step'][0]["loc_type"])), parse.data["test_step"][0]["name"])
    username = parse.data["input_params"]["username"]

    # 密码定位方式，name,要输入的数据
    password_loc = (eval("By." + str.upper(parse.data["test_step"][1]["loc_type"])), parse.data["test_step"][1]["name"])
    password = parse.data["input_params"]["username"]

    # 登录按钮的定位方式，name
    btn_loc = ("By." + str.upper(parse.data['test_step'][2]["loc_type"]), parse.data["test_step"][2]["name"])

    # 预期结果的定位方式、name
    expect_loc = str.upper(parse.data["expect_output"]["loc_type"])
    expect_name = parse.data["expect_output"]["name"]

    login = LoginPage()

    login.type_username(*username_loc, username)

    # login.type_password(*((eval("By." + password_loc)), password), type_password)
    #
    # login.login((eval("By." + btn_loc), btn))
    #
    # login.find_element((eval("By." + expect_loc), expect_name))


if __name__ == "__main__":
    login_by_manager("loginpage", "login_by_manager")
