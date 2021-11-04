from django.db import models

# Create your models here.
LOKASI_CHOICES = (
    ('JK', 'Jakarta'),
    ('BO', 'Bogor'),
    ('DE', 'Depok'),
    ('TA', 'Tangerang'),
    ('BEK', 'Bekasi'),
    ('L', 'Luar Jabodetabek')
)

TERSEDIA = (
    ('I', 'ICU'),
    ('K', 'Kamar'),
    ('IK', 'ICU dan Kamar'),
)

class RumahSakit(models.Model):
    nama = models.CharField(max_length=100)
    lokasi = models.CharField(max_length=3, choices=LOKASI_CHOICES, default='L')
    alamat = models.CharField(max_length=100)
    url_gmaps = models.CharField(max_length=100)
    no_telp = models.CharField(max_length=15)
    tersedia = models.CharField(max_length=2, choices=TERSEDIA, default='IK')

    def __str__(self):
        return "{}.{}".format(self.id, self.nama)