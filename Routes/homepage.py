from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import *
from Components.homepage_components.heroSection import *
from Components.homepage_components.homePageStyle import homepageStyle
from Components.homepage_components.robotSection import *
from Components.general_components.footer import *
from Components.homepage_components.business_trust import *
from Components.homepage_components.client_feedback import *
from Components.homepage_components.ready import *


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
    robotScript = await robot_script()
    footer_html = await footer_body()
    footer_css = await footer_style()
    business_trust_html = await trust_body()
    business_trust_css = await trust_style()
    busiiness_trust_script = await trust_script()
    client_feedback_html = await client_feedback_body()
    client_feedback_css = await client_feedback_style()
    ready_html = await ready_body()
    ready_css = await ready_style()
    
    
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
        {business_trust_css}
        {client_feedback_css}
        {ready_css}
        {footer_css}
        {robotScript}
        {busiiness_trust_script}
        </head>
        <body>
            {navbar_html}
            {heroSection_html}
            {robotSection_html}
            {business_trust_html}
            {client_feedback_html}
            {ready_html}
            {footer_html}
        </body>
    </html>
    """
