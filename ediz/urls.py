from django.urls import path
from . import views

urlpatterns = [
    path('',views.listele,name="ediz_listele"),
    
]
