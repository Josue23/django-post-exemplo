# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=20, verbose_name=b'Nome')),
                ('sobrenome', models.DateTimeField(max_length=50, verbose_name=b'Sobrenome')),
                ('email', models.EmailField(max_length=60, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('slug', models.SlugField(verbose_name=b'Slug')),
                ('description', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=20, verbose_name=b'Nome')),
                ('sobrenome', models.DateTimeField(max_length=50, verbose_name=b'Sobrenome')),
                ('email', models.EmailField(max_length=60, blank=True)),
            ],
        ),
    ]
