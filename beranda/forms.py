from django import forms
from .models import CovidData

class DataCovidForm(forms.ModelForm):
    class Meta:
        model = CovidData
        fields = "__all__"
