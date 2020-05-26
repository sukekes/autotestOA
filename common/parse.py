# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 14:57
# @Author  : suk
# @FileName: parse.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import os
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


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


if __name__ == "__main__":
    parse = Parse()

    parse.yml_parse("personalwork", "personal_work")
    driver = webdriver.Chrome()
    driver.get("http://oa.simulate.com:8080/systemcenter/theme/newecidi/index.jsp#")
    driver.maximize_window()
    driver.find_element_by_id("password").send_keys("chenm2test")
    sleep(3)
    driver.find_element_by_id("username").send_keys("chen_m2")
    sleep(3)
    driver.find_element_by_id("loginbtn").click()
    sleep(3)
    print(parse.data['test_step'][0]["loc_type"])
    driver.find_element(eval("By." + parse.data['test_step'][0]["loc_type"]), parse.data['test_step'][0]["name"]).click()
    sleep(3)



    # if parse.data['pre_case'] is None:
    #     print(" is None: " + str(parse.data['pre_case']))
    # else:
    #     print("is not None" + str(parse.data['pre_case']))

