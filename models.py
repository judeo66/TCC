# -*- encoding: utf	-8 -*-
from __future__ import unicode_literals									# objeto do sistema
from django.db import models											# objeto para indicar que é uma model

class Medicamentos(models.Model):
	Categorias = (														
		('1', u'pouco ou nenhum exercicio fisico'),
		('2', u'Esporte 1-3 dias na semana'), 
		('3', u'Esporte 3-5 dias na semana'), 
		('4', u'Esporte 5-7 dias na semana'), 
		('5', u'Esporte e trabalho fisico'),
	)

	Vias = (														
		('1', u'pouco ou nenhum exercicio fisico'),
		('2', u'Esporte 1-3 dias na semana'), 
		('3', u'Esporte 3-5 dias na semana'), 
		('4', u'Esporte 5-7 dias na semana'), 
		('5', u'Esporte e trabalho fisico'),
	)

	Marca = models.CharField(max_length=1,null=False)					# marca
	Tipo = models.CharField(max_length=1,null=False)					# 
	Inicio_acao = models.IntegerField(max_length=1,null=False)			# 
	Pico = models.IntegerField(max_length=1,null=False)					#
	Duração = models.IntegerField(max_length=1,null=False)				#
	Categoria = models.IntegerField(max_length=1,null=False,choice=Categorias)	#
	Via = models.IntegerField(max_length=1,null=False,choice=Vias)

class Medico(model.Model):
	Contato = models.CharField(max_length=11,null=False)					# 
	CRM = models.CharField(max_length=11,null=False)					#
	Clínica 
	user = models.OneToOneField(										# referencia da model user, relacao de 1 para 1
		User,
		related_name='user_profile'
	)

class Tratamentos(model.Model):
	Dt_tratamento = models.DateField(null=False)						# data do tratamento
	Id_medicamento = models.ManyToManyField(Medicamentos)
	Horário = models.TimeField(null=False)
