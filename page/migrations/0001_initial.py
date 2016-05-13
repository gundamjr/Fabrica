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
                ('id_curso', models.AutoField(auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=60)),
                ('turma', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id_disciplina', models.AutoField(auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=45)),
                ('periodo', models.CharField(max_length=3, choices=[('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4'), ('P5', 'P5'), ('P6', 'P6'), ('P7', 'P7'), ('P8', 'P8'), ('P9', 'P9'), ('P10', 'P10')])),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina_Profesor',
            fields=[
                ('id_Disciplina_Profesor', models.AutoField(auto_created=True, serialize=False, primary_key=True)),
                ('Disciplina_id', models.ForeignKey(to='page.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id_professor', models.AutoField(auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=60)),
                ('matricula', models.CharField(unique=True, max_length=15)),
                ('email', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id_prova', models.AutoField(auto_created=True, serialize=False, primary_key=True)),
                ('data_prova', models.DateField()),
                ('data_limite', models.DateField()),
                ('estagio', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)])),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id_status', models.AutoField(auto_created=True, serialize=False, primary_key=True)),
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
            model_name='disciplina_profesor',
            name='Professor_id',
            field=models.ForeignKey(to='page.Professor'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='disciplina_id_prova',
            field=models.ForeignKey(null=True, to='page.Prova'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='disciplina_id_status',
            field=models.ForeignKey(null=True, to='page.status'),
        ),
    ]
