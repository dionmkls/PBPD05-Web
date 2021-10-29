from django.db import models

# Create your models here.

class FAQ(models.Model):
    question = models.TextField(max_length=4000)
    answer = models.TextField(max_length=4000)