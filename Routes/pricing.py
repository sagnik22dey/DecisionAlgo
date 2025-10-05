from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import *
from Components.homepage_components.heroSection import *
from Components.general_components.footer import *
from Components.pricing_components.heroSection import *
from Components.pricing_components.plans import *
from Components.pricing_components.get_in_touch import *
from Components.pricing_components.customSolutions import *


router = APIRouter()


@router.get("/pricing", response_class=HTMLResponse)
async def pricing():
    navbar_html = await navbar_body()
    navbar_css = await navbar_style()
    footer_html = await footer_body()
    footer_css = await footer_style()
    heroSection_html = await pricing_banner_body()
    heroSection_css = await pricing_banner_style()
    plans_html = await plans_body()
    plans_css = await plans_style()
    getInTouch_html = await get_in_touch_body()
    getInTouch_css = await get_in_touch_style()
    getInTouch_script = await get_in_touch_script()
    customSolutions_html = await custom_solutions_body()
    customSolutions_css = await custom_solutions_style()



    return f"""
    <html>
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Import Fonts from Google Fonts -->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@700&family=Jost:wght@400&family=Poppins:wght@400&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;500;600;700&display=swap" rel="stylesheet">
        <!-- EmailJS SDK -->
        <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
        <title>Pricing</title>
        
        {navbar_css}
        {footer_css}
        {heroSection_css}
        {plans_css}
    
        {getInTouch_css}
        {customSolutions_css}

    </head>
    <body>
        {navbar_html}
        {heroSection_html}
        {plans_html}

        {customSolutions_html}
        {getInTouch_html}
        {footer_html}
        {getInTouch_script}

    </body>
    </html>
    """