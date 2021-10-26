from django import forms
from .models import APD

class APDForm(forms.ModelForm):
    class Meta:
        model = APD
        fields = ('jenis', 'lokasi', 'jumlah', 'harga',)