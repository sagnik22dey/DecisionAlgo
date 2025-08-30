from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import *
from Components.homepage_components.heroSection import *
from Components.homepage_components.homePageStyle import homepageStyle
from Components.homepage_components.robotSection import *
from Components.general_components.footer import *


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def homepage():
    navbar_html = await navbar_body()
    heroSection_html = await heroSection_body()
    homepageStyle_css = await homepageStyle()
    navbar_css = await navbar_style()
    heroSection_css = await heroSection_style()
    robotSection_html= await robot_body()
    robotSection_css= await robot_style()
    footer_html = await footer_body()
    footer_css = await footer_style()
    
    
    
    return f"""
    <html>
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Import Fonts from Google Fonts -->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@700&family=Jost:wght@400&family=Poppins:wght@400&display=swap" rel="stylesheet">
        <title>Home Page</title>
        {homepageStyle_css}
        {navbar_css}
        {heroSection_css}  
        {robotSection_css}
        {footer_css}
        </head>
        <body>
            {navbar_html}
            {heroSection_html}
            {robotSection_html}
            
            {footer_html}
        </body>
    </html>
    """
