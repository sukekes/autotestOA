# -*- coding: utf-8 -*-
# @Time    : 2020-5-26 18:50
# @Author  : suk
# @FileName: test_personal_work.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import pytest
from selenium import webdriver
from testcase.personalwork.personal_work import personal_work


@pytest.mark.tasks
def test_personal_work():
    driver = webdriver.Chrome()
    expect = personal_work(driver, "personalwork", "personal_work")
    assert expect
    driver.quit()