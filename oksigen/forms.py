from django.db import models
from .models import Oksigen
from django import forms

class OksigenForm(forms.ModelForm):
    class Meta:
        model = Oksigen
        fields = ['url', 'alamat', 'telepon']
    error_messages = {
        'required': 'Please Type'
    }
    input_attrs = {
        'type' : 'text',
        'placeholder':'data kamu'
    }
    
    url = forms.CharField(label = 'URL', required=False, max_length=30, widget=forms.TextInput(attrs=input_attrs))
    alamat = forms.CharField(label = 'Alamat', required=False, max_length=30, widget=forms.TextInput(attrs=input_attrs))
    telepon = forms.CharField(label = 'Telepon', required=False, max_length=30, widget=forms.TextInput(attrs=input_attrs))