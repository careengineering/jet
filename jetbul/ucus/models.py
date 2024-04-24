from django.db import models

# Create your models here.
class Airport(models.Model):
    isim = models.CharField(max_length=180) # Charfield= kısa metinsel ifade, max_lenght belirtilmeli
    sehir = models.CharField(max_length=50)
    ulke = models.CharField(max_length=80)
    kod = models.CharField(max_length=8)
    aciklama = models.TextField(null=True,blank=True) # null veritabanı için blank form için

    def __str__(self):
        return self.isim #listede object yerine isim görünmesi için


class Ucak(models.Model):
    isim = models.CharField(max_length=150)
    marka = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    yil = models.IntegerField()
    kapasite = models.IntegerField()
    hiz = models.FloatField()
    boy = models.FloatField()
    ulke = models.CharField(max_length=120)
    detay = models.TextField()
    resim = models.ImageField(upload_to="images/")

    # Ucak - Ucaks yerine kendi dilimize uyarlama
    class Meta:
        verbose_name="Jet"
        verbose_name_plural="Jetler"

    def __str__(self):
        isim = self.isim
        yil = self.yil
        return isim + " " + str(yil)



class Rota(models.Model):
    isim = models.CharField(max_length=120)
    kalkis = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="Kalkış")
    varis = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="Varış")
    ucak = models.ForeignKey(Ucak,on_delete=models.CASCADE)

    def __str__(self):
        return self.isim

    class Meta:
        verbose_name="Uçus Rotası"
        verbose_name_plural="Uçuş Rotaları"


class RotaPlan(models.Model):
    rota = models.ForeignKey(Rota,on_delete=models.CASCADE, related_name="Rota")
    tarih = models.DateField()
    ucret = models.FloatField()
    vale = models.BooleanField()
    olusturulma_tarihi=models.DateTimeField(auto_now_add=True) #otomatik tarih alır

    class Meta:
        verbose_name="Planlanmış Uçuş"
        verbose_name_plural="Planlanmış Uçuşlar"

    def __str__(self):
        return self.rota.isim+" "+str(self.tarih)



class Rezervasyon(models.Model):
    rotaplan = models.ForeignKey(RotaPlan,on_delete=models.CASCADE,related_name="RotaPlan")
    #tekrar seçilmesin unique=True eklenebilir
    ucus_saati=models.TimeField()
    isim = models.CharField(max_length=120)
    soyisim = models.CharField(max_length=120)
    tc = models.CharField(max_length=11)

    class Meta:
        verbose_name="Rezervasyon"
        verbose_name_plural="Rezervasyonlar"

    def __str__(self):
        return self.soyisim



