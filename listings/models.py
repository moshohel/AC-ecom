from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    ac_type = models.CharField(max_length=200, default='Split AC')
    fan_speed = models.CharField(
        max_length=100, default='Multi Fan Speeds and Wide Angel Louvers')
    cooling_speed = models.CharField(
        max_length=100, default='Turbo and Max Speed Cooling')
    energy_efficient = models.CharField(max_length=100, default='Inverter')
    # zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True, default=None)
    price = models.IntegerField(default=None)
    air_control = models.TextField(blank=True, default='Air Flow 5400')
    remote_control = models.CharField(max_length=10, default='YES')
    timer = models.CharField(max_length=10, default='YES')
    temperature_adjustment = models.CharField(max_length=100, default='AUTO')
    # garage = models.IntegerField(default=0)
    sqft = models.IntegerField(default=None)
    ton = models.IntegerField(max_length=10, default=None)
    btu = models.DecimalField(max_digits=10, decimal_places=1, default=1200)
    # lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
