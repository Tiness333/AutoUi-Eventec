import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utils.base_def import BaseDef
from BasePages.LoginPage import LoginPage
from BasePages.SpuManage import Spu_manage

driver = webdriver.Chrome()

class Auto_Test(unittest.TestCase):
    #实例化对象
    def setUp(self) -> None:
        self.driver = Spu_manage(driver)
    #关闭网页
    def tearDown_class(self) -> None:
        self.driver.quit()

    #登录测试
    def test_case001(self):
        self.driver.login(username='XDSC',password='cs123456')

    #新增SPU
    def test_case002(self):
        self.driver.spu_add()