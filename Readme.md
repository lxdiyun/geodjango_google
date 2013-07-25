These code are based on the geodjango tutorial at https://docs.djangoproject.com/en/1.5/ref/contrib/gis/tutorial/. 
The database is SpatiaLite which is the spatial extension to SQLite.
This project not only implements the steps in the tutorial but also implenments the below features:
* Google Map API V2 base layer in Geographic Admin (GeoDjango)(Based on snippets http://djangosnippets.org/snippets/1144/ )
    File: (world/admin.py) (world/templates/gis/admin/google.html) (world/templates/gis/admin/google.js)
* Google Map API V3 base layer in Geographic Admin (Based on snippets http://djangosnippets.org/snippets/2839/)

Requirements
------------
* GEOS
* GDAL
* PROJ.4
* SpatiaLite
* pysqlite2
* PIL                                                                                                                    
* django-imagekit (https://github.com/matthewwithanm/django-imagekit)
* dajaxice
* dajax(http://www.dajaxproject.com/)

Initial the database
-----------------------
``` shell
spatialite geodjango.db "SELECT InitSpatialMetaData();"
```

Then you can sync the database by syncdb

Import the world data into database
-----------------------------------
start the django shell
```python
from world import load
load.run()
```
