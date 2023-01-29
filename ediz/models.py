from django.db import models

class OrnekData(models.Model):
    class Meta:
        verbose_name_plural = "Örnek DATALAR"

    adi = models.CharField(verbose_name="ADI",max_length=50)
    soyadi = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    adres = models.TextField(null=True,blank=True)
    kayitzaman=models.DateTimeField(null=True)
    

    def __str__(self):
        return self.adi + " " + self.soyadi