from django.urls import path
from .views import indice, acerca, bienvenido, home, home_registrado, ProductoDetalle

urlpatterns = [
    path("", indice, name="indice"),
    path("bienvenido/", bienvenido, name="bienvenido"),
    path("acerca/", acerca, name="acerca"),
    path("home/", home, name="home"),
    path("home_registrado/", home_registrado, name="home_registrado"),
    path("producto/<int:pk>/",ProductoDetalle.as_view(), name="detalle_flan"),
]