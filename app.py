# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# linux上執行selenium用的配置
# ch_options = webdriver.ChromeOptions()

# ch_options.add_argument("--headless")
# ch_options.add_argument("--no-sandbox")
# ch_options.add_argument("--disble-gpu")
# ch_options.add_argument("--disble-dev-shm-usage")
# # 開啟瀏覽器視窗(Chrome)
# driver = webdriver.Chrome(ch_options)
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 開啟目標網頁
    driver.get("https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do")

    # 查找輸入框
    search_box = driver.find_element(By.ID, "qryCond")  # 假設輸入框的ID為 'qryCond'

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
    screenshot_path = "image/screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")

    data = []

    # 定位表格
    element = driver.find_element(
        By.XPATH, '//*[@id="tabShareHolderContent"]/div[3]/table'
    )  
    table = element.find_element(
        By.XPATH, '//*[@id="tabShareHolderContent"]/div[3]/table/tbody'
    )
    rows = table.find_elements(By.TAG_NAME, 'tr')
    for row in rows:
        row_data = []
        cols = row.find_elements(By.TAG_NAME, 'td')
        for col in cols:
            row_data.append(col.text.strip())
        data.append(row_data)

    print("********")
    print(data)

finally:
    # 關閉瀏覽器
    driver.quit()
