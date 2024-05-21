# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from seleniumbase import SB

def verify_success(sb):
    sb.assert_element('img[alt="天下雜誌"]', timeout=8)
    sb.sleep(4)

with SB(uc_cdp=True, guest_mode=True) as sb:
    sb.open("https://www.cw.com.tw/")
    time.sleep(3)

    # 找到指定的連結並點擊
    link = sb.driver.find_element(
        By.XPATH, "/html/body/header/div[1]/div[2]/div[1]/span[1]"
    )
    link.click()

    # 等待結果加載（根據實際情況調整）
    time.sleep(3)

    # 查找輸入框
    search_box = sb.driver.find_element(
        By.XPATH, "/html/body/header/div[2]/div/div[1]/form/div/input"
    )  # 假設輸入框的ID為 'qryCond'

    # 輸入公司名稱
    company_name = "富邦人壽"
    search_box.send_keys(company_name)

    # 提交查詢表單
    search_box.send_keys(Keys.RETURN)
    try:
        verify_success(sb)
        print("---success---")
        time.sleep(5)

    except Exception:
        if sb.is_element_visible('input[value*="Verify"]'):
            sb.click('input[value*="Verify"]')
        elif sb.is_element_visible('iframe[title*="challenge"]'):
            sb.switch_to_frame('iframe[title*="challenge"]')
            sb.click("span.mark")
        else:
            raise Exception("Detected!")
        try:
            verify_success(sb)
        except Exception:
            raise Exception("Detected!")
