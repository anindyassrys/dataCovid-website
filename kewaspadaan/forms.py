from django import forms
from .models import Waspada

class NoteForm(forms.ModelForm):
    class Meta:
        model = Waspada
        fields = ['daerah', 'tingkat_kewaspadaan']