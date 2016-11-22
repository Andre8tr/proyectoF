from django.shortcuts import render
from .models import Liga,Equipo
from django.shortcuts import render, get_object_or_404
from .forms import EquipoForm, LigaForm, RegistroForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy


# Create your views here.
def post_ligas(request):
        ligas = Liga.objects.order_by('name')
        return render(request, 'ligas/post_ligas.html', {'ligas':ligas})

def post_equipos(request):
        equipos = Equipo.objects.order_by('league')
        return render(request, 'ligas/post_equipos.html', {'equipos':equipos})

def post_detail(request, pk):
        post = get_object_or_404(Liga, pk=pk)
        return render(request, 'ligas/post_detail.html', {'post': post})

def post_detailE(request, pk):
        e = get_object_or_404(Equipo, pk=pk)
        return render(request, 'ligas/post_detailE.html', {'e': e})

def nuevo_equipo(request):
        if request.method == "POST":
            form = EquipoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('ligas.views.post_detailE', pk=post.pk)
        else:
            form = EquipoForm()
        return render(request, 'ligas/equipo_edit.html', {'form': form})
def equipo_edit(request, pk):
        post = get_object_or_404(Equipo, pk=pk)
        if request.method == "POST":
            form = EquipoForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('ligas.views.post_detailE', pk=post.pk)
        else:
            form = EquipoForm(instance=post)
        return render(request, 'ligas/equipo_edit.html', {'form': form})

def nueva_liga(request):
        if request.method == "POST":
            form = LigaForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('ligas.views.post_detail', pk=post.pk)
        else:
            form = LigaForm()
        return render(request, 'ligas/liga_edit.html', {'form': form})

def liga_edit(request, pk):
        post = get_object_or_404(Liga, pk=pk)
        if request.method == "POST":
            form = LigaForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('ligas.views.post_detail', pk=post.pk)
        else:
            form = LigaForm(instance=post)
        return render(request, 'ligas/liga_edit.html', {'form': form})

#-----------------------Visas para borrar---------------------------
def eliminar_equipo(request, pk):
    post = get_object_or_404(Equipo, pk=pk)
    post.delete()
    return render(request, 'ligas/equipo_edit.html', {'form': form})


#____________------------------------Login-----------------------__
def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render(request, 'ligas/nuevousuario.html', {'formulario': formulario})

class RegistroUsuario(CreateView):
    model = User
    template_name = "ligas/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('post_equipos')
