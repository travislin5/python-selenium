from fastapi import FastAPI
from fastapi.responses import FileResponse
from routers.test_router import router as test_router
from routers.test_router2 import router as test_router2


app = FastAPI()

app.include_router(test_router)
app.include_router(test_router2)


# 首頁設定成某個html
@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse("./public/index.html")
