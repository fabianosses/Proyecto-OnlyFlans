from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from .forms import FormularioRegistro
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

# Create your views here.
class Registro(SuccessMessageMixin, CreateView):
    form_class = FormularioRegistro
    template_name = "users/registro.html"
    success_url = reverse_lazy("login")
    success_message = "Registro exitoso :)"

class Login(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("welcome")

class Logout(LogoutView):
    next_page = reverse_lazy("index")
    
    def post(self, request, *args, **kwargs):
        messages.success(request, "Sesión cerrada con éxito")
        return super().post(request, *args, **kwargs)

