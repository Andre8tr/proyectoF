from django import forms
from .models import Liga,Equipo

class LigaForm(forms.ModelForm):

    class Meta:
        model = Liga
        fields = ('name','pais', 'numero')
        
class EquipoForm(forms.ModelForm):

    class Meta:
        model = Equipo
        fields = ('league','nombre', 'color', 'capitan', 'comment')
