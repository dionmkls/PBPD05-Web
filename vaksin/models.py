from django.db import models

# Create your models here.
class VaksinJakarta(models.Model):
    nama = models.CharField(max_length=50)
    url = models.CharField(max_length=1000)
    alamat = models.CharField(max_length=50)
    nomorTelp = models.IntegerField() # max 12 digit
    jenis = models.CharField(max_length=50)
    syaratPeserta = models.CharField(max_length=50)
class VaksinBogor(models.Model):
    nama = models.CharField(max_length=50)
    url = models.CharField(max_length=1000)
    alamat = models.CharField(max_length=50)
    nomorTelp = models.IntegerField() # max 12 digit
    jenis = models.CharField(max_length=50)
    syaratPeserta = models.CharField(max_length=50)
class VaksinDepok(models.Model):
    nama = models.CharField(max_length=50)
    url = models.CharField(max_length=1000)
    alamat = models.CharField(max_length=50)
    nomorTelp = models.IntegerField() # max 12 digit
    jenis = models.CharField(max_length=50)
    syaratPeserta = models.CharField(max_length=50)
class VaksinTangerang(models.Model):
    nama = models.CharField(max_length=50)
    url = models.CharField(max_length=1000)
    alamat = models.CharField(max_length=50)
    nomorTelp = models.IntegerField() # max 12 digit
    jenis = models.CharField(max_length=50)
    syaratPeserta = models.CharField(max_length=50)
class VaksinBekasi(models.Model):
    nama = models.CharField(max_length=50)
    url = models.CharField(max_length=1000)
    alamat = models.CharField(max_length=50)
    nomorTelp = models.IntegerField() # max 12 digit
    jenis = models.CharField(max_length=50)
    syaratPeserta = models.CharField(max_length=50)
