"""
author :admin
Date : 2021/07/08
Description : 登录模块测试
"""
import allure
import pytest

from utils.data_utils import DataUtils
from utils.driver_utils import DriverUtils
from utils.page_utils import PageUtils


@allure.feature("登录需求")
class TestLogin:

    def setup_class(self) -> None:
        self.driver = DriverUtils.get_driver()
        self.page_utils = PageUtils(self.driver)
        self.login_page = self.page_utils.get_login_page()
        self.application_list_page = self.page_utils.get_application_list_page()

    def teardown_class(self) -> None:
        DriverUtils.quit_driver()

    @pytest.mark.parametrize('account, pwd, expect_data,user_name', DataUtils.get_login_data('account'))
    @allure.story('登录功能测试')
    def test_01_account_login(self, account, pwd, expect_data, user_name):
        allure.description('账户登录')
        self.login_page.login(account, pwd)
        self.login_page.attach_pic('登录结果_%s' % expect_data)
        toast_text = self.login_page.get_toast_text(expect_data)
        assert expect_data in toast_text

    @allure.story("用户名称校验")
    def test_02_account_name(self):
        allure.description('登录成功，用户名称显示')
        self.login_page.to_home()
        user_name = DataUtils.get_login_data('account')[1][3]
        self.login_page.attach_pic('应用列表页面')
        assert user_name == self.application_list_page.get_user_name()


if __name__ == '__main__':
    pytest.main()
