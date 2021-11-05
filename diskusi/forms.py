from django import forms
from django.forms.widgets import TextInput, Textarea

from diskusi.models import Discussion


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        exclude = ("user",)
