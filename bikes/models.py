from django.db import models


# Create your models here.
class Bikes(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    active = models.TextField(default='yeah, cool')
