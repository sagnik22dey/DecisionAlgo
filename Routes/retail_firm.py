from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from Components.general_components.navbar import *
from Components.general_components.footer import *
from Components.caseStudies_components.heroSection import *
from Components.caseStudies_components.robotSection import *
from Components.caseStudies_components.retail.text import *
from Components.caseStudies_components.retail.our_offerings import *
from Components.caseStudies_components.retail.robustData import *
from Components.caseStudies_components.retail.unleash import *
from Components.caseStudies_components.retail.future_of_retail import *
from Components.caseStudies_components.our_perspective import *


router = APIRouter()


@router.get("/casestudy/retail_firm", response_class=HTMLResponse)
async def get_retail_firm():
    navbar_html = await navbar_body()
    navbar_css = await navbar_style()
    footer_css = await footer_style()
    footer_html = await footer_body()
    heroSection_html = await heroSection_body("Retail Firms Adapting to AI Era")
    heroSection_css = await heroSection_style()
    robotSection_html = await robotSection_body(
        "retail",
        "Fashion & Apparel",
        "Electronics & Gadgets",
        "Books & Entertainment",
        "Home & Living",
        "Auto & Accessories",
    )
    robotSection_css = await robotSection_style()
    text_top_robot = await text_top_robot_section()
    style_top_robot = await style_top_robot_section()
    our_offerings_html = await our_offerings_body()
    our_offerings_css = await our_offerings_style()
    robustData_html = await robustData_body()
    robustData_css = await robustData_style()
    unleash_html = await unleash_body()
    unleash_css = await unleash_style()
    future_of_retail_html = await future_of_retail_body()
    future_of_retail_css = await future_of_retail_style()
    our_perspective_html = await our_perspective_body(
        "AI's Role In",
        "Decision-Making",
        "Uncover the critical role that artificial intelligence plays in making informed, data-backed decisions.",
        "Data-Driven",
        "Transformations",
        "Delve into real-world examples of how data and AI have transformed industries and businesses.",
        "Intelligence",
        "Beyond Numbers",
        "See how data and AI provide a depth of understanding that goes beyond raw data points.",
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
        
        @media(max-width: 767px){{
            *{{
                font-family: 'Exo 2', sans-serif !important;
            }}
        }}
        
        </style>
        
            {navbar_css}
            {heroSection_css}
            {footer_css}
            {robotSection_css}
            {style_top_robot}
            {our_offerings_css}
            {robustData_css}
            {unleash_css}
            {future_of_retail_css}
            {our_perspective_css}

    </head>
    <body>
        {navbar_html}
        {heroSection_html}
        {text_top_robot}
        {robotSection_html}
        {our_offerings_html}
        {robustData_html}
        {unleash_html}
        {future_of_retail_html}
        {our_perspective_html}
        {footer_html}
    </body>
    </html>
"""
