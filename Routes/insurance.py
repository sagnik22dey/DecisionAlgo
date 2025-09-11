from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from Components.general_components.navbar import *
from Components.general_components.footer import *
from Components.caseStudies_components.heroSection import *
from Components.caseStudies_components.robotSection import *
from Components.caseStudies_components.insurance.trans_insurance import *
from Components.caseStudies_components.our_perspective import *
from Components.caseStudies_components.insurance.text import *



router = APIRouter()


@router.get("/casestudy/insurance", response_class=HTMLResponse)
async def get_insurance():
    navbar_html = await navbar_body()
    navbar_css = await navbar_style()
    footer_css = await footer_style()
    footer_html = await footer_body()
    heroSection_html = await heroSection_body("Unlocking Full Client Potential at Every Stage")
    heroSection_css = await heroSection_style()
    robotSection_html = await robotSection_body(
        "insurance",
        "Travel Insurance",
        "Reinsurance",
        "Commercial Insurance",
        "Medical Insurance",
        "Life Insurance",
    )
    robotSection_css = await robotSection_style()
    text_top_robot = await text_top_robot_section()
    style_top_robot = await style_top_robot_section()
    trans_insurance_html = await trans_insurance_body()
    trans_insurance_css = await trans_insurance_style()
    our_perspective_html = await our_perspective_body(
        "Claims",
        "Efficiency",
        "We prioritize efficient claims processing, reducing costs and ensuring prompt settlements.",
        "Operational",
        "Excellence",
        "Our focus is on operational excellence, streamlining processes and optimizing resources.",
        "Compliance",
        "Assurance",
        "Our perspective ensures confidence in regulatory compliance through real-time monitoring."
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
            {trans_insurance_css}
            {our_perspective_css}
            {style_top_robot}

    </head>
    <body>
        {navbar_html}
        {heroSection_html}
        {text_top_robot}
        {robotSection_html}
        {trans_insurance_html}
        {our_perspective_html}
        {footer_html}
    </body>
    </html>

    """
    