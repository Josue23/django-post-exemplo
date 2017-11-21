from django.conf.urls import include, url
from django.contrib import admin
from core.views import cadastro, aluno_add, index, aluno_list


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^aluno/add$', aluno_add, name='aluno_add'),
    url(r'^aluno_list$', aluno_list, name='aluno_list'),
    url(r'^add$', cadastro, name='cadastro'),
    url(r'^admin/', include(admin.site.urls)),
]