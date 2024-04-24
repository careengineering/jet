from django.shortcuts import render, get_object_or_404
from .models import Airport,Rota

# Create your views here.
def home(request):
    airports = Airport.objects.all()
    rotalar = Rota.objects.all()
    # Airport.objects.filter(sehir ="Ankara) ankaradaki havalimanlarını filtreler
    return render(request,'index.html',context={'airports':airports,'rotalar':rotalar})

def Havalimani(request, airport_id):
    airport = get_object_or_404(Airport, pk=airport_id)
    return render(request,'airport.html',context={'airport':airport})
