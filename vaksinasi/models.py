from django.db import models

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=50)
    telah_vaksin_dosis_1 = models.IntegerField()
    telah_vaksin_dosis_2 = models.IntegerField()
    target_vaksin = models.IntegerField()
    per_tanggal = models.DateField()
