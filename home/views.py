from django.shortcuts import render
from .models import Chambre,Catalogue,Testimonial
# Create your views here.

def index (request):
    chambres= Chambre.objects.all()
    catalogues= Catalogue.objects.all()
    testimonials = Testimonial.objects.all()
    render(request,'index.html',{'testimonial': testimonials})
    render (request,'index.html',{'catalogues': catalogues})
    return render(request,"index.html",{'chambres': chambres})
def reservation (request):
    return render(request, "reservation.html")