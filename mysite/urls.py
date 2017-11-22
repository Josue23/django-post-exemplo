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
    # url(r'^candidate/(?P<pk>\d+)/edit/$', v.candidate_edit, name='candidate_edit'),
    
    # professor
    url(r'^professor_list/$', v.professor_list, name='professor_list'),
    url(r'^professor/(?P<pk>\d+)/$', v.professor_detail, name='professor_detail'),

    # cadastro com 3 forms
    url(r'^add/$', v.cadastro, name='cadastro'),
    
    # admin
    url(r'^admin/', include(admin.site.urls)),
]