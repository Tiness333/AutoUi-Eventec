# -*- coding: utf-8 -*-
# @Time    : 2023/12/06 14:18
# @Author  : Tiness
# @Email   : wangruiwlj@163.com
# @File    : data_format
# @Software: PyCharm


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from BasePages.LoginPage import LoginPage
import os
import pyautogui
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
ParentDirPath = os.path.dirname(os.path.dirname(__file__))
class Spu_manage(LoginPage):
    # 页面地址
    # url2 = 'https://test.eventec.shop/page/sendmall/#/store/ProductCenter/StoreGoodsList'
    #商品中心元素
    spu_ele = (By.XPATH,'//span[text()="商品中心"]')
    #商品管理元素
    spu_manage_sel = (By.XPATH,'//span[text()="商品管理"]')
    #新增商品按钮
    add_spu_ele = (By.XPATH,'//span[text()=" 新增商品 "]')
    #搜索按钮元素
    search_ele = (By.CSS_SELECTOR,'.mb-20 > .el-button--primary')
    #商品名称输入框元素
    spu_name_ele = (By.CSS_SELECTOR,'input[placeholder="请输入商品名称"]')
    #商品货仓选择下拉框元素
    spu_are_dropdownlist_ele = (By.CSS_SELECTOR,'input[placeholder="请选择商铺货仓"]')
    #货仓属性元素
    spu_are_ele = (By.XPATH,'//span[text()="自动化测试货仓"]')
    #商品后台分类下拉框元素
    spu_bec_dropdownlist_ele = (By.CSS_SELECTOR,'input[placeholder="请选择"]')
    #商品后台一级分类属性元素
    spu_classify1_ele = (By.XPATH,'//span[text()="测试专用"]')
    spu_classify2_ele = (By.XPATH,'//span[text()="其他商品"]')
    spu_classify3_ele = (By.XPATH,'//span[text()="测试类商品"]')
    #上传商品图片
    spu_pictureinput_ele = (By.NAME,'file')
    #spu基本信息下一步
    spu_nextstep_ele = (By.XPATH,'//span[text()=" 下一步 "]')
    #销售价输入框
    spu_SalesPrice_ele = (By.CSS_SELECTOR,'input[placeholder="￥输入销售价格"]')
    #市场价输入框
    spu_Price_ele = (By.CSS_SELECTOR,'input[placeholder="￥输入市场价格"]')
    #成本价输入框
    spu_CostPrice_ele = (By.CSS_SELECTOR,'input[placeholder="￥输入成本价格"]')
    #库存输入框
    spu_stock_ele = (By.CSS_SELECTOR,'input[placeholder="输入库存数量"]')
    #保存创建商品
    spu_create_ele = (By.XPATH,'//span[text()=" 保存 "]')


    def spu_add(self):
        # self.get_url(self.url2)
        #点击商品中心
        self.click(self.spu_ele)
        #点击商品管理
        self.click(self.spu_manage_sel)
        time.sleep(1)
        #点击新增商品
        self.click(self.add_spu_ele)
        time.sleep(2)
        #点击商品名称输入框并输入内容
        self.sendkeys(loc=self.spu_name_ele,value="自动化测试商品")
        #点击商品货仓下拉选择框
        self.click(self.spu_are_dropdownlist_ele)
        #点击选择自动化测试货仓
        self.click(self.spu_are_ele)
        #点击后台分类下拉选择框
        self.click(self.spu_bec_dropdownlist_ele)
        #选择一级二级三级分类
        self.click(self.spu_classify1_ele)
        time.sleep(1)
        self.click(self.spu_classify2_ele)
        time.sleep(1)
        self.click(self.spu_classify3_ele)
        time.sleep(3)

        #上传商品图片

        image_path = os.path.join(ParentDirPath,u'BasePages\spu.jpg')
        print(image_path)
        self.sendkeys(self.spu_pictureinput_ele, value=image_path)
        time.sleep(4)

        #点击下一步去创建sku规格及价格
        self.click(self.spu_nextstep_ele)
        time.sleep(1)
        #点击输入销售价
        self.sendkeys(self.spu_SalesPrice_ele,1)
        time.sleep(1)
        #点击输入输入市场价
        self.sendkeys(self.spu_Price_ele,10)
        time.sleep(1)
        #点击输入成本价
        self.sendkeys(self.spu_CostPrice_ele,15)
        time.sleep(1)
        #点击输入库存
        self.sendkeys(self.spu_stock_ele,999)
        time.sleep(1)
        #点击创建商品
        self.click(self.spu_create_ele)
        time.sleep(4)

    def spu_delete(self):
        pass





if __name__ == '__main__':
    Spu_manage(driver=webdriver.Chrome()).spu_add()





