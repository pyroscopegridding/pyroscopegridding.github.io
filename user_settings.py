# gridsetting user dict
#initially set as defaults
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

uploaded_files = None