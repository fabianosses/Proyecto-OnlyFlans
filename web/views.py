from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib import messages
from .forms import ContactForm
from .models import Flan, ContactForm as ContactModel  # Se crea este modelo

# Create your views here.

def index(request):
    # Solo flanes públicos (is_private=False)
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"flanes": flanes_publicos})

def acerca(request):
    return render(request, "about.html", {})

def exito(request):
    return render(request, "exito.html", {})

def home(request):
    flanes = Flan.objects.all()
    return render(request, "home.html", {"flanes": flanes})

@login_required(login_url='/login/')  # Especifica la URL correcta
def bienvenido(request):
    # Solo flanes privados (is_private=True)
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, "welcome.html", {"flanes": flanes_privados})

class ProductoDetalle(DetailView):
    model = Flan
    template_name = "componentes/detalle_flan.html"
    context_object_name = "flan"

def contacto(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Guarda el mensaje en la base de datos
            ContactModel.objects.create(
                customer_email=form.cleaned_data["customer_email"],
                customer_name=form.cleaned_data["customer_name"],
                message=form.cleaned_data["message"]
            )

            return HttpResponseRedirect("/exito")  # Redirige a la página mensaje éxito
    else:
        form = ContactForm()

    return render(request, "users/contactus.html", {"form": form})

"""
def contacto(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        # crea una instancia de formulario y rellénala con los datos de la solicitud:
        form = ContactForm(request.POST)
        # check wether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # procesar los datos en form.cleaned_data según sea necesario
            # ...
            # redirect to a new URL:
            # redirigir a una nueva URL:
            return HttpResponseRedirect("/")
        
    # if a GET (or any other method) we'll create a blank form
    # Si es un GET (o cualquier otro método) crearemos un formulario en blanco
    else:
        form = ContactForm()

    return render(request, "contactus.html", {"form": form})
"""
