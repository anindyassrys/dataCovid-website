from django.db import models


class Indikator(models.Model):
    name = models.CharField(max_length=100, null=True)
    source = models.CharField(max_length=254, null=True)