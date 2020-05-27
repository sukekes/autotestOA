# -*- coding: utf-8 -*-
# @Time    : 2020-5-25 12:58
# @Author  : suk
# @FileName: login_by_manager.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from common.parse import Parse
from pages.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By


def login_by_manager(driver, page, yml):
    # 解析测试数据，返回dict
    parse = Parse()
    login = LoginPage(driver)
    parse.call_pre_case(driver, page, yml)


    # 确认用户名输入框定位方式，属性值，输入参数
    username_loc = (
        "By." +
        str.upper(
            parse.data['test_step'][0]["loc_type"]),
        parse.data["test_step"][0]["name"])
    username = parse.data["input_params"]["username"]

    # 确认密码输入框定位方式，属性值，输入参数
    password_loc = (
        "By." +
        str.upper(
            parse.data["test_step"][1]["loc_type"]),
        parse.data["test_step"][1]["name"])
    password = parse.data["input_params"]["password"]

    # 确认登录按钮定位方式，属性值
    btn_loc = (
        "By." +
        str.upper(
            parse.data['test_step'][2]["loc_type"]),
        parse.data["test_step"][2]["name"])

    # 确认预期结果定位方式、属性值
    expect_loc = "By." + str.upper(parse.data["expect_output"]["loc_type"])
    expect_name = parse.data["expect_output"]["name"]

    # 输入用户名、密码
    login.open()
    login.type_password(password_loc[0], password_loc[1], password)
    login.type_username(username_loc[0], username_loc[1], username)

    # 登录
    login.submit(btn_loc[0], btn_loc[1])

    # 验证能否定位到首页topmu，定位到返回True，反之False
    topmemu = login.find_element(eval(expect_loc), expect_name)

    return topmemu

# if __name__ == "__main__":
#     login_by_manager("loginpage", "login_by_manager")
