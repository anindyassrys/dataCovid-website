from django.db import models

# Create your models here.

class Discussion(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=2500)
    created = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=30, default="anonymous")