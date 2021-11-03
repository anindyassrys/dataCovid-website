from django import forms
from django.forms.widgets import TextInput, Textarea

from diskusi.models import Discussion


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["title", "message"]
        exclude = ("user",)

    title = forms.CharField(label="Judul", widget=TextInput(
        attrs={'placeholder': 'Topik diskusi'}))

    message = forms.CharField(label="Pesan", widget=Textarea(
        attrs={'placeholder': 'Tuliskan pesanmu'}))
