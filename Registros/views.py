# -*- coding: utf-8 -*-	
from django.shortcuts import render
from django.contrib.auth.models import User
from Registros.models import Registro
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def index(request):
	if request.method == 'POST':
		contato_id = User.objects.get(id=request.user.id) 
		Hora = request.POST.get('Hora')
		nGlicose = request.POST.get('nivelGlicose') 
		nCarb = request.POST.get('totalCal') 
		stComent = request.POST.get('Coment') 
		dtRegistroData = request.POST.get('RegData')
		dtData = dtRegistroData[6:] + '-' + dtRegistroData[0:2]	+ '-'+ dtRegistroData[3:5]  
		nUnidade = request.POST.get('Unidades')
		boolInsulina = request.POST.get('ins')
		novoRegistro = Registro(			
			Hora = Hora,
			NivelGlicose = nGlicose,
			NivelCarb = nCarb,
			Comentario = stComent,
			RegistroData = dtData,
			Unidades = nUnidade,
			Insulina = boolInsulina
		)
		novoRegistro.save()		
		novoRegistro.IdUsuario.add(contato_id)
	return render(request, 'HTML/registro.html')	