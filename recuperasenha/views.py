from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User 							# objeto que carrega as informacoes do usuario para implementar

# Create your views here.

def index(request):
	if request.method == 'GET':
		hsSenha = request.GET.get('hash')
		objUsers = User.objects.all()
		for i in objUsers:
			if objUsers.password == hsSenha:
				i.is_active = True
				i.save()
				return render(request, 'HTML/validaemail.html')
	if request.method == 'POST':
		email = request.POST.get('')
	return render(request, '')

