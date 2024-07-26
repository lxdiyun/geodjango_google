These codes are based on the geodjango [tutorial(5.0)](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/tutorial/). 

The database is SpatiaLite which is the spatial extension to SQLite.

This project not only follow the steps in the geogjango tutorial but also implenments the below features:
* Google Map API V3 base in Geographic Admin.[gmap app](gmap/)
* Gaode(高德) AMap API V2 base in Geographic Admin.[amap app](amap/)
* Use Google maps to display GMapPoints(http://localhost:8000/gmap/gmap_points). 
* Use Google maps to display AMapPoints(http://localhost:8000/amap/gmap_points). 
* Use AMap to display AMapPoints(http://localhost:8000/amap/amap_points). 
* Use AMap to display GMapPoints(http://localhost:8000/gmap/amap_points). 

Requirements
============
* GEOS
* GDAL
* PROJ.4
* SpatiaLite
* PILLOW                                                                                                                    

SETUP
=====

Install required libraries 
---------------------
One method is use conda and follow up the steps in [conda_init_steps.txt](conda_init_steps.txt)

Confiugre the setting
---------------------
Google MAP API key is needed for the project. Follow this [document](https://developers.google.com/maps/documentation/javascript/tutorial#api_key).
Or use AMAP API key and security key. Follow this [document](https://lbs.amap.com/api/javascript-api-v2)
create .env file,
```env
# Google Maps settings
GOOGLE_MAPS_API_KEY=
DEFAULT_GMAP_CENTER=30.5,128.05

# AMap settings
AMAP_SECURITY_JS_CODE=
AMAP_API_KEY=
DEFAULT_AMAP_CENTER=30.5,128.05
```

Initialize database and create admin user
---------------------
```shell
python manage.py migrate
python manage.py createsuperuser
```


Import the world data into database
-----------------------------------
start the django shell
```python
from world import load
load.run()
```
