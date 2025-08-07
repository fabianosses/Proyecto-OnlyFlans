from django.urls import path
from .views import home, home_registrado, ProductoDetalle

urlpatterns = [
    path("", home, name="home"),
    path("home_registrado/", home_registrado, name="home_registrado"),
    path("producto/<int:pk>/",ProductoDetalle.as_view(), name="detalle_flan"),
]