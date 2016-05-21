from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


Estage=((1,1),(2,2),(3,3))


class Professor(models.Model):
    id_professor=models.AutoField(primary_key=True,auto_created=True)
    nome = models.CharField(max_length=60)
    matricula = models.CharField(max_length=15,unique=True)
    email = models.CharField(max_length=30,blank=True)


class Curso(models.Model):
	Curso_id=models.AutoField(primary_key=True,auto_created=True)
	nome=models.CharField(max_length=60)
	turma=models.CharField(max_length=1)


class status(models.Model):
	id_status=models.AutoField(primary_key=True,auto_created=True)
	devolucao=models.BooleanField(default=False)
	data_devolucao=models.DateField(null=True)


class Prova(models.Model):
	id_prova=models.AutoField(primary_key=True,auto_created=True)
	id_status=models.ForeignKey(status,on_delete=models.CASCADE,null=True)
	data_prova=models.DateField()
	data_limite=models.DateField()
	estagio=models.IntegerField(choices=Estage)


class Disciplina(models.Model):
	id_disciplina=models.AutoField(primary_key=True,auto_created=True)
	nome=models.CharField(max_length=45)
	periodo=models.IntegerField(null=True)
	id_prova=models.ForeignKey(Prova,on_delete=models.CASCADE,null=True)
	id_status=models.ForeignKey(status,on_delete=models.CASCADE,null=True)

class Disciplina_Profesor(models.Model):
	id_Disciplina_Profesor=models.AutoField(primary_key=True,auto_created=True)
	Professor_id=models.ForeignKey(Professor,on_delete=models.CASCADE,null=True)
	Disciplina_id=models.ForeignKey(Disciplina,on_delete=models.CASCADE,null=True)

class Disciplina_Curso(models.Model):
	id_Disciplina_Curso=models.AutoField(primary_key=True,auto_created=True)
	Curso_id=models.ForeignKey(Curso,on_delete=models.CASCADE,null=True)
	Disciplina_id=models.ForeignKey(Disciplina,on_delete=models.CASCADE,null=True)

