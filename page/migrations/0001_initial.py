# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('Curso_id', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=60)),
                ('turma', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id_disciplina', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=45)),
                ('periodo', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina_Curso',
            fields=[
                ('id_Disciplina_Curso', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('Curso_id', models.ForeignKey(null=True, to='page.Curso')),
                ('Disciplina_id', models.ForeignKey(null=True, to='page.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina_Profesor',
            fields=[
                ('id_Disciplina_Profesor', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('Disciplina_id', models.ForeignKey(null=True, to='page.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id_professor', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=60)),
                ('matricula', models.CharField(unique=True, max_length=15)),
                ('email', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id_prova', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('data_prova', models.DateField()),
                ('data_limite', models.DateField()),
                ('estagio', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)])),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False, auto_created=True)),
                ('devolucao', models.BooleanField(default=False)),
                ('data_devolucao', models.DateField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='prova',
            name='id_status',
            field=models.ForeignKey(null=True, to='page.status'),
        ),
        migrations.AddField(
            model_name='disciplina_profesor',
            name='Professor_id',
            field=models.ForeignKey(null=True, to='page.Professor'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='id_prova',
            field=models.ForeignKey(null=True, to='page.Prova'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='id_status',
            field=models.ForeignKey(null=True, to='page.status'),
        ),
    ]
