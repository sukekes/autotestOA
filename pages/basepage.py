# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 17:35
# @Author  : suk
# @FileName: basepage.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/

from common.log import logging
from selenium import webdriver
from  time import sleep
from selenium.common.exceptions import WebDriverException, NoSuchWindowException, NoSuchElementException


class BasePage(object):
    def __init__(self):
        self.element = None
        self.elements = None
        self.pre_case = False
        self.base_url = None
        self.driver = None
        self.timeout = 30

    # protected mthod
    def _open(self, base_url):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(base_url)
            self.driver.implicitly_wait(self.timeout)
            self.driver.current_window_handle
            self.driver.maximize_window()
        except (WebDriverException, NoSuchWindowException, NoSuchElementException) as error:
            logging.error(error)

    def open(self, base_url):
        self._open(base_url)

    def find_element(self, *loc):
        try:
            self.element = self.driver.find_element(*loc)
            sleep(3)
            logging.info("find the element %s success." % str(loc))
            return self.element
        except NoSuchElementException as error:
            logging.erro(error)

    def find_elements(self, *loc):
        try:
            self.elements = self.driver.find_elements(*loc)
            sleep(3)
            self.driver.implicitly_wait(self.timeout)
            logging.info("find the element %s succeed." % loc)
            return self.elements
        except NoSuchElementException as error:
            logging.erro(error)

    def driver_quit(self):
        self.driver.quit()


# if __name__ == "__main__":
#     basepage = BasePage()
#     basepage.open("http://oa.simulate.com:8080/systemcenter/theme/newecidi/loginform.html")


