# -*- coding: utf-8 -*-
# @Time    : 2020-5-26 18:39
# @Author  : suk
# @FileName: personal_work.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
from common.parse import Parse
from pages.personal_work import PersonalWork
from selenium import webdriver
from selenium.webdriver.common.by import By


def personal_work(page, yml):

    # 解析测试数据，返回dict
    parse = Parse()
    parse.call_pre_case(page, yml)

    # 确认个人办公菜单定位方式，属性名称
    menu_loc = ("By." + str.upper(parse.data['test_step'][0]["loc_type"]), parse.data["test_step"][0]["name"])

    # 确认网上表单定位方式，属性值，输入参数
    webform_loc = ("By." + str.upper(parse.data["test_step"][1]["loc_type"]), parse.data["test_step"][1]["name"])

    # 确认登录按钮定位方式，属性值
    webform_manager_loc = ("By." + str.upper(parse.data['test_step'][2]["loc_type"]), parse.data["test_step"][2]["name"])

    # 确认预期结果定位方式、属性值
    expect_loc = "By." + str.upper(parse.data["expect_output"]["loc_type"])
    expect_name = parse.data["expect_output"]["name"]

    # 输入用户名、密码
    person = PersonalWork(parse.data["base_url"])
    person.click_menu(menu_loc[0], menu_loc[1])
    person.click_web_form(webform_loc[0], webform_loc[1])
    person.click_form_manager(webform_manager_loc[0], webform_manager_loc[1])

    # 验证能否定位到首页form_type，定位到返回True，反之False
    form_type = person.find_element(eval(expect_loc), expect_name)
    if form_type is not None:
        return True
    else:
        return False

    person.driver_quit()
