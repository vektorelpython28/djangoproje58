from django.shortcuts import render
from .models import BlogModel

def listele(request):
    gonderiler =  BlogModel.objects.all()
    return render(request,"ediz/listele.html",{"gonderiler":gonderiler})
    
""" 
1. Templates klasöründe adına ait bir klasör oluştur
2. Klasör içerisine listele.html dosyasını kopyala
3. Kendine Ait View Yaz
4. Kendine ait path yaz (uygulamanda bulunan  urls.py) dosyası 
"""