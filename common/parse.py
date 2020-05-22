# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 14:57
# @Author  : suk
# @FileName: parse.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/

import yaml


class Parse(object):
    @staticmethod
    def yml_parse(self, page, name):
        file = open(
            "../testdata/" +
            page +
            "/" +
            name +
            ".yml",
            'r',
            encoding="utf-8")
        yml_data = file.read()
        file.close()
        # 解析yml，转化成dict
        data = yaml.full_load(yml_data)
        return data

    # 待实现
    def excel_parse(self):
        pass
