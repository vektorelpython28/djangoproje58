from django.db import models
from django.utils import timezone

class KitaplikModel(models.Model):
    isim = models.CharField(max_length=200)
    yazar = models.CharField(max_length=200)
    yayin_tarihi = models.DateField()
    tur = models.CharField(max_length=200)
    aciklama = models.TextField()
    kayit_tarihi = models.DateTimeField(default=timezone.now)
    yayin_durumu = models.BooleanField(default=False)
    
    def yayinla(self):
        self.yayin_durumu = True
        self.save()
    
    def __str__(self):
        return self.isim
