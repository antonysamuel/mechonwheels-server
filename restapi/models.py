from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.gis.db.models.fields import PointField
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import AbstractUser, User
# Create your models here.


class   WorkshopAccount(models.Model):
    user = OneToOneField(User,on_delete=CASCADE)
    workshopName = models.CharField(max_length=60)
    address = models.CharField(max_length=50)
    phone = models.IntegerField(default=9999999999)
    latitude = models.DecimalField(max_digits=12, decimal_places=9,default=0)
    longitude = models.DecimalField(max_digits=12, decimal_places=9,default=0)
    location = models.PointField(default=Point(0.0, 0.0))
    def __str__(self):
        return self.workshopName


