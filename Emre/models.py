from django.db import models
from django.utils import timezone

class EsporModel(models.Model):
    class Meta:
        verbose_name = "Oyuncu Kimliği"
        verbose_name_plural = "Oyuncu Kimlikleri"
    isim = models.CharField(max_length=30,verbose_name = "İsim")
    nickname = models.CharField(max_length=20,verbose_name = "Kullanıcı Adı")
    mainhero = models.CharField(max_length=10,verbose_name = "Oynanan Ana Ajan", null = True)
    takim = models.CharField(max_length=30,verbose_name = "Oynanan Takım")
    giristarih = models.DateTimeField(default=timezone.now,verbose_name = "Kayıt Tarihi")
    
    def __str__(self):
        return self.isim



