These codes are based on the geodjango [tutorial(5.0)](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/tutorial/). 

The database is SpatiaLite which is the spatial extension to SQLite.

This project not only follow the steps in the geogjango tutorial but also implenments the below features:
* Google Map API V3 base in Geographic Admin

Requirements
============
* GEOS
* GDAL
* PROJ.4
* SpatiaLite
* PILLOW                                                                                                                    

SETUP
=====

Confiugre the setting
---------------------
Google MAP API key is needed for the project. Follow this [document](https://developers.google.com/maps/documentation/javascript/tutorial#api_key).
create .env file,
```env
GOOGLE_MAPS_API_KEY=
DEFAULT_MAP_CENTER=30.5,128.05
```

Initialize database and create admin user
---------------------


Import the world data into database
-----------------------------------
start the django shell
```python
from world import load
load.run()
```
