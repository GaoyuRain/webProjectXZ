"""
author :Rain
Date : 2019/08/02
Description : 获取各个页面对象
"""
from page.application_list_page import ApplicationListPage
from page.login_page import LoginPage


class PageUtils:
    def __init__(self, driver):
        self.driver = driver

    def get_login_page(self) -> LoginPage:
        return LoginPage(self.driver)

    def get_application_list_page(self) -> ApplicationListPage:
        return ApplicationListPage(self.driver)


if __name__ == '__main__':
    pass
