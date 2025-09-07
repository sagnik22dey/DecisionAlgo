from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import *
from Components.general_components.footer import *
from Components.aboutUs_components.heroSection import *
from Components.aboutUs_components.comapnies import *
from Components.aboutUs_components.innovation import *
from Components.aboutUs_components.team import *



router = APIRouter()


@router.get("/aboutus", response_class=HTMLResponse)
async def aboutUs():
    
    navbar_css = await navbar_style()
    navbar_html = await navbar_body()
    footer_html = await footer_body()
    footer_css = await footer_style()
    heroSection_html = await heroSection_body()
    heroSection_css = await heroSection_style()
    companies_html = await companies_body()
    companies_css = await companies_style()
    innovation_html = await innovation_body()
    innovation_css = await innovation_style()
    team_html= await team_body()
    team_css = await team_style()
    
    


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
        </style>
        {navbar_css}
        {footer_css}
        {heroSection_css}
        {companies_css}
        {innovation_css}
        {team_css}

        </head>
        <body>
        {navbar_html}
        {heroSection_html}
        {companies_html}
        {innovation_html}
        {team_html}
        {footer_html}
            
            
        </body>


    

    """
    