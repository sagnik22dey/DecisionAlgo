from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/casestudy/healthcare", response_class=HTMLResponse)
async def get_healthcare():
    return "<h1>Healthcare</h1>"