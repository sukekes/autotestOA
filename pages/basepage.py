# -*- coding: utf-8 -*-
# @Time    : 2020-5-22 17:35
# @Author  : suk
# @FileName: basepage.py
# @Software: PyCharm
# @Blog    ：https://www.cnblogs.com/xjin/

from common.log import logging
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchWindowException,NoSuchElementException


class BasePage(object):

    element = None
    elements = None

    def __init__(self, driver):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    # protected mthod
    def _open(self):
        try:
            self.driver = webdriver.Edge()
            self.driver.get(self.base_url)
            self.driver.current_window_handle
        except (WebDriverException, NoSuchWindowException, NoSuchElementException) as error:
            logging.error(error)

    def open(self):
        self._open()

    def find_element(self, *loc):
        try:
            self.element = self.driver.find_element(*loc)
            logging.info("find the element %s success." % loc)
            return self.element
        except NoSuchElementException as error:
            logging.erro(error)

    def find_elements(self, *loc):
        try:
            self.elements = self.driver.find_elements(*loc)
            logging.info("find the element %s succeed." % loc)
            return self.elements
        except NoSuchElementException as error:
            logging.erro(error)

    def send_keys(self, param):
        try:
            self.location.send_keys(param)
        except NoSuchElementException as error:
            logging.error(error)



