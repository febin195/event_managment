from django.db import models

# Create your models here.



class EventModel(models.Model):
    Title=models.CharField(max_length=100)
    Desc=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    date=models.DateField()
    org=models.CharField(max_length=100)




