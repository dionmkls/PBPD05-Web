from django.db import models

class Information(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    sumber =  models.CharField(max_length=100)