# -*- encoding: utf	-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from Cadastro.models import Tratamentos as objTratamento
from Cadastro.models import Medicamentos as objMedicamentos
from Cadastro.models import UserProfile
from datetime import datetime, time, timedelta

@login_required
def index(request):
	med = objMedicamentos.objects.all()
	if request.method == 'POST':
		nNivelGlicose = request.POST.get('nivelGlicose')
		nCarb = request.POST.get('totalCal')
		stHorario = request.POST.get('horario')
		nInsulina = request.POST.get('Insulina')
		objTrat = objTratamento.objects.get(Id_user=request.user.id)
		Med = objMedicamentos.objects.get(id=nInsulina)
		objUser = UserProfile.objects.get(user_id=request.user.id)
		tempo = datetime.now()
		
		if int(tempo.hour) < int(stHorario[0:2]):
			tempo -= timedelta(days=1)
		tempo = tempo.replace(hour=int(stHorario[0:2]), minute=int(stHorario[3:5]))
		
		if int(tempo.hour) + int(Med.Pico) > 23:
			tempo += timedelta(days=1)
			tempo = tempo.replace(hours= int(tempo.hour) + int(Med.Pico) - 23)
		else:	
			tempo += timedelta(hours=int(Med.Pico))

		if int(tempo.minute) + Med.Pico % 1 * 60 > 59:
			tempo += timedelta(hours=1)
			tempo += timedelta(minutes= int(stHorario[3:5]) + Med.Pico % 1 * 60 - 59)
		else:
			tempo += timedelta(minutes= int(stHorario[3:5]) + Med.Pico % 1 * 60)

		if tempo > datetime.now():
			return render(request,'HTML/calculadora.html',{'msg': 'Voce tomou sua insulina a pouco tempo, por favor aguarde o Pico', 'medics':med})
		if tempo <= datetime.now():	
			correcao = int(nNivelGlicose) - int(objTrat.GLicIdeal) / int(objTrat.Sensibilidade)			
			comp = 0
			if 45 <= int(objUser.Peso) <= 49:
				comp = 16
			if 49 < int(objUser.Peso) <= 58:
				comp = 15
			if 58 < int(objUser.Peso) <= 62:
				comp = 14
			if 63 < int(objUser.Peso) <= 67:
				comp = 13
			if 67 < int(objUser.Peso) <= 76:
				comp = 12
			if 76 < int(objUser.Peso) <= 80:
				comp = 11
			if 80 < int(objUser.Peso) <= 85:
				comp = 10
			if 85 < int(objUser.Peso) <= 89:
				comp = 9
			if 90 < int(objUser.Peso) <= 98:
				comp = 8
			if 98 < int(objUser.Peso) <= 107:
				comp = 7
			if int(objUser.Peso) >= 108:
				comp = 6
			qtdInsulina = correcao + int(nCarb) / comp 

			return render(request,'HTML/calculadora.html',{'msg': 'Você precisa tomar '+ str(qtdInsulina) +' Un.', 'medics':med})
	return render(request, 'HTML/calculadora.html', {'medics':med})

def m(request):
	return render(request, 'HTML/index.html')