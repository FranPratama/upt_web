from django.db import models

# Create your models here.
class jurusan(models.Model):
    prodi = models.CharField(max_length=50)

    def __str__(self):
        return self.prodi
    
class status(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status

class ktm(models.Model):
    nim = models.CharField(max_length=15)
    nama = models.CharField(max_length=100)
    jurusan = models.ForeignKey(jurusan, on_delete=models.CASCADE)
    tempat_lahir = models.CharField(max_length=50)
    tgl_lahir = models.DateField()
    alamat = models.CharField(max_length=200)
    kec = models.CharField(max_length=50)
    kota = models.CharField(max_length=50)
    status = models.ForeignKey(status, on_delete=models.CASCADE)
    no_foto = models.CharField(max_length=13)
    no_telp = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='uploads/')
    tgl_daftar = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nim, self.nama