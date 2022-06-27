from django.db import models

# Create your models here.
class Schools(models.Model):
    name = models.Charfield(max_length=23)
    address = models.Charfield(max_length=23)

class Country(models.Model):
    name = models.Charfield(max_length=23)





