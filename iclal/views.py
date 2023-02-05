from django.shortcuts import render
from .models import BlogModel

def listele(request):
    gonderiler =  BlogModel.objects.all()
    return render(request,"iclal/listele.html",{"gonderiler":gonderiler})