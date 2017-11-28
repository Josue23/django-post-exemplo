from django.conf.urls import include, url
from django.contrib import admin
from core import views as v
from django.core.urlresolvers import reverse


urlpatterns = [
    url(r'^$', v.index, name='index'),

    # aluno
    url(r'^aluno/add/$', v.aluno_add, name='aluno_add'),
    url(r'^aluno_list/$', v.aluno_list, name='aluno_list'),
    url(r'^aluno/(?P<pk>\d+)/$', v.aluno_detail, name='aluno_detail'),
    url(r'^aluno/(?P<pk>\d+)/edit/$', v.aluno_edit, name='aluno_edit'),
    url(r'^aluno/(?P<pk>\d+)/update/$', v.aluno_update, name='aluno_update'),
    url(r'^aluno/(?P<pk>\d+)/delete/$', v.aluno_delete, name='aluno_delete'),
    url(r'^aluno/(?P<pk>\d+)/delete/confirm/$',
        v.aluno_delete_confirm, name='aluno_delete_confirm'),

    # professor
    url(r'^professor/add/$', v.professor_add, name='professor_add'),
    url(r'^professor_list/$', v.professor_list, name='professor_list'),
    url(r'^professor/(?P<pk>\d+)/$', v.professor_detail, name='professor_detail'),
    url(r'^professor/(?P<pk>\d+)/delete/$',
        v.professor_delete, name='professor_delete'),
    url(r'^professor/(?P<pk>\d+)/delete/confirm/$',
        v.professor_delete_confirm, name='professor_delete_confirm'),

    # cadastro com 3 forms
    url(r'^add/$', v.cadastro, name='cadastro'),

    # admin
    url(r'^admin/', include(admin.site.urls)),


]
