# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='sobrenome',
            field=models.CharField(max_length=50, verbose_name=b'Sobrenome'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='sobrenome',
            field=models.CharField(max_length=50, verbose_name=b'Sobrenome'),
        ),
    ]
