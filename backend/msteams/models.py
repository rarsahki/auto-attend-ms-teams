from django.db import models

# Create your models here.
class Msteams(models.Model):
    subject = models.CharField(max_length=10)
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)
    prof = models.CharField(max_length=100,default="Prof")
    time = models.CharField(max_length=5,default="00:00")
    days = models.CharField(max_length=27,default="MON")

