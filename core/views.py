from django.shortcuts import render

from .models import Aluno, Professor, Course
from .forms import AlunoForm, ProfessorForm, CourseForm

def home(request):
	return render(request, 'index.html')

def aluno_add(request):
	if request.method == 'POST':
		alunoform = AlunoForm(request.POST)
		if alunoform.is_valid:
			alunoform.save()
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