from django.shortcuts import render

from .models import Aluno, Professor, Course
from .forms import AlunoForm, ProfessorForm, CourseForm


def cadastro(request):
	
	# formAluno
	if request.method == 'POST':
		formAluno = AlunoForm(request.POST)
		if formAluno.is_valid():
			formAluno.save()
			# print 'success'
	else:
		formAluno = AlunoForm()

	context = {'form': formAluno}

	# formProfessor
	if request.method == 'POST':
		formProfessor = ProfessorForm(request.POST)
		if formProfessor.is_valid():
			formProfessor.save()
			# print 'success'
	else:
		formProfessor = AlunoForm()

	context = {'form': formProfessor}

	# formCourse
	if request.method == 'POST':
		formCourse = CourseForm(request.POST)
		if formCourse.is_valid():
			formCourse.save()
			# print 'success'
	else:
		formCourse = AlunoForm()

	context = {'form': formCourse}

	return render(request, 'home.html', context)


    


# def aluno_add(request):
	
# 	if request.method == 'POST':
# 		form = AlunoForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			# print 'success'
# 	else:
# 		form = AlunoForm()

# 	context = {'form': form}

# 	return render(request, 'home.html', context)
