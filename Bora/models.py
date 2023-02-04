from django.db import models
from django.utils import timezone

class MakaleModel(models.Model):
    class Meta:
        verbose_name = 'Makale'
        verbose_name_plural = 'Makaleler'
    makale_baslik = models.CharField(verbose_name = 'Başlık',max_length=250)
    makale_konu = models.CharField(verbose_name = 'Konu',max_length=100)
    makale_yazi = models.TextField(verbose_name = 'Makale İçeriği')
    makale_yayimzaman = models.DateTimeField(verbose_name = 'Yayım Tarihi',null = True, blank = True)
    
    def yayimzamani(self):
        self.makale_yayimzaman = timezone.now()
        self.save()

    def kelime_sayma(self):
        satir=self.makale_yazi.splitlines()
        sayi = 0
        for i in satir:
            kelimeler=i.split()
            for k in kelimeler:
                sayi += 1
        return sayi    

    def __str__(self):
        return self.makale_baslik
