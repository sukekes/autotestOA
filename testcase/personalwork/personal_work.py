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
    menu_lock = "By." + parse.data['test_step'][0]["loc_type"]
    menu_attr_name = parse.data["test_step"][0]["name"]

    # 确认网上表单定位方式，属性值，输入参数
    webform_loc = "By." + parse.data["test_step"][1]["loc_type"]
    webform_attr_name = parse.data["test_step"][1]["name"]

    # 确认登录按钮定位方式，属性值
    webform_manager_loc= "By." + parse.data['test_step'][2]["loc_type"]
    webform_manager_attr_name = parse.data["test_step"][1]["name"]

    # 确认预期结果定位方式、属性值
    expect_loc = "By." + str.upper(parse.data["expect_output"]["loc_type"])
    expect_name = parse.data["expect_output"]["name"]

    # 输入用户名、密码
    person = PersonalWork()
    person.click_menu(menu_lock, menu_attr_name)
    person.click_web_form(webform_loc, webform_attr_name)
    person.click_form_manager(webform_manager_loc, webform_manager_attr_name)

    # 验证能否定位到首页form_type，定位到返回True，反之False
    form_type = person.find_element(eval(expect_loc), expect_name)
    if form_type is not None:
        return True
    else:
        return False

    person.driver_quit()
