from django.urls import path
from .views import home, home_registrado

urlpatterns = [
    path("", home, name="home"),
    path("home_registrado/", home_registrado, name="home_registrado")
]