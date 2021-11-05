from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# User_CHOICES = [
#     ('tenaga kesehatan', 'Tenaga Kesehatan'),
#     ('masyarakat umum', 'Masyarakat Umum'),
# ]

class createUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
		# User_CHOICES = forms.CharField(label = "Tipe pengguna", widget = forms.RadioSelect(choices=User_CHOICES))