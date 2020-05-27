# UI 自动化测试PageObject 实例
##内网OA模拟环境

## requirement
### UI自动化测试框架：[Selenium v3.141.0](https://selenium-python.readthedocs.io/)
### 单元测试框架： [pytest v5.4.2](https://learning-pytest.readthedocs.io/zh/latest/index.html)
### 报告模板 ：[PyTestReport v0.2.1](https://github.com/five3/PyTestReport)
### 用例解析 ：[PyYaml v5.3.1](https://pyyaml.org/wiki/PyYAMLDocumentation)
### 浏览器驱动： [ChromeDriver](https://chromedriver.chromium.org/downloads)


## 代码结构
-   common
    -   log.py #日志输出
    -   parse.py # 解析测试数据
-   logs
    -   log.log # 日志
-   pages
    -   basepage.py     # 所有页面的父类，主要定义元素定位方法
    -   ***.py          # 子类页面，主要定义测试方法，如登录页面输入用户名、输入密码，点击登录按钮
-   run_test
    -   run.py          # 执行测试方法
    -   test_xxx.py     # 测试方法
-   testcase
    -   dirname/xxx.py  # 描述测试业务逻辑，如调用前置用例，调动方法前后顺序
    
-   testdata
    -   dirname/xxx.yml # 测试用例，主要内容为前置用例、测试步骤、预期结果
-   testdata_excel
    -   xxx.xlsx        # Excel维护的测试用例，预留内容，尚未实现
-   testreport
    -   report.html     # 测试报告

## 测试用例编写模板
### [Yaml语法](https://www.runoob.com/w3cnote/yaml-intro.html)
### [login_by_manager](https://github.com/sukekes/autotestOA/blob/master/testdata/loginpage/login_by_manager.yml)
### [personal_work](https://github.com/sukekes/autotestOA/blob/master/testdata/personalwork/personal_work.yml)


## 执行测试脚本
```python
import pytest


if __name__ == "__main__":
    pytest.main(["-m", "tasks", "--pytest_report", "../testreport/report.html"])
```
