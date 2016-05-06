from django.db import models
from django.utils import timezone

class Professor(models.Model):
    id_professor=models.AutoField(primary_key=True,auto_created=True)
    nome = models.CharField(max_length=60)
    matricula = models.CharField(max_length=15)
    email = models.CharField(max_length=30,blank=True)
