# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 15:12
# @Author  : suk
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import yaml
from common.log import logging
import importlib
# from testcase.loginpage.login_pwd_error import *


def yml_parse(page, name):
    try:
        # 取yml 文件内容
        file = open("../testdata/" + page + "/" + name + ".yml", 'r', encoding="utf-8")
        data = file.read()
        file.close()

        # 解析yml，转化成dict
        data = yaml.full_load(data)
        logging.info("parse case success: " + str(data))
        # print(data["pre_case"])
        return data
    except (FileNotFoundError, UnboundLocalError) as error:
        logging.error(error)


if __name__ == "__main__":
    data = yml_parse("loginpage", "login_by_manager")

    if data['pre_case'] is not None:
        methods = []
        for pre_case in data['pre_case']:

            __import__("testcase.loginpage.login_pwd_error")
            # print(help("testcase.loginpage.login_pwd_error"))

    eval("login_pwd_errot")()


# 获取当前文件名
# print(os.path.basename(__file__)[:-3])

