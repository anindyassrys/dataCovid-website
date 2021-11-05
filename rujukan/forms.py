from django import forms
from .models import RumahSakit

class RSForm(forms.ModelForm):
    
    class Meta:
        model = RumahSakit
        fields = '__all__'