from django.db import models

class Service(models.Model):
    name = models.CharField(max_length = 30)
    details = models.CharField(max_length = 1000)
    truth = models.BooleanField(max_length = 1)
    rating = models.PositiveSmallIntegerField()