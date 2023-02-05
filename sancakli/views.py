from django.shortcuts import render

from django.shortcuts import render
from .models import HaberModel

def listele(request):
    haberler =  HaberModel.objects.all()
    return render(request,"sancakli/listele.html",{"haberler":haberler})
