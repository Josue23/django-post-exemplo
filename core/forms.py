# coding=utf-8

from django.forms import ModelForm
from .models import Aluno, Professor, Course


class AlunoForm(ModelForm):
	class Meta:
		model = Aluno
		fields = '__all__'


class ProfessorForm(ModelForm):
	class Meta:
		model = Professor
		fields = '__all__'


class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = '__all__'