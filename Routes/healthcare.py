from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from Components.general_components.navbar import *
from Components.general_components.footer import *
from Components.caseStudies_components.heroSection import *
from Components.caseStudies_components.robotSection import *
from Components.caseStudies_components.healthcare.trans_health import *
from Components.caseStudies_components.our_perspective import *
from Components.caseStudies_components.healthcare.text import *



router = APIRouter()


@router.get("/casestudy/healthcare", response_class=HTMLResponse)
async def get_healthcare():
    navbar_html = await navbar_body()
    navbar_css = await navbar_style()
    footer_css = await footer_style()
    footer_html = await footer_body()
    heroSection_html = await heroSection_body("Pioneering the Future of Health with AI and Data Science")
    heroSection_css = await heroSection_style()
    robotSection_html = await robotSection_body(
        "healthcare",
        "Biotechnology",
        "Medical Devices",
        "Telehealth and Telemedicine",
        "Pharmaceuticals",
        "Diagnostic Laboratories",
    )
    robotSection_css = await robotSection_style()
    text_top_robot = await text_top_robot_section()
    style_top_robot = await style_top_robot_section()
    trans_health_html = await trans_health_body()
    trans_health_css = await trans_health_style()
    our_perspective_html = await our_perspective_body(
        "Medical",
        "Advancements",
        "Our focus is on driving innovations for state-of-the-art healthcare.",
        "Data-Driven",
        "Healthcare",
        "We harness data for evidence-based decisions and improved outcomes.",
        "Life Sciences",
        "Innovation",
        "We drive innovation in pharmaceuticals, biotechnology, and medical devices."
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
            {trans_health_css}
            {our_perspective_css}
            {style_top_robot}

    </head>
    <body>
        {navbar_html}
        {heroSection_html}
        {text_top_robot}
        {robotSection_html}
        {trans_health_html}
        {our_perspective_html}
        {footer_html}
    </body>
    </html>

    """
    