from django.contrib import admin
from .models import ContactData

# Register your models here.

@admin.register(ContactData)
class ContactoAdmin(admin.ModelAdmin):
    pass