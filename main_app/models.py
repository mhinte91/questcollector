from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=100)
    hero_class = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    level = models.IntegerField()