"""
URL configuration for jetbul project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ucus import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home),
    path('airport/<int:airport_id>/',views.Havalimani, name='Havalimanı Detay'),
    path('ucak/<int:ucak_id>/',views.Ucaklar, name='Ucak Detay'),
    path('takvim/<int:rota_id>/',views.Takvim,name="Uçuş Takvimi"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)