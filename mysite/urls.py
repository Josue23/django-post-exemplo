from django.conf.urls import include, url
from django.contrib import admin
from core.views import cadastro, aluno_add, index


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^aluno/add$', aluno_add, name='aluno_add'),
    url(r'^add$', cadastro, name='cadastro'),
    url(r'^admin/', include(admin.site.urls)),
]