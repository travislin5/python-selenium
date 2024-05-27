from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from routers.test_router import router as test_router
from routers.test_router2 import router as test_router2
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time
import os


app = FastAPI()

app.include_router(test_router)
app.include_router(test_router2)


class CompanyRequest(BaseModel):
    company_name: str


# 將 /image 資料夾掛載到 /static 路徑
app.mount("/static", StaticFiles(directory="image"), name="static")


# 首頁設定成某個html
@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse("./public/index.html")


@app.post("/get_company_data")
def get_company_data(request: CompanyRequest):
    print("********")
    # linux上執行selenium用的配置
    ch_options = webdriver.ChromeOptions()

    ch_options.add_argument("--headless")
    ch_options.add_argument("--no-sandbox")
    ch_options.add_argument("--disble-gpu")
    ch_options.add_argument("--disble-dev-shm-usage")

    driver = webdriver.Chrome(ch_options)

    driver.maximize_window()
    try:
        # 開啟目標網頁
        driver.get("https://findbiz.nat.gov.tw/fts/query/QueryBar/queryInit.do")

        # 查找輸入框
        search_box = driver.find_element(By.ID, "qryCond")  # 假設輸入框的ID為 'qryCond'

        # 輸入公司名稱
        search_box.send_keys(request.company_name)

        # 提交查詢表單
        search_box.send_keys(Keys.RETURN)

        # 等待結果加載（根據實際情況調整）
        time.sleep(3)

        # 找到指定的連結並點擊
        link = driver.find_element(By.LINK_TEXT, request.company_name)
        link.click()

        time.sleep(3)

        # 找到指定的連結並點擊
        dataLink = driver.find_element(By.LINK_TEXT, "董監事資料")
        dataLink.click()

        time.sleep(3)

        # 截取整個頁面的截圖
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_filename = f"screenshot_{current_time}.png"
        screenshot_path = os.path.join("image", screenshot_filename)
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
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            row_data = []
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                row_data.append(col.text.strip())
            data.append(row_data)

        return {"data": data, "screenshot_path": f"/static/{screenshot_filename}"}

    except Exception as e:
        return {"data": "error", "e": e}

    finally:
        driver.quit()
