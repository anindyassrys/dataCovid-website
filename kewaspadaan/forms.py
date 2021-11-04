from django import forms
from .models import Indikator


class SaranForm(forms.ModelForm):
    class Meta:
        model = Indikator
        fields = ['indikator']