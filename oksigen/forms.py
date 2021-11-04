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
    input_attrs = {
        'type' : 'text',
        'placeholder': 'masukkan data',
        'class': 'form-control col-sm-5'
    }
    telepon = {
        'type' : 'text',
        'placeholder': 'masukkan data',
        'class': 'form-control col-sm-1'
    }
    DOMISILI_choice = {
        ('Jakarta', 'Jakarta'), ('Bogor', 'Bogor'), ('Depok', 'Depok'), ('Tangerang', 'Tangerang'), ('Bekasi', 'Bekasi')
    }
    
    url = forms.CharField(label = 'URL', required=False, max_length=70, widget=forms.TextInput(attrs=input_attrs))
    alamat = forms.CharField(label = 'Alamat', required=False, max_length=70, widget=forms.TextInput(attrs=input_attrs))
    telepon = forms.CharField(label = 'Telepon', required=False, max_length=15, widget=forms.TextInput(attrs=telepon))
    domisili = forms.CharField(label = 'Domisili', required=False, widget=forms.Select(choices=DOMISILI_choice))