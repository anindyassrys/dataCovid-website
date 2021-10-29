from django import forms
from .models import DataCovid

class dataform(forms.ModelForm):
    class Meta:
        model = DataCovid
        fields = ['daerah', 'positif']