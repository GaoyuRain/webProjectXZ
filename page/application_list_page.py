"""
author :admin
Date : 2021/07/08
Description : 应用列表页面
"""
from page.base_page import BasePage
from page_elements import application_list_elements

from utils.instance_utils import singleton


@singleton
class ApplicationListPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_user_name(self):
        return self.get_element(application_list_elements.name_text_input).text
