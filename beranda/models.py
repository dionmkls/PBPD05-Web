from django.db import models

class CovidData(models.Model):
    bulan = models.CharField(max_length=9, default='')
    tahun = models.CharField(max_length=4, default='2021')
    penambahanKasusPositif = models.CharField(max_length=9)
    PositifKumulatif = models.CharField(max_length=9)