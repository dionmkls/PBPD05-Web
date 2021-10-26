from django.db import models

# Create your models here.

class APD(models.Model):
    jenis = models.CharField(max_length = 30)
    lokasi = models.CharField(max_length = 100)
    jumlah = models.IntegerField(default=0)
    harga = models.IntegerField(default=0)

    def __str__(self):
        return self.jenis + "-" + self.lokasi