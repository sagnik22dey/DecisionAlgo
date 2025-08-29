from fastapi import APIRouter
from fastapi.responses import HTMLResponse


async def homepageStyle():
    return """
    <style>
        body {
            background: black;
            margin: 0;
            padding: 0;
        }
    </style>    
    """
