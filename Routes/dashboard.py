from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import *
from Components.general_components.footer import *

router = APIRouter()


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard():

    navabar_html = await navbar_body()
    footer_html = await footer_body()
    navabar_css = await navbar_style()
    footer_css = await footer_style()

    return f""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard</title>  
        {navabar_css}
        {footer_css}
        
        
          
    </head>
    <body>
        {navabar_html}
        {footer_html}
    
    
    </body>
    </html>
    """
