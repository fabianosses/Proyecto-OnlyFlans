from django.urls import path
from .views import Login, Registro, Logout
from web.views import contacto  # Importa la vista de contacto desde web

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("registro/", Registro.as_view(), name="registro"),
    path("logout/", Logout.as_view(), name="logout"),
    path("contacto/", contacto, name="contacto"),  # Usa la vista basada en función
]