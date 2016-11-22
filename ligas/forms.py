from django import forms
from .models import Liga,Equipo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LigaForm(forms.ModelForm):

    class Meta:
        model = Liga
        fields = ('name','pais', 'numero')

class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = ('league','nombre', 'color', 'capitan', 'comment')

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
            ]
        labels = {
                'username': 'Nombre de usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo',
        }
