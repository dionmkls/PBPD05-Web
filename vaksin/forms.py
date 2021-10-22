from django import forms
from .models import Vaksin
from django.db.models import fields

class VaksinForm(forms.ModelForm):
    class Meta:
        model = Vaksin
        # fields = '__all__'
        fields = [
            'nama', 'url', 'alamat', 'nomorTelp', 
            'jenis', 'syaratPeserta'
            ]