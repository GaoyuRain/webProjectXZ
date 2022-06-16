"""
author :admin
Date : 2021/07/07
Description : 登录页面元素
"""
from selenium.webdriver.common.by import By

# '域账号登录按钮'
domain_login_btn = (By.XPATH, "//li[contains(text(),'域账号登录')]")
# '账号输入框'
login_input_account = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/ul[2]/li[1]/div[1]/input[1]")
# '密码输入框'
login_input_pwd = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/ul[2]/li[2]/div[1]/input[1]")
# '登录按钮'
login_btn = (By.XPATH, "//span[contains(text(),'登录')]")
# 租户选择按钮
choice_tenement_btn = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/input[1]")
# 新奥新智按钮
xinzhi_btn = (By.XPATH, "//span[contains(text(),'新奥新智')]")
# 确定按钮
sure_btn = (By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/button[1]")


