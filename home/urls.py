from django.urls import path
from .views import index,reservation
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',index, name= 'index'),
    path ("Reservation",reservation,name= 'reservation'),
]
urlpatterns += staticfiles_urlpatterns()