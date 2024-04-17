from django.contrib import admin

# Register your models here.

from.models import Airport,Ucak,Rota,RotaPlan,Rezervasyon

class AirportAdmin(admin.ModelAdmin):
    list_display = ("isim","ulke","sehir","kod")
    search_fields = ("ulke","sehir")
    list_filter = ("ulke", "sehir")

class UcakAdmin(admin.ModelAdmin):
    list_display = ("isim","ulke","kapasite","model","marka")
    search_fields = ("isim", "marka", "model", "ulke")

class RotaPlanAdmin(admin.ModelAdmin):
    list_display = ("rota","tarih","ucret")
    search_fields = ("rota","tarih","ucret")

class RezervasyonAdmin(admin.ModelAdmin):
    list_display = ("rotaplan","ucus_saati","isim","soyisim")
    search_fields = ("rotaplan" , "isim","soyisim")

admin.site.register(Airport,AirportAdmin)
admin.site.register(Ucak,UcakAdmin)
admin.site.register(Rota)
admin.site.register(RotaPlan,RotaPlanAdmin)
admin.site.register(Rezervasyon,RezervasyonAdmin)