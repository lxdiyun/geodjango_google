spatialite geodjango.db "SELECT InitSpatialMetaData();"
syncdb

shell
>>> from world import load
>>> load.run()
