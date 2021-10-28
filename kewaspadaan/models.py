from django.db import models

# Create your models here.
class Waspada(models.Model):
    daerah = models.TextField()
    tingat_kewaspadaan = models.TextField()
