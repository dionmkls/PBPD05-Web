from django import forms
from django.db.models import fields

from .models import RumahSakit

class RumahSakitForm(forms.ModelForm):
    class Meta:
        model = RumahSakit
        fields = [
            'lokasi',
            'nama',
            'alamat',
            'url_gmaps' , 
            'no_telp',
            'tersedia',
        ]

        widgets = {
            'lokasi': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),

            'nama': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'isi nama rumah sakit',
                }
            ),

            'alamat': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'isi alamat rumah sakit',
                }
            ),

            'url_gmaps': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'isi link google maps rumah sakit',
                }
            ),

            'no_telp': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'isi nomor telephone rumah sakit',
                }
            ),

            'tersedia': forms.Select(
                attrs = {
                    'class': 'form-control',
                }
            ),
        }
