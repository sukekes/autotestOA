# -*- coding: utf-8 -*-
# @Time    : 2020-5-26 18:50
# @Author  : suk
# @FileName: test_personal_work.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import pytest
from testcase.personalwork.personal_work import personal_work


@pytest.mark.tasks
def test_personal_work():
    expect = personal_work("personalwork", "personal_work")
    assert expect
