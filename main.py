from fastapi import FastAPI, APIRouter, Form, Query, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional, Any
from pathlib import Path

# custom
from schemas import *
from user_settings import gridsettings, geo_variables
#from satellite_getter import *

#from pyroscopegridding import grid_ncf

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH))


app = FastAPI() #(title="Recipe API", openapi_url="/openapi.json")
api_router = APIRouter()

user_config = None

@api_router.get("/", status_code=200)
def root(request: Request) -> dict:
    """
    Root GET
    """
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request}
        #{"request": request, "gridsettings": gridsettings, "geo_variables": geo_variables},
    )

@app.post("/")
async def submit(request: Request,
                 gridsize: float = Form(...),
                 limit: str = Form(...),
                 fill_value: float = Form(...),
                 time_interval: float = Form(...),
                 start_date: str = Form(...),
                 start_time: str = Form(...),
                 end_date: str = Form(...),
                 end_time: str = Form(...),
                 
                 geo_var: str = Form(...),
                 phy_var: str = Form(...),
                 phy_var_nc: str = Form(...),
                 phy_var_hdf: str = Form(...),
                 pixel_range: str = Form(...)
                 ):
    
    #save into user configuration
    user_config = {"gridsize": gridsize,
            "limit": limit,
            "fill_value": fill_value,
            "time_interval": time_interval,
            "start_date" : start_date,
            "start_time" : start_time,
            "end_date" : end_date,
            "end_time" : end_time,
            
            
            "geo_var": geo_var,
            "phy_var": phy_var,
            "phy_var_nc": phy_var_nc,
            "phy_var_hdf": phy_var_hdf,
            "pixel_range": pixel_range
            
            }
    
    print(user_config)
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request}
    )


app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
