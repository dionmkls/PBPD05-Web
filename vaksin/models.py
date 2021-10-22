from django.db import models

# Create your models here.
class Vaksin(models.Model):
    nama            = models.CharField(max_length=100)
    url             = models.CharField(max_length=100)
    alamat          = models.CharField(max_length=100)
    nomorTelp       = models.IntegerField() # max 12 digit
    jenis           = models.CharField(max_length=100)
    syaratPeserta   = models.CharField(max_length=100)
