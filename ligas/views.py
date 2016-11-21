from django.shortcuts import render
from .models import Liga,Equipo
from django.shortcuts import render, get_object_or_404
from .forms import EquipoForm
from django.shortcuts import redirect


# Create your views here.
def post_ligas(request):
        ligas = Liga.objects.order_by('name')
        return render(request, 'ligas/post_ligas.html', {'ligas':ligas})

def post_equipos(request):
        equipos = Equipo.objects.order_by('nombre')
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
