from django.db import models


class Indikator(models.Model):
    indikator = models.CharField('indikator', max_length=100)