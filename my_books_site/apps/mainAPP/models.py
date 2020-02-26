from django.db import models

class city (models.Model):
    name = models.CharField(max_length= 40)
    country = models.CharField(max_length=40)
