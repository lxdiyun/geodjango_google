These codes are based on the geodjango [tutorial](https://docs.djangoproject.com/en/1.5/ref/contrib/gis/tutorial/). 

The database is SpatiaLite which is the spatial extension to SQLite.

This project not only follow the steps in the geogjango tutorial but also implenments the below features:
* Google Map API V2 base layer in Geographic Admin (GeoDjango)(Based on [snippets](http://djangosnippets.org/snippets/1144/)). APP [world](world/)
* Google Map API V3 base layer in Geographic Admin (Based on [snippets](http://djangosnippets.org/snippets/2839/)). APP [gmap](gmap/)
* Simple Goolge Map and Marker frontpage, using JS Library [Gmaps.js](http://hpneo.github.io/gmaps/ )
* [Bootstrap](http://twitter.github.io/bootstrap/) based frontpage UI
* Ajax hanlder for Google marker chick event, with the help of [Dajax](http://www.dajaxproject.com/)
* Image gallery based on [django-imagekit][1], [Bootstrap-Image-Gallery][2] and [blueimp Gallery][3]
   [1]: https://github.com/matthewwithanm/django-imagekit 
   [2]: https://github.com/blueimp/Bootstrap-Image-Gallery
   [3]: https://github.com/blueimp/Gallery

Requirements
============
* GEOS
* GDAL
* PROJ.4
* SpatiaLite
* pysqlite2
* PIL                                                                                                                    
* [django-imagekit](https://github.com/matthewwithanm/django-imagekit)
* dajaxice
* [dajax](http://www.dajaxproject.com/)
* [django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar)

SETUP
=====

Confiugre the setting
---------------------
Google MAP API key is needed for the project. Follow this [document](https://developers.google.com/maps/documentation/javascript/tutorial#api_key). Remeber to toggle the Google MAPs API V2 and V3 in the Service menu.
After that, update path, key and url in [django project setting file](geodjango/settings.py)
```python
MEDIA_ROOT = '$YOURT_MEdIA_PATH'
STATIC_ROOT = '$YOUR_STATIC_PATH'
...
GOOGLE_MAPS_API_KEY = '$GOOGLE_API_KEY'
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/js'
```

Setup the database
-------------------
use spatialite to generate the splite file. More information can be find at [here](https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/spatialite/)
``` shell
$spatialite geodjango.db "SELECT InitSpatialMetaData();"
the SPATIAL_REF_SYS table already contains some row(s)
 InitSpatiaMetaData ()error:"table spatial_ref_sys already exists"
0
```
The error messages shown can be safely ignore.

Then sync the database by syncdb

Import the world data into database
-----------------------------------
start the django shell
```python
from world import load
load.run()
```
