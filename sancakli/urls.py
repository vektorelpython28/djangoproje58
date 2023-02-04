from django.urls import path
from . import views

urlpatterns = [
    path('',views.listele,name="sancakli_listele")
]
