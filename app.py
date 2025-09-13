from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from Routes import healthcheck
from Routes import homepage
from Routes import dashboard
from Routes import aboutUs
from Routes import contactUs
from Routes import pricing
from Routes import customer_package_goods
from Routes import retail_firm
from Routes import finance
from Routes import insurance
from Routes import tech_media_telecom
from Routes import healthcare

app = FastAPI()

app.include_router(healthcheck.router)
app.include_router(homepage.router)
app.include_router(dashboard.router)
app.include_router(aboutUs.router)
app.include_router(contactUs.router)
app.include_router(pricing.router)
app.include_router(customer_package_goods.router)
app.include_router(retail_firm.router)
app.include_router(finance.router)
app.include_router(insurance.router)
app.include_router(tech_media_telecom.router)
app.include_router(healthcare.router)

app.mount("/Resources", StaticFiles(directory="Resources"), name="Resources")
app.mount("/Images", StaticFiles(directory="Resources/Images"), name="Images")


@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc):
    return JSONResponse(status_code=404, content={"message": "Page not found"})

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)