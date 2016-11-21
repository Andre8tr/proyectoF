from django import forms
from .models import Liga,Equipo

class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = ('league','nombre', 'color', 'capitan', 'comment')
