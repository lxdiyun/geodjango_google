from django.contrib.gis.db import models

class GMapPoint(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "GMap Points"

class GMapPointImage(models.Model):
    map_point = models.ForeignKey(GMapPoint, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gmap_images/')

    def __str__(self):
        return f"Image for {self.map_point.name}"


