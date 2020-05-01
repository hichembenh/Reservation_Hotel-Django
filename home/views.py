from django.shortcuts import render
from .models import Chambre,Catalogue
# Create your views here.

def index (request):
    chambres= Chambre.objects.all()
    catalogues= Catalogue.objects.all()
    render (request,'index.html',{'catalogues': catalogues})
    return render(request,"index.html",{'chambres': chambres})