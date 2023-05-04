from fastapi import FastAPI, APIRouter, Form, Query, HTTPException, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, Any, List
from pathlib import Path

# custom
from schemas import *
#from user_settings import configuration, uploaded_files
#from satellite_getter import *

#from pyroscopegridding import grid_ncf

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH))


app = FastAPI() #(title="Recipe API", openapi_url="/openapi.json")
api_router = APIRouter()

#app.mount("/", StaticFiles(directory="static",html = True), name="static")

#saved data
configuration = {
    "gridsize":0.25,
    "limit": [-89.875, 89.875, -179.875, 179.875] ,
    "fill_value": -9999., #default is NAN
    "time_interval": 30, #minute intervals that will be split
    "time_start": "2019/07/27/00/00", # year/month/day/hour/min
    "time_end": "2019/07/27/00/29",   # year/month/day/hour/min
    "geo_var": ["latitude", "longitude"] #default (what geophysical variables are mapped to)
    ,"phy_var": ["Sensor_Zenith", "Scattering_Angle", "Image_Optical_Depth_Land_And_Ocean", "Optical_Depth_Land_And_Ocean"] # output names and master list
    ,"phy_var_nc": ["sensor_zenith_angle", "Scattering_Angle", "Image_Optical_Depth_Land_And_Ocean", "Optical_Depth_Land_And_Ocean"] # geophysical variables netCDF
    ,"phy_var_hdf": ["Sensor_Zenith", "Scattering_Angle", "Image_Optical_Depth_Land_And_Ocean","Optical_Depth_Land_And_Ocean"] # geophysical variables hdf
    ,"pixel_range": [0, 500] # Range for pixel count at single pixel
}
filenames = []
uploaded_files = []

"""
@api_router.get("/", status_code=200)
def root(request: Request) -> dict:
    
    #Root GET
    
    return TEMPLATES.TemplateResponse(
        "index.html",
        {"request": request}
    )
""" 
@app.get("/")
async def index(request: Request):
    return TEMPLATES.TemplateResponse("index.html", {"request": request})

# get user request information
@app.post("/config")
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
    
    #time string edit
    
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
    
    #save into configuration
    configuration["gridsize"] = user_config["gridsize"] 
    configuration["limit"] = user_config["limit"] 
    configuration["time_interval"] = user_config["time_interval"]
    configuration["start_date"] = user_config["start_date"] 
    configuration["end_date"] = user_config["end_date"] 
    configuration["end_time"] = user_config["end_time"] 
    configuration["geo_var"] = user_config["geo_var"] 
    configuration["phy_var"] = user_config["phy_var"]  
    configuration["phy_var_nc"] = user_config["phy_var_nc"] 
    configuration["phy_var_hdf"] = user_config["phy_var_hdf"] 
    configuration["pixel_range"] = user_config["pixel_range"] 
    
    print("Uploaded files: ", uploaded_files)
    #print("User configuration: ", user_config)
    
    user_config_html = """
    <html>
        <head>
            <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
        </head>
        <body>
            <h2 class="mb-8 text-2xl font-medium text-white">
                User Configurations:
            </h2>
            <br>
            <p id = "user_config" class="text-base text-white">"""
    user_config_html = user_config_html + str(configuration)
    user_config_html = user_config_html + """
            </p>
            <br><br>
        </body>
    </html>
    """
    print(configuration)
    return HTMLResponse(content=user_config_html, status_code=200)

#file upload
@app.post("/file")
async def submit_file(request: Request,
                      #file: UploadFile = File(...)):
                      file: List[UploadFile]):
    filenames.extend([f.filename for f in file])
    uploaded_files.extend(file)
    print("Saved config: ", configuration)
    print("Uploaded files: ", uploaded_files)
    print("filenames" , filenames)
    
    file_upload_html =  """
    <html>
        <head>
            <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
        </head>
        <body>
            <h2 class="mb-8 text-2xl font-medium text-white">
                Files Uploaded:
            </h2>
            <br>
            <p id="file_uploads" class="text-base text-white">"""
    file_upload_html = file_upload_html + str(filenames)
    file_upload_html = file_upload_html + """
            </p>
            <br><br>
        </body>
    </html>
    """
    print(configuration)
    return HTMLResponse(content=file_upload_html, status_code=200)


app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
