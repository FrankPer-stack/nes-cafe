from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        help_text='Requerido. 150 caracteres o menos. Letras, números y @/./+/-/_ solamente.',
        error_messages={
            'unique': 'Este nombre de usuario ya está en uso.',
            'invalid': 'Ingrese un nombre de usuario válido.',
        }
    )
    
    email = forms.EmailField(
        label='Correo electrónico',
        required=True,
        error_messages={
            'invalid': 'Por favor ingrese un correo electrónico válido.',
            'unique': 'Este correo electrónico ya está registrado.',
        }
    )
    
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        help_text='Tu contraseña debe tener al menos 8 caracteres y no puede ser demasiado común.',
        error_messages={
            'password_too_short': 'La contraseña debe tener al menos 8 caracteres.',
            'password_too_common': 'Esta contraseña es demasiado común.',
            'password_entirely_numeric': 'La contraseña no puede ser completamente numérica.',
        }
    )
    
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
        help_text='Ingrese la misma contraseña que antes, para verificación.',
        error_messages={
            'password_mismatch': 'Las contraseñas no coinciden.',
        }
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        try:
            validate_password(password1, self.instance)
        except ValidationError as error:
            # Personalizar mensajes de error de contraseña
            custom_messages = {
                'password_too_short': 'La contraseña debe tener al menos 8 caracteres.',
                'password_too_common': 'Por favor usa una contraseña más segura. Esta contraseña es demasiado común.',
                'password_entirely_numeric': 'La contraseña no puede ser completamente numérica.',
                'password_too_similar': 'La contraseña es muy similar a tu información personal.'
            }
            
            # Reemplazar mensajes de error con versiones personalizadas
            errors = []
            for error in error.messages:
                for key, message in custom_messages.items():
                    if key in error:
                        errors.append(message)
                        break
                else:
                    errors.append(error)
            
            raise ValidationError(errors)
        
        return password1

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario o correo')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
    error_messages = {
        'invalid_login': 'Por favor ingrese un nombre de usuario y contraseña correctos.',
        'inactive': 'Esta cuenta está inactiva.'
    }

    class Meta:
        model = CustomUser
        fields = ('username', 'password')
