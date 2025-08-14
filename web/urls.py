from django.urls import path
from .views import index, acerca, bienvenido, home, exito, ProductoDetalle

urlpatterns = [
    path("", index, name="index"),
    path("welcome/", bienvenido, name="welcome"),
    path("about/", acerca, name="about"),
    path("home/", home, name="home"),
    path("exito/", exito, name="exito"),
    path('flan/<uuid:pk>/', ProductoDetalle.as_view(), name='detalle_flan'),
]