# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=60)),
                ('turma', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id_disciplina', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=45)),
                ('periodo', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id_professor', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=60)),
                ('matricula', models.CharField(max_length=15)),
                ('email', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id_prova', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('data_prova', models.DateField()),
                ('data_limite', models.DateField()),
                ('estagio', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id_status', models.AutoField(serialize=False, auto_created=True, primary_key=True)),
                ('devolucao', models.BooleanField(default=False)),
                ('data_devolucao', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='prova',
            name='Prova_id_status',
            field=models.ForeignKey(null=True, to='page.status'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='disciplina_id_prova',
            field=models.ForeignKey(to='page.Prova'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='disciplina_id_status',
            field=models.ForeignKey(to='page.status'),
        ),
    ]
