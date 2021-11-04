from django.db import models

class CovidData(models.Model):
    bulan = models.CharField(max_length=9, default='')
    tahun = models.CharField(max_length=4, default='2021')
    penambahanKasusPositif = models.CharField(max_length=9)
    PositifKumulatif = models.CharField(max_length=9)

class VaksinData(models.Model):
    bulan = models.CharField(max_length=9, default='')
    tahun = models.CharField(max_length=4, default='2021')
    vaksin_1_kali = models.CharField(max_length=9)
    vaksin_2_kali = models.CharField(max_length=9)
    belum_vaksin =  models.CharField(max_length=9)