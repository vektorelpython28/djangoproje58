from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class ToDoList(models.Model):
    baslik = models.CharField(max_length=144,verbose_name="Başlık")
    aciklama = models.TextField(blank=True,null=True,verbose_name="Açıklama")
    eklenme_tarihi = models.DateTimeField(default=timezone.now,verbose_name="Eklenme Tarihi")
    durum = models.BooleanField(default=False, verbose_name="Yapıldı")

    def __str__(self):
        return self.baslik