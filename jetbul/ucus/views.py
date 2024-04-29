from django.shortcuts import render, get_object_or_404
from .models import Airport,Rota,Ucak,RotaPlan

# Create your views here.
def home(request):
    airports = Airport.objects.all()
    rotalar = Rota.objects.all()
    # Airport.objects.filter(sehir ="Ankara) ankaradaki havalimanlarını filtreler
    return render(request,'index.html',context={'airports':airports,'rotalar':rotalar})

def Havalimani(request, airport_id):
    airport = get_object_or_404(Airport, pk=airport_id)
    return render(request,'airport.html',context={'airport':airport})


def Ucaklar(request, ucak_id):
    ucak = get_object_or_404(Ucak, pk=ucak_id)
    return render(request,'ucak.html',context={'ucak':ucak})

def Takvim(request, rota_id):
    rota = get_object_or_404(Rota, pk=rota_id)
    planlar = RotaPlan.objects.filter(rota=rota)
    return render(request,'takvim.html',context={'planlar':planlar,'rota':rota})

