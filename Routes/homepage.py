from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from Components.general_components.navbar import navbar
from Components.homepage_components.heroSection import heroSection
from Components.homepage_components.homePageStyle import homepageStyle
router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def homepage():
    navbar_html = await navbar()
    heroSection_html = await heroSection()
    homepageStyle_css = await homepageStyle()
    return f"""
    <html>
        <head>
            <title>Home Page/title>
            {homepageStyle_css}
            
        </head>
        <body>
            {navbar_html}
            {heroSection_html}
        </body>
    </html>
    """