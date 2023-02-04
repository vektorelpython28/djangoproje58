from django.db import models
from django.utils import timezone

class KitaplikModel(models.Model):
    class Meta:
        verbose_name="Kitap"
        verbose_name_plural="Kitaplar"
    isim = models.CharField(verbose_name="Kitap İsmi",max_length=200)
    yazar = models.CharField(max_length=200)
    yayin_tarihi = models.DateField()
    tur = models.CharField(verbose_name="Kitap Turu",max_length=200)
    aciklama = models.TextField(verbose_name="Kitap ozeti")
    kayit_tarihi = models.DateTimeField(default=timezone.now)
    yayin_durumu = models.BooleanField(default=False)
    
    def yayinla(self):
        self.yayin_durumu = True
        self.save()
    
    def __str__(self):
        return self.isim
