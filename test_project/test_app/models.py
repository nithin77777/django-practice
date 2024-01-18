from django.db import models


# Start from here
from django.db import models





class Details(models.Model):
    job_id = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    job = models.CharField(max_length=50)
    salary = models.IntegerField()

