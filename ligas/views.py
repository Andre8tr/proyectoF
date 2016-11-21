from django.shortcuts import render
from .models import Liga,Equipo
from django.shortcuts import render, get_object_or_404

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
