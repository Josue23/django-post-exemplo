from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect

from .models import Aluno, Professor, Course
from .forms import AlunoForm, ProfessorForm, CourseForm
from django.views import generic


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
    aluno_list = Aluno.objects.all()
    ctx = {'aluno_list': aluno_list}
    return render(request, 'core/aluno_list.html', ctx)


def aluno_detail(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    ctx = {'aluno': aluno}
    return render(request, 'core/aluno_detail.html', ctx)


def aluno_edit(request, pk):
    if request.is_ajax() and request.method == 'POST':
        pk = request.POST.get('pk')
        aluno = get_object_or_404(Candidate, pk=pk)
        aluno.nome = request.POST.get('nome')
        aluno.sobrenome = request.POST.get('sobrenome')
        candidate.email = request.POST.get('email')

        aluno.save()
        response = {'status': 'update'}
        return JsonResponse(response)
    else:
        return HttpResponseRedirect(reverse('aluno_list'))


def professor_list(request):
    professor_list = Professor.objects.all()
    ctx = {'professor_list': professor_list}
    return render(request, 'core/professor_list.html', ctx)


def professor_detail(request, pk):
    professor = Professor.objects.get(pk=pk)
    ctx = {'professor': professor}
    return render(request, 'core/professor_detail.html', ctx)
