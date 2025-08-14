from django import forms

class  ContactForm(forms.Form):
    # contact_form_uuid No necesita ser declarado en nuestro form
    customer_email = forms.EmailField(label="Correo")
    customer_name = forms.CharField(max_length=64, label="Nombre")
    message = forms.CharField(label="Mensaje")