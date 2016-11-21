from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^equipo/nuevo/$', views.nuevo_equipo, name='nuevo_equipo'),
        url(r'^$', views.post_equipos),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detailE),
        url(r'^$', views.post_ligas),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),






    ]
