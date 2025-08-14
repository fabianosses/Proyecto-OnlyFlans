from django.contrib import admin
from .models import Flan, ContactData

# Register your models here.

@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    pass

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    pass