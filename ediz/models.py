from django.db import models
from django.utils import timezone

class BlogModel(models.Model):
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    kayitzaman = models.DateTimeField(default=timezone.now)
    yayimzaman = models.DateTimeField(null=True,blank=True)

    def yayimla(self):
        self.yayimzaman = timezone.now()
        self.save()
    
    def __str__(self):
        return self.baslik

    
