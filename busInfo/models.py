from django.db import models

# Create your models here.

class BusNo(models.Model):
    bus_no=models.CharField(max_length=50)
    def __str__(self):
        return self.bus_no

class StopName(models.Model):
    stop_name=models.CharField(max_length=100)
    latitude=models.FloatField(null=True,blank=True)
    longitude=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.stop_name

class Route(models.Model):
    bus_id = models.ForeignKey(BusNo, on_delete=models.CASCADE)
    stop_id = models.ForeignKey(StopName, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.stop_id)
