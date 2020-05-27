# -*- coding: utf-8 -*-
# @Time    : 2020-5-26 16:09
# @Author  : suk
# @FileName: run.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/

import pytest

if __name__ == "__main__":
    pytest.main(["-m", "tasks", "--pytest_report", "../testreport/report.html"])
