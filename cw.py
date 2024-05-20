# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# from screen import fullsreen

# 開啟瀏覽器視窗(Chrome)
driver = webdriver.Chrome()

# 將瀏覽器視窗調整到最大化
driver.maximize_window()

try:
    # 開啟目標網頁
    driver.get("https://www.cw.com.tw/")

    # 等待結果加載（根據實際情況調整）
    time.sleep(3)

    # 找到指定的連結並點擊
    link = driver.find_element(
        By.XPATH, "/html/body/header/div[1]/div[2]/div[1]/span[1]"
    )
    link.click()

    # 等待結果加載（根據實際情況調整）
    time.sleep(3)

    # 查找輸入框
    search_box = driver.find_element(
        By.XPATH, "/html/body/header/div[2]/div/div[1]/form/div/input"
    )  # 假設輸入框的ID為 'qryCond'

    # 輸入公司名稱
    company_name = "富邦人壽"
    search_box.send_keys(company_name)

    # 提交查詢表單
    search_box.send_keys(Keys.RETURN)

    # 等待結果加載（根據實際情況調整）
    time.sleep(15)


finally:
    # 關閉瀏覽器
    driver.quit()
