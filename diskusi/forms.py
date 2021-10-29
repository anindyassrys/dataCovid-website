from django import forms
from django.forms.widgets import TextInput

from diskusi.models import Discussion


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["title", "message"]

    title = forms.CharField(widget=TextInput(
        attrs={'placeholder': 'Judul Diskusi'}))

    message = forms.CharField(widget=TextInput(
        attrs={'placeholder': 'Isi diskusi...'}))
