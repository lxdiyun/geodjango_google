from django.contrib.gis.db import models

class AMapPoint(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "AMap Points"

class AMapPointImage(models.Model):
    map_point = models.ForeignKey(AMapPoint, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='amap_images/')

    def __str__(self):
        return f"Image for {self.map_point.name}"


