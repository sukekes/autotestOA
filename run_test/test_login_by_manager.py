# -*- coding: utf-8 -*-
# @Time    : 2020-5-26 15:35
# @Author  : suk
# @FileName: test_login_by_manager.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import pytest
from selenium import webdriver
from testcase.loginpage.login_by_manager import login_by_manager


@pytest.mark.tasks
def test_login_by_manager():
    driver = webdriver.Chrome()
    expect = login_by_manager(driver, "loginpage", "login_by_manager")

    assert expect
    driver.quit()
