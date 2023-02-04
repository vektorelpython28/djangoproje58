from django.db import models
from django.utils import timezone

class MakaleModel(models.Model):
    makale_baslik = models.CharField(max_length=250)
    makale_konu = models.CharField(max_length=100)
    makale_yazi = models.TextField()
    makale_yayimzaman = models.DateTimeField(null = True, blank = True)
    
    def yayimzamani(self):
        self.makale_yayimzaman = timezone.now()
        self.save()
        

    def __str__(self):
        return self.baslik
