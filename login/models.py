from django.db import models
# # from django.db.models.signals import post_save
# # from django.dispatch import receiver


# Create your models here.

# User_CHOICES = [
#     ('tenaga kesehatan', 'Tenaga Kesehatan'),
#     ('masyarakat umum', 'Masyarakat Umum'),
# ]

# class Pendaftar(models.Model):
#     first_name = models.CharField(max_length=72)
#     last_name = models.CharField(max_length=72)
#     username = models.CharField(max_length=32)
#     email = models.EmailField(max_length=200, default="")
#     password1 = models.CharField(max_length=100)
#     password2 = models.CharField(max_length=100)
#     user_role = models.CharField(max_length=32, default="")

# # @receiver(post_save)
# # def create_user_profile(instance, created, **kwargs):
# #     if created:
# #         Pendaftar.objects.create(username=instance)


# # @receiver(post_save)
# # def save_user_profile(instance, **kwargs):
# #     instance.pendafrar.save()