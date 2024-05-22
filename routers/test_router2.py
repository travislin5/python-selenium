from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/api2")


@router.get("/test")
async def livez():
    return JSONResponse(content={"message": "OKOK2"})
