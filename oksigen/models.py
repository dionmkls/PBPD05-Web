from django.db import models


DOMISILI_choice = [
        ('Jakarta', 'Jakarta'), ('Bogor', 'Bogor'), ('Depok', 'Depok'), ('Tangerang', 'Tangerang'), ('Bekasi', 'Bekasi')
    ]

class Oksigen(models.Model):
    url = models.CharField(max_length=30)
    alamat = models.CharField(max_length=30)
    telepon = models.CharField(max_length=30)
    domisili = models.CharField(max_length=9, choices=DOMISILI_choice, default='green')