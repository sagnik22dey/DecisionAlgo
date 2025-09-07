from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import *
from Components.homepage_components.heroSection import *
from Components.general_components.footer import *
from Components.pricing_components.heroSection import *



router = APIRouter()


@router.get("/pricing", response_class=HTMLResponse)
async def pricing():
    navbar_html = await navbar_body()
    navbar_css = await navbar_style()
    footer_html = await footer_body()
    footer_css = await footer_style()
    footerScript = await footer_script()
    heroSection_html = await pricing_banner_body()
    heroSection_css = await pricing_banner_style()


    return f"""
    <html>
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Import Fonts from Google Fonts -->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@700&family=Jost:wght@400&family=Poppins:wght@400&display=swap" rel="stylesheet">
        <title>Pricing</title>
        
        {navbar_css}
        {footer_css}
        {footerScript}
        {heroSection_css}
    </head>
    <body>
        {navbar_html}
        {heroSection_html}
        {footer_html}
        
    </body>
    </html>
    """