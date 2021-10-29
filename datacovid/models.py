from django.db import models

# Create your models here.
class DataCovid(models.Model):
    daerah = models.CharField(max_length=200, default='DEFAULT VALUE')
    positif = models.CharField(max_length=200, default='DEFAULT VALUE')

    
