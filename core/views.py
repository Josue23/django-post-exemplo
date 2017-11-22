from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from .models import Aluno, Professor, Course
from .forms import AlunoForm, ProfessorForm, CourseForm
from django.views import generic
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'POST':

        formAluno = AlunoForm(request.POST)
        if 'enviarAluno' in request.POST and formAluno.is_valid():
            formAluno.save()
            # print 'success'

        formProfessor = ProfessorForm(request.POST)
        if 'enviarProfessor' in request.POST and formProfessor.is_valid():
            formProfessor.save()

        formCourse = CourseForm(request.POST)
        if 'enviarCourse' in request.POST and formCourse.is_valid():
            formCourse.save()

    else:
        formAluno = AlunoForm()
        formProfessor = ProfessorForm()
        formCourse = CourseForm()

    context = {'formAluno': formAluno,
               'formProfessor': formProfessor, 'formCourse': formCourse}

    return render(request, 'home.html', context)


def aluno_add(request):
    if request.method == 'POST':
        alunoform = AlunoForm(request.POST)
        if alunoform.is_valid:
            alunoform.save()
            # import ipdb; ipdb.set_trace()
        return redirect('aluno_list')
    else:
        alunoform = AlunoForm()
    ctx = {'aluno_form': alunoform}
    return render(request, 'core/aluno_add.html', ctx)


def aluno_list(request):
    # pega todos os objetos do model Aluno
    aluno_list = Aluno.objects.all()
    # pega a busca do input com name="q" no aluno_list.html
    query = request.GET.get('q')
    if query:
        # query_list = query.split()

        # filtra pelo campo nome OU campo sobrenome OU campo email
        aluno_list = aluno_list.filter(
            Q(nome__icontains=query) |
            Q(sobrenome__icontains=query) |
            Q(email__icontains=query)
        )
    ctx = {'aluno_list': aluno_list}
    return render(request, 'core/aluno_list.html', ctx)


def aluno_detail(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    ctx = {'aluno': aluno}
    return render(request, 'core/aluno_detail.html', ctx)


def aluno_edit(request, pk):
    if request.is_ajax() and request.method == 'POST':
        pk = request.POST.get('pk')
        aluno = get_object_or_404(Aluno, pk=pk)
        aluno.nome = request.POST.get('nome')
        aluno.sobrenome = request.POST.get('sobrenome')
        candidate.email = request.POST.get('email')

        aluno.save()
        response = {'status': 'update'}
        return JsonResponse(response)
    else:
        return HttpResponseRedirect(reverse('aluno_list'))


def professor_add(request):
    if request.method == 'POST':
        professorform = ProfessorForm(request.POST)
        if professorform.is_valid:
            professorform.save()
            # import ipdb; ipdb.set_trace()
        return redirect('professor_list')
    else:
        professorform = ProfessorForm()
    ctx = {'professor_form': professorform}
    return render(request, 'core/professor_add.html', ctx)


def professor_list(request):
    # pega todos os objetos do model Professor
    professor_list = Professor.objects.all()
    # pega a busca do input com name="q" no professor_list.html
    query = request.GET.get('q')
    if query:
        # query_list = query.split()

        # filtra pelo campo nome OU campo sobrenome OU campo email
        professor_list = professor_list.filter(
            Q(nome__icontains=query) |
            Q(sobrenome__icontains=query) |
            Q(email__icontains=query)
        )
    ctx = {'professor_list': professor_list}
    return render(request, 'core/professor_list.html', ctx)


def professor_detail(request, pk):
    professor = Professor.objects.get(pk=pk)
    ctx = {'professor': professor}
    return render(request, 'core/professor_detail.html', ctx)


def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    ctx = {'aluno': aluno}
    return render(request, 'core/aluno_delete.html', ctx)


def aluno_delete_confirm(request, pk):
    if request.method == 'POST':
        aluno = Aluno.objects.get(pk=pk)
        aluno.delete()
        return HttpResponseRedirect(reverse_lazy('aluno_list'))
