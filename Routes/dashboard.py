from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import *
from Components.general_components.footer import *
from Components.dashboard_components.heroSection import *
from Components.dashboard_components.dashboard_love import *
from Components.dashboard_components.dashboard_text_cards import *
from Components.homepage_components.client_feedback import *
from Components.dashboard_components.track import *

router = APIRouter()


@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard():

    navabar_html = await navbar_body()
    footer_html = await footer_body()
    navabar_css = await navbar_style()
    footer_css = await footer_style()
    hero_section_html = await heroSection_body()
    hero_section_css = await heroSection_style()
    dashboard_love_html = await dashboard_love_body()
    dashboard_love_css = await dashboard_love_style()
    dashboard_text_cards_smart_html = await smart_simple_body()
    dashboard_text_cards_see_data_html = await see_data_body()
    dashboard_text_cards_css = await dashboard_text_cards_style()
    client_feedback_html = await client_feedback_body()
    client_feedback_css = await client_feedback_style()
    track_html = await track_body()
    track_css = await track_style()

    return f""" 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard</title>  
        <style>
            body, html {{
                overflow-x: hidden;
            }}
        </style>
        {navabar_css}
        {footer_css}
        {hero_section_css}
        {dashboard_love_css}
        {dashboard_text_cards_css}
        {client_feedback_css}
        {track_css}
    </head>
    <body>
        {navabar_html}
        {hero_section_html}
        {dashboard_love_html}
        {track_html}
        {dashboard_text_cards_smart_html}
        {client_feedback_html}
        {dashboard_text_cards_see_data_html}
        {footer_html}
    </body>
    </html>
    """
