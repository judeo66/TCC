# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Registro(models.Model):
	Categoria = (
		('1', u'antes do café'),
		('2', u'depois do café'), 
		('3', u'antes do almoço'), 
		('4', u'depois do almoço'), 
		('5', u'antes do jantar'),
		('6', u'depois do jantar'), 
		('7', u'Madrugada'),
	)
	IdUsuario = models.ManyToManyField(User)
	RegistroData = models.DateField(auto_now=False) 
	Hora = models.CharField(choices=Categoria, max_length=2) 
	NivelGlicose =  models.IntegerField()
	NivelCarb = models.IntegerField()
	Comentario = models.CharField(max_length=255)
	Unidades = models.IntegerField()
	Insulina = models.CharField(max_length=1)		