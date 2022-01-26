from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/welcome")
def greeting():
    return JSONResponse({"message": "hello"})
