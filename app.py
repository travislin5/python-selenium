# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#開啟瀏覽器視窗(Chrome)
driver = webdriver.Chrome()

try:
    # 開啟目標網頁
    driver.get("https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do")

    # 查找輸入框
    search_box = driver.find_element(By.ID, 'qryCond')  # 假設輸入框的ID為 'qryCond'
    
    # 輸入公司名稱
    company_name = "保誠人壽保險股份有限公司"
    search_box.send_keys(company_name)

    # 提交查詢表單
    search_box.send_keys(Keys.RETURN)
    
    # 等待結果加載（根據實際情況調整）
    time.sleep(3)

    # 找到指定的連結並點擊
    link = driver.find_element(By.LINK_TEXT, "保誠人壽保險股份有限公司")
    link.click()

    time.sleep(3)

    # 找到指定的連結並點擊
    dataLink = driver.find_element(By.LINK_TEXT, "董監事資料")
    dataLink.click()

    time.sleep(3)

    # 截取整個頁面的截圖
    screenshot_path = 'image/screenshot.png'
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")


finally:
    # 關閉瀏覽器
    driver.quit()