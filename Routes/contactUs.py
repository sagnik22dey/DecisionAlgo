from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import *
from Components.general_components.footer import *
from Components.contactUs_components.heroSection import *
from Components.contactUs_components.flags import *
from Components.contactUs_components.get_in_touch import *





router = APIRouter()


@router.get("/contactus", response_class=HTMLResponse)
async def contactUs():
    navbar_html = await navbar_body()
    footer_html = await footer_body()
    navbar_css = await navbar_style()
    footer_css = await footer_style()
    heroSection_html = await contact_banner_body()
    heroSection_css = await contact_banner_style()
    flags_html = await locations_body()
    flags_css = await locations_style()
    getInTouch_html = await get_in_touch_body()
    getInTouch_css = await get_in_touch_style()


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
            background-color: black;
        }}
        </style>
        {navbar_css}
        {footer_css}
        {heroSection_css}
        {flags_css}
        {getInTouch_css}
        </head>
        <body>
        {navbar_html}
        
        {heroSection_html}
        {flags_html}
        {getInTouch_html}
        
        {footer_html}
        </body>
    </html>
"""