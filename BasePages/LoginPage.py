# -*- coding: utf-8 -*-
# @Time    : 2023/12/06 14:18
# @Author  : Tiness
# @Email   : wangruiwlj@163.com
# @File    : data_format
# @Software: PyCharm


from selenium import webdriver
from Utils.base_def import BaseDef
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BaseDef):
    #页面地址
    url = 'https://pre-store.eventec.cn/#/'
    #用户名输入框元素
    username_ele = (By.CSS_SELECTOR,'input[type="text"]')
    #密码输入框元素
    password_ele = (By.CSS_SELECTOR,'input[type="password"]')
    #记住用户名密码元素
    remember_ele = (By.CSS_SELECTOR,'.el-checkbox__inner')
    #登录按钮元素
    login_ele = (By.CSS_SELECTOR,'.el-button')
    filename1 = '登录成功.png'
    filename2 = '登录失败.png'

    def login(self,username,password):
        try:
            self.get_url(self.url)
            self.sendkeys(self.username_ele,value=username)
            self.sendkeys(self.password_ele,value=password)
            self.click(self.remember_ele)
            self.click(self.login_ele)



            #断言
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, ".menuTitle")))
            self.save_screenshot(filename=self.filename1)


        except Exception:
            self.save_screenshot(filename=self.filename2)






if __name__ == '__main__':

    LoginPage(driver = webdriver.Chrome()).login(username='XDSC',password='cs123456')







