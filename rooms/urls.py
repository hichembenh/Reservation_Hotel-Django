from django.urls import path
from . import views

urlpatterns = [
    path("",views.allRooms, name= 'allRooms')
]
