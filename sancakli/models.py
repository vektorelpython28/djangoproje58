from django.db import models
from django.utils import timezone

class HaberModel(models.Model):
    class Meta:
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'
    haberbaslik = models.CharField(verbose_name = 'Haber Başlığı',max_length=250)
    haberozet = models.TextField(verbose_name = 'Haber Özeti')
    habericerik = models.TextField(verbose_name = 'Haber İçeriği')
    haberkayitzaman = models.DateTimeField(verbose_name = 'Haber Kayıt Zamanı', default=timezone.now)
    haberyayimzaman = models.DateTimeField(verbose_name = 'Haber Yayım Zamanı', null=True,blank=True)

    def yayimla(self):
        self.haberyayimzaman = timezone.now()
        self.save()
    
    def __str__(self):
        return self.haberbaslik