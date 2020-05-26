# -*- coding: utf-8 -*-
# @Time    : 2020-5-26 15:35
# @Author  : suk
# @FileName: test_login_by_manager.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import pytest
from testcase.loginpage.login_by_manager import login_by_manager, RESULT


@pytest.mark.tasks
def test_login_by_manager():
    login_by_manager("loginpage", "login_by_manager")

    assert RESULT
