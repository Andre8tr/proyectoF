from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_equipos),
        url(r'^$', views.post_ligas),

    ]
