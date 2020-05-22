# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 15:12
# @Author  : suk
# @FileName: test.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import yaml
from log import logging


def yml_parse(page, name):
    try:
        # 取yml 文件内容
        file = open("../testdata/" + page + "/" + name + ".yml", 'r', encoding="utf-8")
        data = file.read()
        file.close()

        # 解析yml，转化成dict
        data = yaml.full_load(data)
        logging.info("parse case success" + data)
        return data
    except (FileNotFoundError, UnboundLocalError) as error:
        logging.error(error)


yml_parse("login", "12")
