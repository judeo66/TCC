# -*- coding: utf-8 -*-
from django.shortcuts import render
from Cadastro.models import UserProfile, Tratamentos
# Create your views here.
def index(request):
	contato_id = UserProfile.objects.get(user_id=request.user.id)
	Nivel_id = Tratamentos.objects.get(Id_user_id=request.user.id)
	if request.method == 'POST':
		nGlicMax = request.POST.get('GlicMax')
		nGLicAlto = request.POST.get('GlicAlt')
		nMeta = request.POST.get('Meta')
		nGlicBaixa = request.POST.get('GlicBaixa')
		nGlicMin = request.POST.get('GlicMin')
		nPeso = request.POST.get('Peso')
		nAltura = request.POST.get('Altura')
		atFisica = request.POST.get('AtFisica')
		alerta = '0'
		if nGlicMax<=nGLicAlto:
			alerta = '1'
			msg = 'A HiperGlicemia não pode ser menor que a glicemia em nível alto'
			
		if nGLicAlto<=nMeta:
			alerta = '1'
			msg = 'A glicemia alta não pode ser menor que a meta'

		if nMeta >= nGlicBaixa:
			alerta = '1'
			msg = 'A meta não pode ser menor que a glicemia em nível baixo'

		if nGlicBaixa <= nGlicMin:
			alerta = '1'
			msg = 'A meta não pode ser menor que a glicemia em nível baixo'

		if nGLicAlto >= 200:
			alerta = '1'
			msg = '200'			
		
		if alerta == '1':
			context = {'confContato':contato_id, 'nivelGlic':Nivel_id, 'alerta': alerta, 'msg':msg }
			return render(request, 'HTML/configuracoes.html', context)		

		contato_id.Peso=nPeso		
		contato_id.altura=nAltura
		contato_id.AtFisica=atFisica

		
		Nivel_id.HiperGLicemia=nGlicMax
		Nivel_id.HipoGlicemia=nGlicMin
		Nivel_id.GlicAlta=nGLicAlto
		Nivel_id.GlicBaixa=nGlicBaixa
		Nivel_id.GLicIdeal=nMeta
		
		contato_id.save()
		Nivel_id.save()
		return render(request, 'HTML/configuracoes.html', context)

	context = {'confContato':contato_id, 'nivelGlic':Nivel_id }
	return render(request, 'HTML/configuracoes.html', context)
