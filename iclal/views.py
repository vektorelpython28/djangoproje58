from django.shortcuts import render
from .models import BlogModel

def listele(request):
    gonderiler =  BlogModel.objects.all()
    return render(request,"Iclal/listele.html",{"gonderiler":gonderiler})