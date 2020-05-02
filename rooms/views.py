from django.shortcuts import render
from .models import Chambre
# Create your views here.
def allRooms (request):

   return render(request,"rooms.html")
