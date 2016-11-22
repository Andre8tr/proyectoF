from django.conf.urls import include, url
from . import views

urlpatterns = [
        #url(r'^usuario/nuevo/$', views.nuevo_usuario, name='nuevo_user'),
        #url(r'^usuario/nuevo', views.RegistroUsuario, name="registrar"),
        url(r'^usuario/nuevo/$', views.RegistroUsuario.as_view(), name='nuevo_user'),
        url(r'^$', views.post_equipos),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detailE),
        url(r'^post/(?P<pk>[0-9]+)/eliminar/$', views.eliminar_equipo),
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.equipo_edit, name='equipo_edit'),
        url(r'^equipo/nuevo/$', views.nuevo_equipo, name='nuevo_equipo'),

        url(r'^$', views.post_ligas),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
        url(r'^post/(?P<pk>[0-9]+)/editL/$', views.liga_edit, name='liga_edit'),
        url(r'^liga/nueva/$', views.nueva_liga, name='nueva_liga'),
        ]
