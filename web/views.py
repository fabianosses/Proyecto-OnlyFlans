from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib import messages
from .forms import ContactDataModelForm
from .models import Flan, ContactData

# Create your views here.

def index(request):
    # Solo flanes públicos (is_private=False)
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"flanes": flanes_publicos})

def acerca(request):
    return render(request, "about.html", {})

def exito(request):
    return render(request, "exito.html", {})

#def home(request):
#    flanes = Flan.objects.all()
#    return render(request, "home.html", {"flanes": flanes})

@login_required #(login_url="login")  # Especifica la URL correcta
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
        # create a form instance and populate it with data from the request:
        # crea una instancia de formulario y rellénala con los datos de la solicitud:
        # Usar ContactDataModelForm en lugar de ContactDataForm
        form = ContactDataModelForm(request.POST)
        # check wether it's valid:
        if form.is_valid():
            # Guardar directamente con el ModelForm
            form.save()  # Esto crea y guarda el objeto automáticamente
            # process the data in form.cleaned_data as required
            # procesar los datos en form.cleaned_data según sea necesario
            # ...
            #contact_form = ContactData.objects.create(**form.cleaned_data)
            # redirect to a new URL:
            # redirigir a una nueva URL:
            return HttpResponseRedirect("/exito")
        
    # if a GET (or any other method) we'll create a blank form
    # Si es un GET (o cualquier otro método) crearemos un formulario en blanco
    else:
        # se cambia ContactDataForm por ContactDataModelForm
        form = ContactDataModelForm()

    return render(request, "contactus.html", {"form": form})
