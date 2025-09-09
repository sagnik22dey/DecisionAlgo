from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/casestudy/retail_firm", response_class=HTMLResponse)
async def get_retail_firm():
    return "<h1>Retail Firm Adapting to AI Era</h1>"