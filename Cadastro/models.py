# -*- encoding: utf	-8 -*-			
from __future__ import unicode_literals									# objeto do sistema
from django.db import models											# objeto para indicar que é uma model
from django.contrib.auth.models import User 							# objeto que carrega as informacoes do usuario para implementar

class UserProfile(models.Model):										# classe model
	# categorias para atividades que o usuario pode escolher
	Atividade = (														
		(1, u'pouco ou nenhum exercicio fisico'),
		(2, u'Esporte 1-3 dias na semana'), 
		(3, u'Esporte 3-5 dias na semana'), 
		(4, u'Esporte 5-7 dias na semana'), 
		(5, u'Esporte e trabalho fisico'),
	)

	user = models.OneToOneField(										# referencia da model user, relacao de 1 para 1
		User,
		related_name='user_profile'
	)

	# informações necessárias para cadastro do usuário
	BDate = models.DateField(null=False)								# data de nascimento 		
	Sexo = models.CharField(max_length=1,null=False)					# sexo
	Peso = models.IntegerField(null=False)								# peso
	altura = models.IntegerField(null=False)							# altura
	AtFisica = models.IntegerField(max_length=2, choices=Atividade)		# nível de atividade física, se baseando nas categorias da variavel Atividde

class Medicamentos(models.Model):
	Tipos = (
		('1', u'ultrarrapida'),
		('2', u'acao rapida'),
		('3', u'acao intermediaria'),
		('4', u'acao prolongada'),
		('5', u'pre misturada regular'),
		('6', u'pre misturada analoga'),
	)
	Marca = models.CharField(max_length=25,null=False)					# marca
	Tipo = models.CharField(max_length=1,null=False,choices=Tipos)		# 
	Inicio_acao = models.FloatField(max_length=1,null=False)			# 
	Pico = models.FloatField(max_length=1,null=False)					#	
	Duracao = models.FloatField(max_length=1,null=False)				#

class Tratamentos(models.Model):
	Id_medicamentoCurto = models.ForeignKey(Medicamentos, related_name='medCurto')
	Id_medicamentoLongo = models.ForeignKey(Medicamentos, related_name='medLongo')
	HiperGLicemia = models.IntegerField(null=False, default=200)		# nível máximo de glicemia no sangue
	HipoGlicemia = models.IntegerField(null=False, default=50)			# nível minimo de glicemia no sangue
	GlicAlta =  models.IntegerField(null=False, default=145)			# nível alto de glicemia no sangue
	GlicBaixa =  models.IntegerField(null=False, default=80)			# nível baixo de glicemia no sangue
	GLicIdeal =  models.IntegerField(null=False, default=100)			# nível ideal de glicemia no sangue
	Id_user = models.OneToOneField(
		User,
		related_name='user_trat'
	)
	Sensibilidade = models.IntegerField(null=False, default=100)		# sensibilidade de insulina