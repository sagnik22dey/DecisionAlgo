from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/casestudy/insurance", response_class=HTMLResponse)
async def get_insurance():
    return "<h1>Insurance</h1>"