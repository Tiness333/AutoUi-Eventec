from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://pre-store.eventec.cn/#/')

driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入用户名']").send_keys("ccwdz")

driver.find_element(By.CSS_SELECTOR, "input[placeholder='请输入密码']").send_keys("ccwdz11")
driver.find_element(By.CSS_SELECTOR, ".el-checkbox__inner").click()
driver.find_element(By.CSS_SELECTOR, ".el-button--large").click()

driver.find_element(By.CSS_SELECTOR, ".i-icon i-icon-shop rowCenter mr-20").click()
driver.find_element(By.CSS_SELECTOR, ".el-menu-item is-active").click()
driver.find_element(By.CSS_SELECTOR, 'button[placeholder="商品名称/商品ID"]').send_keys("测试新创建的状态")
driver.find_element(By.CSS_SELECTOR,'.mb-20 > .el-button--primary').click()