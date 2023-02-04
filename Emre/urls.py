from django.urls import path
from . import views

urlpatterns = [
    path('',views.listele,name="Emre_listele")
]
