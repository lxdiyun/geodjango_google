Initlaztion the database
=======================
``` shell
spatialite geodjango.db "SELECT InitSpatialMetaData();"
```

Then you can sync the database by syncdb

Import the world data into database
===================================
start the django shell
```python
    from world import load
    load.run()
```
