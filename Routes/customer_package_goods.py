from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import *
from Components.general_components.footer import *
from Components.caseStudies_components.heroSection import *
from Components.caseStudies_components.customert_package_goods.text import *
from Components.caseStudies_components.robotSection import *
from Components.caseStudies_components.customert_package_goods.top_business import *
from Components.caseStudies_components.customert_package_goods.our_offerings import *
from Components.caseStudies_components.customert_package_goods.client_feedback import *


router = APIRouter()


@router.get("/casestudy/customer_package_goods", response_class=HTMLResponse)
async def customer_package_goods():
    navbar_html = await navbar_body()
    footer_html = await footer_body()
    navbar_css = await navbar_style()
    footer_css = await footer_style()
    heroSection_html = await heroSection_body("Fueling Consumer Goods Growth with AI.")
    heroSection_css = await heroSection_style()
    robotSection_html = await robotSection_body("customer","Beauty & Hair Care","Health & Wellness","Home Care","Personal & Fabric Care","Packaged Food & Beverages")
    robotSection_css = await robotSection_style()
    top_business_html = await top_business_body()
    top_business_css = await top_business_style()
    our_offerings_html = await our_offerings_body()
    our_offerings_css = await our_offerings_style()
    client_feedback_html = await client_feedback_body()
    client_feedback_css = await client_feedback_style()
    text_top_robot_section_html = await text_top_robot_section()
    text_top_robot_section_css = await style_top_robot_section()


    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Case Studies</title>
        
            {navbar_css}
            {heroSection_css}
            {footer_css}
            {robotSection_css}
            {top_business_css}
            {our_offerings_css}
            {client_feedback_css}
            {text_top_robot_section_css}

    </head>
    <body>
        {navbar_html}
        {heroSection_html}
        {text_top_robot_section_html}
        {robotSection_html}
        {top_business_html}
        {our_offerings_html}
        {client_feedback_html}
        {footer_html}
    </body>
    </html>
    """