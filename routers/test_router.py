from fastapi import APIRouter, Path, Response
from fastapi.responses import FileResponse, JSONResponse

router = APIRouter(prefix="/api")


@router.get("/test")
async def livez():
    return JSONResponse(content={"message": "OK"})


@router.post("/pic")
def download_image():
    image_path = Path("/img/aa.png")
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)
