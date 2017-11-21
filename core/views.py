from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect

from .models import Aluno, Professor, Course
from .forms import AlunoForm, ProfessorForm, CourseForm
from django.views import generic



def index(request):
	return render(request, 'index.html')

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
	return render(request, 'aluno_add.html', ctx)

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

	context = {'formAluno': formAluno, 'formProfessor': formProfessor, 'formCourse': formCourse}

	return render(request, 'home.html', context)

	
def aluno_list(request):
	aluno_list = Aluno.objects.all()
	ctx = {'aluno_list': aluno_list}
	return render(request, 'aluno_list.html', ctx)


def aluno_detail(request, pk):
	aluno = Aluno.objects.get(pk=pk)
	ctx = {'aluno': aluno}
	return render(request, 'aluno_detail.html', ctx)