import uuid
from django.db import models
from django.forms import ModelForm

class Flan(models.Model):
    flan_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField("Nombre del flan", max_length=64)
    description = models.TextField("Descripción")
    image_url = models.URLField("URL de la imagen", max_length=200, blank=True, null=True)
    slug = models.SlugField("Slug", max_length=64, unique=True, blank=True, null=True)
    is_private = models.BooleanField("¿Es privado?", default=False)
    precio = models.DecimalField("Precio", max_digits=5, decimal_places=0)
    stock = models.PositiveIntegerField("Stock", default=0)
    imagen = models.ImageField("Imagen", upload_to="productos/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Flan"
        verbose_name_plural = "Flanes"

class ContactData(models.Model):
    contact_form_uuid = models.UUIDField (default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField("Nombre del cliente", max_length=64)
    message = models.TextField()

    def __str__(self):
        return f"Mensaje de {self.customer_name} ({self.customer_email})"

# Crear un modelo basado en ModelForm que permita reemplazar nuestro ContactDataForm, lo podemos llamar ContactDataModelForm.
class ContactDataModelForm(ModelForm):
    class Meta:
        model = ContactData
        fields = ["customer_name", "customer_email", "message"]