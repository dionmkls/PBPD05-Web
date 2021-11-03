from django.db import models


class Oksigen(models.Model):
    url = models.CharField(max_length=30)
    alamat = models.CharField(max_length=30)
    telepon = models.CharField(max_length=30)