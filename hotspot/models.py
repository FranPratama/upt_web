from django.db import models

# Create your models here.
class hotspot(models.Model):
    email = models.CharField(max_length=15)
    no_telp = models.CharField(max_length=15)
    nama = models.CharField(max_length=100)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username, self.password