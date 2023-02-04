from django.db import models
from django.utils import timezone

class ZINKModel(models.Model):
    isim = models.CharField(max_length=200)
    nickname = models.CharField(max_length=20)
    
    text = models.TextField()
    kayitzaman = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.baslik



