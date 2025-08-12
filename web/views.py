from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto
from django.views.generic import DetailView

# Create your views here.
def indice(request):
    return render(request, "index.html", {})

def acerca(request):
    return render(request, "about.html", {})

def bienvenido(request):
    return render(request, "welcome.html", {})

def home(request):
    flanes = Producto.objects.all()
    return render(request, "home.html", {"flanes": flanes})

@login_required
def home_registrado(request):
    return render(request, "registro.html", {})

class ProductoDetalle(DetailView):
    model = Producto
    template_name = "componentes/detalle_flan.html"
    context_object_name = "flan"