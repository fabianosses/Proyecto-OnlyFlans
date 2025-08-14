from django.contrib import admin
from .models import Flan, ContactForm

# Register your models here.

admin.site.register(ContactForm)

@admin.register(Flan)
class ProductoAdmin(admin.ModelAdmin):
    pass