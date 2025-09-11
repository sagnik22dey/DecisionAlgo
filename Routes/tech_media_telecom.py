from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from Components.general_components.navbar import *
from Components.general_components.footer import *
from Components.caseStudies_components.heroSection import *
from Components.caseStudies_components.robotSection import *
from Components.caseStudies_components.tech_media_telecom.trans_tech import *
from Components.caseStudies_components.our_perspective import *
from Components.caseStudies_components.tech_media_telecom.text import *



router = APIRouter()


@router.get("/casestudy/tech_media_telecom", response_class=HTMLResponse)
async def get_tech_media_telecom():
    navbar_html = await navbar_body()
    navbar_css = await navbar_style()
    footer_css = await footer_style()
    footer_html = await footer_body()
    heroSection_html = await heroSection_body("Maximizing SMB Growth &  Conversion")
    heroSection_css = await heroSection_style()
    robotSection_html = await robotSection_body(
        "tech_media_telecom",
        "Entertainment",
        "Telecom Services",
        "Broadcasting",
        "Advertising",
        "Digital Media",
    )
    robotSection_css = await robotSection_style()
    text_top_robot = await text_top_robot_section()
    style_top_robot = await style_top_robot_section()
    trans_tech_html = await trans_tech_body()
    trans_tech_css = await trans_tech_style()
    our_perspective_html = await our_perspective_body(
        "Connectivity And",
        "Communication",
        "Telecom plays a pivotal role in seamless communication and connectivity, supporting the digital era.",
        "Content",
        "Evolution",
        "In media and entertainment, we advocate for evolving content to engage audiences using cutting-edge technologies.",
        "Empowering",
        "Creativity",
        "We empower creative minds in media and entertainment, fostering originality and innovation."
    )
    our_perspective_css = await our_perspective_style()

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Case Studies</title>
        <style>
        
        body{{
            overflow-x: hidden;
        }}
        </style>
        
            {navbar_css}
            {heroSection_css}
            {footer_css}
            {robotSection_css}
            {trans_tech_css}
            {our_perspective_css}
            {style_top_robot}

    </head>
    <body>
        {navbar_html}
        {heroSection_html}
        {text_top_robot}
        {robotSection_html}
        {trans_tech_html}
        {our_perspective_html}
        {footer_html}
    </body>
    </html>

    """
    