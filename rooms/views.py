from django.shortcuts import render
from .models import Chambre
# Create your views here.
def allRooms (request):
    chambre3= Chambre()
    chambre3.nom= 'aal bhar'
    chambre3.description= 'mandher mezyen wallah'
    chambre3.image = 'img_1.jpg'
    chambre3.prix= 100

    chambre2= Chambre()
    chambre2.nom= 'aal jbal'
    chambre2.description= 'mch khayba'
    chambre2.image='img_2.jpg'
    chambre2.prix= 200

    chambres = [chambre3,chambre2]

    return render(request,"rooms.html",{'chambres': chambres})
