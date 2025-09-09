from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/casestudy/finance", response_class=HTMLResponse)
async def get_finance():
    return "<h1>Finance</h1>"