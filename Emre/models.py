from django.db import models
from django.utils import timezone

class ZINKModel(models.Model):
    isim = models.CharField(max_length=200,verbose_name = "İsim")
    nickname = models.CharField(max_length=20,verbose_name = "Kullanıcı Adı")
    mainhero = models.CharField(max_length=10,verbose_name = "İsim")
    giristarih = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.baslik



