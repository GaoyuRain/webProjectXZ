from selenium import webdriver


class DriverUtils:
    '''
    获取浏览器对象
    '''
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    url = 'http://authentication-center-new.ennewi.cn/login?appid=tenant-management-service&redirect=http%3A%2F%2Fdevops.' \
          'ennewi.cn%2Fcicd%2Fapp%3FauthCode%3DMTQwMTc1MDc2OTYwMDIwNDgwMSM3M2M4M2M5YWY3Y2NkMDg4MGQzMDA0MWZmOTFhOGIxNw%26r' \
          'ememberMe%3D0%26loginCode%3DMTQwMTc1MDc2OTYwMDIwNDgwMSM4NUIwRDZDMy0zMkJBLTRBM0EtOTI2Ni04MzRCMUNBRkQ2RTg&tena' \
          'ntPageName=Default'

    __driver = None

    @classmethod
    def get_driver(cls, type=CHROME, url=url):
        '''
        :param type:
        :param url:
        :return:
        '''
        if cls.__driver is None:
            if cls.FIREFOX == type:
                cls.__driver = webdriver.Firefox()
            else:
                cls.__driver = webdriver.Chrome()
            cls.__driver.get(url)
            cls.__driver.maximize_window()
            cls.__driver.implicitly_wait(10)
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver = None


def get_tips_msg(type=DriverUtils.CHROME):
    return DriverUtils.get_driver(type).find_element_by_class_name('layui-layer-content').text

if __name__ == '__main__':
    DriverUtils.get_driver()