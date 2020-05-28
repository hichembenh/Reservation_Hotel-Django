from django.urls import path
from . import views

urlpatterns = [
    path("allRooms",views.allRooms, name= 'allRooms')
]
