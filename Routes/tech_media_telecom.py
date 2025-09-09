from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/casestudy/tech_media_telecom", response_class=HTMLResponse)
async def get_tech_media_telecom():
    return "<h1>Tech, Media & Telecom</h1>"