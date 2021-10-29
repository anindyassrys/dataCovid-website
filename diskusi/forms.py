from django import forms
from django.forms.widgets import TextInput

from diskusi.models import Discussion


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["title", "message"]

    title = forms.CharField(widget=TextInput(
        attrs={'placeholder': 'Nama Baru'}))

    message = forms.CharField(widget=TextInput(
        attrs={'placeholder': 'ex: 2006597241'}))
