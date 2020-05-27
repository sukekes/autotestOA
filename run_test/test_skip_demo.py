# -*- coding: utf-8 -*-
# @Time    : 2020-5-27 10:30
# @Author  : suk
# @FileName: test_skip_demo.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/
import pytest


@pytest.mark.skip
def test_skip_demo():
    assert False
