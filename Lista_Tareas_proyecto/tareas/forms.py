from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Formulario para crear un nuevo usuario
class RegistroFormulario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # Campos del formulario

# Formulario para iniciar sesión
class LoginFormulario(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
