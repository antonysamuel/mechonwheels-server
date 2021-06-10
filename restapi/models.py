from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.gis.db.models.fields import PointField
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, EmailField
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import AbstractUser, User
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class WorkshopAccount(models.Model):
    user = OneToOneField(User,on_delete=CASCADE)
    workshopName = models.CharField(max_length=60)
    address = models.CharField(max_length=50)
    phone = models.BigIntegerField(default=9999999999)
    latitude = models.DecimalField(max_digits=12, decimal_places=9,default=0)
    longitude = models.DecimalField(max_digits=12, decimal_places=9,default=0)
    location = models.PointField(default=Point(0.0, 0.0))
    def __str__(self):
        return self.workshopName


status_choices = (
    ('1','Pending'),    
    ('2','On Progress'),
    ('3','Completed'),
    ('4','Cancelled'),
)

class BookingDetails(models.Model):
    user = ForeignKey(User,on_delete=CASCADE)
    workshop = ForeignKey(WorkshopAccount,on_delete=CASCADE)
    msg = models.CharField(max_length=200,default=" ")
    created = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=9,default=0)
    longitude = models.DecimalField(max_digits=12, decimal_places=9,default=0)
    status = models.CharField(choices=status_choices,max_length=20,default='1')  

    


    def __str__(self):
        return str(self.created)


#//////////////////////////////////////////#
def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class Products(models.Model):
    workshop = ForeignKey(WorkshopAccount,on_delete=CASCADE,null=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250,default="No Description")
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)

    def __str__(self):
        return self.name

order_status_choices = (
    ('1','Pending'),    
    ('2','On the Way'),
    ('3','Delivered'),
    ('4','Cancelled'),
)



class Orders(models.Model):
    product = ForeignKey(Products,on_delete=CASCADE)
    user = ForeignKey(User,on_delete=CASCADE)
    address = models.CharField(max_length=200)
    status = models.CharField(choices=order_status_choices,max_length=20,default='1')
    latitude = models.DecimalField(max_digits=12, decimal_places=9,default=0)
    longitude = models.DecimalField(max_digits=12, decimal_places=9,default=0)

class Cart(models.Model):
    user = ForeignKey(User,on_delete=CASCADE)
    product = ForeignKey(Products,on_delete=CASCADE)
