from django.db import models

# Create your models here.
class Airport(models.Model):
    isim = models.CharField(max_length=180) # Charfield= kısa metinsel ifade, max_lenght belirtilmesi
    sehir = models.CharField(max_length=50)
    ulke = models.CharField(max_length=80)
    kod = models.CharField(max_length=8)

    def __str__(self):
        return self.isim #listede object yerine isim görünmesi için



