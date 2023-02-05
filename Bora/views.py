from django.shortcuts import render
from .models import MakaleModel

def listele(request):
    makaleler =  MakaleModel.objects.all()
    return render(request,"Bora/listele.html",{"Makaleler":makaleler})
