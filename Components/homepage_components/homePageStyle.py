from fastapi import APIRouter
from fastapi.responses import HTMLResponse


async def homepageStyle():
    return """
    <style>
        body {
            background: #111111;
        }
    </style>    
    """
