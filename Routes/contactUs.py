from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import *
from Components.general_components.footer import *
from Components.contactUs_components.heroSection import *




router = APIRouter()


@router.get("/contactus", response_class=HTMLResponse)
async def contactUs():
    navbar_html = await navbar_body()
    footer_html = await footer_body()
    navbar_css = await navbar_style()
    footer_css = await footer_style()
    heroSection_html = await heroSection_body()
    heroSection_css = await heroSection_style()
    
    
    return f"""
    <html>
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Import Fonts from Google Fonts -->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@700&family=Jost:wght@400&family=Poppins:wght@400&display=swap" rel="stylesheet">
        <title>About Us</title>
        <style>
        body {{
            overflow-x: hidden;
        }}
        {navbar_css}
        {footer_css}
        {heroSection_css}
        
        
        </style>
        </head>
        <body>
        {navbar_html}
        {heroSection_html}
        {footer_html}
            
            
            
        </body>
    </html>
"""