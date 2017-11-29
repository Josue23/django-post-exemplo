# coding=utf-8
from django import forms
from django.forms import ModelForm
from .models import Aluno, Professor, Course


class AlunoForm(ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome'
            }
        ))
    sobrenome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Sobrenome'
            }
        ))
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }
        ))

    class Meta:
        model = Aluno
        fields = ('nome', 'sobrenome', 'email')
        # fields = '__all__'


class ProfessorForm(ModelForm):
	nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome'
            }
        ))
    sobrenome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Sobrenome'
            }
        ))
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }
        ))

    class Meta:
        model = Professor
        fields = ('nome', 'sobrenome', 'email')
        # fields = '__all__'


class CourseForm(ModelForm):

    class Meta:
        model = Course
        fields = '__all__'
