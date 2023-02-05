from django.shortcuts import render
from .models import EsporModel

def listele(request):
    Kimlikler =  EsporModel.objects.all()
    return render(request,"Emre/listele.html",{"Oyuncular":Kimlikler})
