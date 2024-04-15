from django.contrib import admin

# Register your models here.

from.models import Airport

class AirportAdmin(admin.ModelAdmin):
    list_display = ("isim","ulke","sehir","kod")
    search_fields = ("ulke","sehir")
    list_filter = ("ulke", "sehir")

admin.site.register(Airport,AirportAdmin)