import os
import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_DIR
from utils.driver_utils import DriverUtils


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_element(self, loc, timeout=15, poll_frequency=1.0) -> WebElement:
        """
        定位单个元素
        :param loc: (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隔时间
        :return:返回元素的定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def click_element(self, loc, timeout=15, poll_frequency=1.0):
        """
        点击元素
        :param loc: (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隔时间
        :return:
        """
        self.get_element(loc, timeout, poll_frequency).click()
        time.sleep(1)

    def click_text_element(self, loc, text):
        """
        点击根据text文本定位的元素
        """
        path = (loc[0], loc[1].format(text))
        print('path:', path)
        self.click_element(path)

    @allure.step(title='获取提示信息')
    def get_toast_text(self, keyword):
        # body:nth-child(2) div.el-message.el-message--error.is-closable:nth-child(10) > p.el-message__content
        # //p[contains(text(),'账户名或密码错误!')]
        # toast_xpath = (By.XPATH, '//*[contains(text(),"{}")]'.format(keyword))
        toast_xpath = (By.XPATH, '//*[contains(text(),"")]')
        return self.get_element(toast_xpath).text

    def send_element(self, loc, text, timeout=15, poll_frequency=1.0):
        """
        输入文本内容
        :param loc: (By.ID, 属性值) (By.CLASS_NAME, 属性值) (By.XPATH, 属性值)
        :param text: 输入文本内容
        :param timeout:搜索元素超时时间
        :param poll_frequency:搜索元素间隔时间
        :return:
        """
        # 定位
        input_text = self.get_element(loc, timeout, poll_frequency)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)
        time.sleep(1)

    def attach_pic(self, pic_name):
        '''截屏'''
        pic_path = BASE_DIR + os.sep + 'image' + os.sep + '{}_{}.png'.format(pic_name, time.strftime('%Y%m%d_%H%M%S'))
        self.driver.get_screenshot_as_file(pic_path)
        with open(pic_path, 'rb') as f:
            allure.attach(f.read(), name=pic_name, attachment_type=allure.attachment_type.PNG)


if __name__ == '__main__':
    print('cehisjieguo %s' % '112233')
