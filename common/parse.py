# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 14:57
# @Author  : suk
# @FileName: parse.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import os
import yaml


class Parse(object):
    def __init__(self):
        self.data = dict()
        self.base_path = os.getcwd()[:os.getcwd().find("autotestOA") + 10]
    # data = dict()

    def yml_parse(self, page, name):
        file = open(self.base_path +
            "/testdata/" + page + "/" + name + ".yml", 'r', encoding="utf-8")
        yml_data = file.read()
        file.close()
        # 解析yml，转化成dict
        self.data = yaml.full_load(yml_data)
        return self.data

    def is_pre(self, page, yml):
        self.yml_parse(page, yml)
        if self.data['pre_case'] is not None:
            return True
        else:
            return False

    def call_pre_case(self, page, yml):
        has_pre_case = self.is_pre(page, yml)

        if has_pre_case:
            for pre_case in self.data['pre_case']:
                exec("from testcase.%s.%s import %s" % (pre_case["suite"], pre_case["name"], pre_case["name"]))
                eval(pre_case["name"])(pre_case["suite"], pre_case["name"])


# if __name__ == "__main__":
#     parse = Parse()
#
#     parse.call_pre_case("loginpage", "login_by_manager")
#
#     if parse.data['pre_case'] is None:
#         print(" is None: " + str(parse.data['pre_case']))
#     else:
#         print("is not None" + str(parse.data['pre_case']))

