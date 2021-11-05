from django.db import models
from .models import Oksigen
from django import forms

class OksigenForm(forms.ModelForm):
    class Meta:
        model = Oksigen
        fields = ['url', 'alamat', 'telepon', 'domisili']
    error_messages = {
        'required': 'Please Type'
    }
    url = {
        'name' : 'url',
        'type' : 'text',
        'placeholder': 'masukkan data',
        'class': 'form-control col-sm-4'
    }
    alamat = {
        'name': 'alamat',
        'type' : 'text',
        'placeholder': 'masukkan data',
        'class': 'form-control col-sm-4'
    }
    telepon = {
        'name': 'telepon',
        'type' : 'text',
        'placeholder': 'masukkan data',
        'class': 'form-control col-sm-1'
    }

    DOMISILI_choice = {
        ('Jakarta', 'Jakarta'), ('Bogor', 'Bogor'), ('Depok', 'Depok'), ('Tangerang', 'Tangerang'), ('Bekasi', 'Bekasi')
    }
    
    url = forms.CharField(label = 'URL', required=False, max_length=80, widget=forms.TextInput(attrs=url))
    alamat = forms.CharField(label = 'Alamat', required=False, max_length=40, widget=forms.TextInput(attrs=alamat))
    telepon = forms.CharField(label = 'Telepon', required=False, max_length=15, widget=forms.TextInput(attrs=telepon))
    domisili = forms.CharField(label = 'Domisili', required=False, widget=forms.Select(choices=DOMISILI_choice))