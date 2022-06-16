"""
author :admin
Date : 2021/07/07
Description : 登录页面
"""
from time import sleep

from page.base_page import BasePage
from page_elements import login_page_elements
from utils.driver_utils import DriverUtils
from utils.instance_utils import singleton


@singleton
class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, pwd):
        self.click_element(login_page_elements.domain_login_btn)
        self.send_element(login_page_elements.login_input_account, username)
        self.send_element(login_page_elements.login_input_pwd, pwd)
        self.click_element(login_page_elements.login_btn)

    def to_home(self):
        # 前往首页
        self.click_element(login_page_elements.choice_tenement_btn)
        self.click_element(login_page_elements.xinzhi_btn)
        self.click_element(login_page_elements.sure_btn)


if __name__ == '__main__':
    LoginPage(DriverUtils.get_driver()).login('gaoyui', 'GAOYU0829')
