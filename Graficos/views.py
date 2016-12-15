# -*- coding: utf-8 -*-	
from django.shortcuts import render
from Registros.models import Registro
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime, time, timedelta



@login_required
def index(request):
	reg = Registro.objects.filter( IdUsuario = request.user.id)	
	dtHj = datetime.now()
	dtAntes = dtHj.replace(month=int(dtHj.month) - 1)
	dtPrimeiro = dtHj.replace(month=int(dtHj.month) - 2)
	dt3 = dtHj.replace(month=int(dtHj.month) - 3)
	Mes = reg.filter(RegistroData__range=[dtAntes, dtHj])
	MesAntes = reg.filter(RegistroData__range=[dtPrimeiro, dtAntes])
	MesPrimeiro = reg.filter(RegistroData__range=[dt3, dtPrimeiro])

	return render(request, 'HTML/grafico.html', { 'login': True, 'reg': reg, 'Mes': Mes, 'MesAntes': MesAntes, 'MesPrimeiro': MesPrimeiro})