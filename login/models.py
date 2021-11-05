from django.db import models


# Create your models here.
class Pendaftar(models.Model):
    first_name = models.CharField(max_length=72)
    last_name = models.CharField(max_length=72)
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=200)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    user_role = models.CharField(max_length=32)
