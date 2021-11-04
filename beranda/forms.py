from django import forms
from .models import CovidData, VaksinData

class DataCovidForm(forms.ModelForm):
    class Meta:
        model = CovidData
        fields = "__all__"

class DataVaksinForm(forms.ModelForm):
    class Meta:
        model = VaksinData
        fields = "__all__"