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

    # 找到表格元素
    # table = driver.find_element(By.CLASS_NAME, 'table-striped')

    # # 提取表格数据
    # rows = table.find_elements(By.TAG_NAME, 'tr')
    # for row in rows:
    #     cols = row.find_elements(By.TAG_NAME, 'td')
    #     for col in cols:
    #         print(col.text.strip())

    lst = []  # 将表格的内容存储为list

    element = driver.find_element(By.XPATH, '//*[@id="tabShareHolderContent"]/div[3]/table')  # 定位表格
    table = element.find_element(By.XPATH, '//*[@id="tabShareHolderContent"]/div[3]/table/tbody')
    # 提取表格内容td
    tr_tags = table.find_elements(By.TAG_NAME, 'tr')  # 进一步定位到表格内容所在的tr节点
    for tr in tr_tags:
        td_tags = tr.find_elements(By.TAG_NAME, 'td')
        for td in td_tags[:4]: #只提取前4列
            lst.append(td.text) #不断抓取的内容新增到list当中

    print(table)
    print("********")
    print(lst)

finally:
    # 關閉瀏覽器
    driver.quit()