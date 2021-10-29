from django import forms
from .models import VaksinJakarta, VaksinBogor, VaksinDepok, VaksinTangerang, VaksinBekasi
from django.db.models import fields

class FormJakarta(forms.ModelForm):
    class Meta:
        model = VaksinJakarta
        fields = [
            'nama', 'url', 'alamat', 'nomorTelp', 
            'jenis', 'syaratPeserta'
            ]
class FormBogor(forms.ModelForm):
    class Meta:
        model = VaksinBogor
        fields = [
            'nama', 'url', 'alamat', 'nomorTelp', 
            'jenis', 'syaratPeserta'
            ]
class FormDepok(forms.ModelForm):
    class Meta:
        model = VaksinDepok
        fields = [
            'nama', 'url', 'alamat', 'nomorTelp', 
            'jenis', 'syaratPeserta'
            ]
class FormTangerang(forms.ModelForm):
    class Meta:
        model = VaksinTangerang
        fields = [
            'nama', 'url', 'alamat', 'nomorTelp', 
            'jenis', 'syaratPeserta'
            ]
class FormBekasi(forms.ModelForm):
    class Meta:
        model = VaksinBekasi
        fields = [
            'nama', 'url', 'alamat', 'nomorTelp', 
            'jenis', 'syaratPeserta'
            ]
            