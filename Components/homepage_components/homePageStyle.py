from fastapi import APIRouter
from fastapi.responses import HTMLResponse


async def homepageStyle():
    return """
    <style>
        :root {
            --bg: #111;
        }
        body {
            background: var(--bg);
        }
    </style>
    """
