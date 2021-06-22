from django.db import models

class test(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
