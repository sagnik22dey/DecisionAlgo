from fastapi import APIRouter
from fastapi.responses import HTMLResponse


async def homepageStyle():
    return """
    <style>
        body {
            background: #111111;
            margin: 0;
            padding: 0;
        }
    </style>    
    """
