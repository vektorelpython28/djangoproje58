from django.db import models
from django.utils import timezone

class BlogModel(models.Model):
    class Meta:
        verbose_name = 'Gönderi'
        verbose_name_plural = 'Gönderiler'
    baslik = models.CharField(verbose_name="Başlık",max_length=200)
    yazi = models.TextField(verbose_name="Yazı Gövdesi")
    kayitzaman = models.DateTimeField(verbose_name="Kayıt Zaman",default=timezone.now)
    yayimzaman = models.DateTimeField(verbose_name="Yayımlanma Zamanı",null=True,blank=True)

    def yayimla(self):
        self.yayimzaman = timezone.now()
        self.save()
    
    def __str__(self):
        return self.baslik

    
