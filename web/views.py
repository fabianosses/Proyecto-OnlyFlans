from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html", {})

@login_required
def home_registrado(request):
    return render(request, "registrado.html", {})