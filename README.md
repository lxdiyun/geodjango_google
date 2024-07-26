# GeoDjango Tutorial Project

These codes are based on the GeoDjango [tutorial (5.0)](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/tutorial/).

The database used is SpatiaLite, which is the spatial extension to SQLite.

This project not only follows the steps in the GeoDjango tutorial but also implements the features below:
* Integration with Google Maps API V3 in the Geographic Admin. [gmap app](gmap/)
* Integration with Gaode (高德) AMap API V2 in the Geographic Admin. [amap app](amap/)
* Display of GMapPoints using Google Maps (http://localhost:8000/gmap/gmap_points).
* Display of AMapPoints using Google Maps (http://localhost:8000/amap/gmap_points).
* Display of AMapPoints using AMap (http://localhost:8000/amap/amap_points).
* Display of GMapPoints using AMap (http://localhost:8000/gmap/amap_points).

## Requirements

- GEOS
- GDAL
- PROJ.4
- SpatiaLite
- Pillow

## Setup

### Install Required Libraries

One method is to use Conda and follow the steps in [conda_init_steps.txt](conda_init_steps.txt).

### Configure Settings
A Google Maps API key is required for the project. Follow this [documentation](https://developers.google.com/maps/documentation/javascript/tutorial#api_key) to obtain one.
Alternatively, you can use an AMap API key and security code. Follow this [documentation](https://lbs.amap.com/api/javascript-api-v2) to create a `.env` file:
```env
# Google Maps settings
GOOGLE_MAPS_API_KEY=
DEFAULT_GMAP_CENTER=30.5,128.05

# AMap settings
AMAP_SECURITY_JS_CODE=
AMAP_API_KEY=
DEFAULT_AMAP_CENTER=30.5,128.05
```

### Initialize Database and Create Admin User
Run the following commands:
```shell
python manage.py migrate
python manage.py createsuperuser
```

### Import World Data into the Database
Start the Django shell and execute:
```shell
python manage.py shell
from world import load
load.run()
```
