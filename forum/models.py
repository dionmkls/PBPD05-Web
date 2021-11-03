from django.db import models

# Create your models here.

class Forum(models.Model):
    ForumTitle = models.CharField(max_length=15)
    ForumFrom = models.CharField(max_length=20)
    ForumMessage = models.CharField(max_length=350)
