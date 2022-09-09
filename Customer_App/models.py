from django.db import models
from jsonfield import JSONField

# Create your models here.
class Customer_data(models.Model):
    name = models.CharField(max_length=100,blank=True,default='')
    email = models.EmailField(max_length=100,blank=True)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=100,blank=True)
    phone_number = models.CharField(max_length=12)
    address_details = JSONField(default={})
    house_num = models.CharField(max_length=100,blank=True)
    street = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    workExperience = JSONField(default={})
    companyName = models.CharField(max_length=100,blank=True)
    fromDate = models.CharField(max_length=100,blank=True)
    toDate = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    qualifications = JSONField()
    qualificationName = models.CharField(max_length=100,blank=True)
    quafromDate = models.CharField(max_length=100,blank=True)
    quaToDate = models.CharField(max_length=100,blank=True)
    percentage = models.FloatField(max_length = 1000,blank=True)
    projects = JSONField()
    title = models.CharField(max_length=100,blank=True)
    description = models.CharField(max_length=100,blank=True)
    photo = models.CharField(max_length=100000,blank=True)

    # def __str__(self):
    #     pass

