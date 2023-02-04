from django.db import models
from django.utils import timezone

class MakaleModel(models.Model):
    makale_baslik = models.CharField(max_length=250)
    makale_yazi = models.TextField()
    makale_ozet = models.TextField()
    makale_kayitzaman = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.baslik
