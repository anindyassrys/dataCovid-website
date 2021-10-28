from django.db import models

class Wilayah(models.Model):
	nama = models.CharField(max_length=50)
	wid = models.CharField(max_length=10, default='null')

	def __str__(self):
		return self.wid

	class Meta:
		ordering = ["nama"]

class RumahSakit(models.Model):
	nama = models.CharField(max_length=254)
	alamat = models.CharField(max_length=254)
	telp = models.CharField(max_length=254)
	mail = models.EmailField(max_length=254)
	wilayah = models.ForeignKey(Wilayah, on_delete=models.CASCADE, related_name="daftarRS")

	def __str__(self):
		return self.nama

	class Meta:
		ordering = ["nama"]
