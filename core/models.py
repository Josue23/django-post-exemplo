# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Aluno(models.Model):
	nome = models.CharField('Nome', max_length=20)
	sobrenome = models.CharField('Sobrenome', max_length=50)
	email = models.EmailField(max_length=60)

	def __unicode__(self):
		return self.nome


class Professor(models.Model):
	nome = models.CharField('Nome', max_length=20)
	sobrenome = models.CharField('Sobrenome', max_length=50)
	email = models.EmailField(max_length=60,blank=True)

	def __unicode__(self):
		return self.nome

class Course(models.Model):

	nome = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Slug')
	description = models.TextField('Descrição', blank=True)
	def __unicode__(self):
		return self.nome