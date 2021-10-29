from django.db import models

# Create your models here.

class Discussion(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
