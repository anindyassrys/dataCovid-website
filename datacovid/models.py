from django.db import models

# Create your models here.
class DataCovid(models.Model):
    daerah = models.CharField('daerah', max_length=200)
    positif = models.CharField('positif', max_length=200)

    
