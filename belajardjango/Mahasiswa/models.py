from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    kelas = models.CharField(max_length=30, default='A')
    nrp = models.CharField(max_length=30, default='0')