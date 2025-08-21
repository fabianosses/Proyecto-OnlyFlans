from django import forms
from .models import ContactData

class ContactDataForm(forms.Form):
    customer_email = forms.EmailField(label="Correo")
    customer_name = forms.CharField(max_length=64, label="Nombre")
    message = forms.CharField(label="Mensaje")

# Nuevo formulario basado en ModelForm
class ContactDataModelForm(forms.ModelForm):
    class Meta:
        model = ContactData
        fields = ["customer_name", "customer_email", "message"]
        labels = {
            "customer_name": "Nombre",
            "customer_email": "Correo",
            "message": "Mensaje"
        }

        # Opcional: puedes personalizar los widgets si es necesario
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu mensaje aquí...'}),
            'customer_name': forms.TextInput(attrs={'placeholder': 'Tu nombre completo'}),
            'customer_email': forms.EmailInput(attrs={'placeholder': 'tu.email@ejemplo.com'})
        }

