from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class FormularioRegistro(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personalizar labels
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'
        
        # Personalizar help texts
        self.fields['username'].help_text = 'Máximo 150 caracteres. Letras, dígitos y @/./+/-/_ solamente.'
        self.fields['password1'].help_text = '''
        <ul>
            <li>Tu contraseña no puede ser muy similar a tu información personal.</li>
            <li>Tu contraseña debe contener al menos 8 caracteres.</li>
            <li>Tu contraseña no puede ser una contraseña comúnmente usada.</li>
            <li>Tu contraseña no puede ser enteramente numérica.</li>
        </ul>
        '''
        self.fields['password2'].help_text = 'Ingresa la misma contraseña que antes, para verificación.'
        
        # Personalizar placeholders
        self.fields['username'].widget.attrs.update({'placeholder': 'Tu nombre de usuario'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repite la contraseña'})

    class Meta:
        model = User
        fields = ("username", "password1", "password2")