from django.db import models
from django.utils import timezone

class HaberModel(models.Model):
    haberbaslik = models.CharField(max_length=250)
    haberozet = models.TextField()
    habericerik = models.TextField()
    haberkayitzaman = models.DateTimeField(default=timezone.now)
    haberyayimzaman = models.DateTimeField(null=True,blank=True)

    def yayimla(self):
        self.haberyayimzaman = timezone.now()
        self.save()
    
    def __str__(self):
        return self.haberbaslik