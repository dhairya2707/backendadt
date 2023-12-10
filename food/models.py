from django.db import models

# Create your models here.

class Food(models.Model):
    studentId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    RegistrationNo = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)

class Crops(models.Model):
    CountryName = models.CharField(db_column='CountryName', max_length=30, blank=True)  # Field name made lowercase.
    item = models.CharField(max_length=30, blank=True)
    element = models.CharField(max_length=20, blank=True)
    year = models.IntegerField(blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True)
    value = models.IntegerField(blank=True, null=True)
    CropId = models.AutoField(db_column='CropId', primary_key=True)
    




