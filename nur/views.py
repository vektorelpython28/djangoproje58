from django.shortcuts import render
from .models import ToDoList
# Create your views here.
def listele(request):
    Yapilacaklar = ToDoList.objects.all()
    return render(request,"nur/listele.html",{"Yapilacaklar":Yapilacaklar})
