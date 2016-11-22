from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login
urlpatterns = [
    # Examples:
    # url(r'^$', 'mysiste.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ligas.urls')),
    url(r'', include('usuarios.urls')),
    url(r'^$', login, {'template_name:index.html'}, name="login")

]
