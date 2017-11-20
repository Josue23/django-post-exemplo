from django.conf.urls import include, url
from django.contrib import admin
from core.views import cadastro


urlpatterns = [
    url(r'^$', cadastro, name='home'),

    url(r'^admin/', include(admin.site.urls)),
]