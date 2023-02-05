from django.shortcuts import render
from .models import ToDoListModel
# Create your views here.
def listele(request):
    Yapilacaklar = ToDoListModel.objects.all()
    return render(request,"nur/listele.html",{"Yapilacaklar":Yapilacaklar})
