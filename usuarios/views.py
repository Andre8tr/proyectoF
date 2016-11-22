from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


class RegistroUsuario(CreateView):
    model = User
    template_name = "templates/usuarios/registrar.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('ligas:post_equipos')
