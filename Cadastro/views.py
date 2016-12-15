#-*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render											# renderiza a pagina														
from django.contrib import messages
from django.contrib.auth.models import User 								# objeto da user
from django.core.urlresolvers import reverse 								
from Cadastro.models import UserProfile, Tratamentos, Medicamentos  		# objetos do cadastro
from django.http import HttpResponseRedirect								# classe que redireciona para outras paginas
from django.contrib.auth import authenticate, login, logout					# classes de usuario para login e logout
from django.template.loader import get_template
from django.template import Context
from django.utils.safestring import mark_safe
from django.core.mail import send_mail, EmailMessage

def index(request):															# metodo index
	med = Medicamentos.objects.all()
	if request.method == 'POST':											# se for POST da pagina
		stLogin = request.POST.get('Email')									# recupera o valor do compo email
		if not User.objects.filter(username=stLogin):						# verifica se o usuario ja existe
			stNome = request.POST.get('Nome')								# recupera o valor do campo nome
			stConfSenha = request.POST.get('ConfirmaSenha')					# recupera o valor de confirmação de senha
			stPaword = request.POST.get('Senha')							# recupera a senha
			dtRegistroData = request.POST.get('Nascimento')					# pega a data de nascimento no modelo dd/mm/aaaa
			dtData = dtRegistroData[6:]+'-'+dtRegistroData[:2]+'-'+dtRegistroData[3:5]
			rbSexo = request.POST.get('Sexo')								# recupera o sexo
			nPeso = request.POST.get('Peso')								# recupera o peso
			nAltura = request.POST.get('Altura')							# recupera a altura
			stAtFisica = request.POST.get('AtFisica')						# recupera a atividade fisica
			nGlicMax = request.POST.get('GlicMax')							# recupera o nivel de glicose maximo
			nGlicAlt = request.POST.get('GlicAlt')							# recupera o nivel de glicose alto
			nMeta = request.POST.get('Meta')								# recupera a meta
			nGlicBaixa = request.POST.get('GlicBaixa')						# recupera o nivel de glicose baixo
			nGlicMin = request.POST.get('GlicMin')							# recupera a meta
			nCurtaDuracao = request.POST.get('CurtaDuracao')				# recupera a curta duracao
			nLongaDuracao = request.POST.get('LongaDuracao')				# recupera a longa duracao
			nSensibilidade = 1800 / int(request.POST.get('qtdsen'))						# recupera a sensibilidade


			if stConfSenha == stPaword: 									# se a senha for igual a confirmacao	
				novo_contato = User.objects.create_user(					# monta o objeto para salvar
					username=stLogin,
					password=stPaword,
					first_name=stNome,
					
				)
				novo_contato.is_active=False
				novo_contato.save()											# salva o ususario		
				contato_id = User.objects.get(username=stLogin)				# recupera o id do usuario
				continua_contato = UserProfile(								# objeto com novas configuracoes do usuario
					BDate=dtData,
					Sexo=rbSexo,
					Peso=nPeso,
					altura=nAltura,
					AtFisica=stAtFisica,	
					user_id=contato_id.id
				)
				continua_contato.save()										# salva outras informações sobre o usuarios

				CadastraNivel = Tratamentos(								# cria o objeto com os niveis ideais para o usuario
					Id_user_id=contato_id.id,
					HiperGLicemia=nGlicMax,
					GlicAlta=nGlicAlt,
					GLicIdeal=nMeta,
					GlicBaixa=nGlicBaixa,
					HipoGlicemia=nGlicMin,
					Id_medicamentoCurto=med.get(id=nCurtaDuracao),
					Id_medicamentoLongo=med.get(id=nLongaDuracao),
					Sensibilidade= nSensibilidade
				)	
				CadastraNivel.save()

				content = get_template('HTML/email.html').render(Context({'host': request.META['HTTP_HOST']}))
				subject = 'MDG'
				message = 'Obrigado por entrar no nosso site'
				from_email = settings.EMAIL_HOST_USER
				to_list = [stLogin]
				#send_mail(subject, message, from_email, to_list)

				email = EmailMessage(subject, mark_safe(content) ,from_email, to_list)
				email.content_subtype = 'html'
				email.send()



				return render(request, 'HTML/validaemail.html')							# retorna para a homeo0
		else:
			return render(request, 'HTML/singin.html', {'usuario': True})	# retorna om mensagem de senhas diferentes
	return render(request, 'HTML/singin.html', {'medics':med})     			# retorna a pagina de cadastro