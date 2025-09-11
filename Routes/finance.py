from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from Components.general_components.navbar import *
from Components.general_components.footer import *
from Components.caseStudies_components.heroSection import *
from Components.caseStudies_components.robotSection import *
from Components.caseStudies_components.finance.trans_Finance import *
from Components.caseStudies_components.our_perspective import *
from Components.caseStudies_components.finance.text import *



router = APIRouter()


@router.get("/casestudy/finance", response_class=HTMLResponse)
async def get_finance():
    navbar_html = await navbar_body()
    navbar_css = await navbar_style()
    footer_css = await footer_style()
    footer_html = await footer_body()
    heroSection_html = await heroSection_body("Unlocking Full Client Potential at Every Stage")
    heroSection_css = await heroSection_style()
    robotSection_html = await robotSection_body(
        "finance",
        "Sustainable Finance",
        "Banking & Lending",
        "Financial Technology (FinTech)",
        "Debt Management",
        "Asset Management",
    )
    robotSection_css = await robotSection_style()
    text_top_robot = await text_top_robot_section()
    style_top_robot = await style_top_robot_section()
    trans_Finance_html = await trans_Finance_body()
    trans_Finance_css = await trans_Finance_style()
    our_perspective_html = await our_perspective_body(
        "Data-Driven",
        "Finance",
        "Embrace the power of data analytics and AI to drive financial decisions, optimize operations, and enhance customer experiences.",
        "Agile",
        "Transformations",
        "Embrace agility and adaptability to swiftly respond to changing market dynamics and evolving customer demands.",
        "FinTech",
        "Collaboration",
        "Forge strategic partnerships with fintech innovators to unlock new possibilities and stay at the forefront of digital finance."
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
            {trans_Finance_css}
            {our_perspective_css}
            {style_top_robot}

    </head>
    <body>
        {navbar_html}
        {heroSection_html}
        {text_top_robot}
        {robotSection_html}
        {trans_Finance_html}
        {our_perspective_html}
        {footer_html}
    </body>
    </html>

    """
    