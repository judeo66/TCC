# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 								# objeto da user



def index(request):
	if request.method == 'POST':
		stNome = request.POST.get('login')
		stSenha = request.POST.get('senha')
		user = authenticate(username=stNome, password=stSenha)
		if not User.objects.filter(username=stNome):
			return HttpResponseRedirect('/cadastro')		
		else:
			if not authenticate(username=stNome, password=stSenha):
				return render(request, 'HTML/login.html', { 'senha': True})
			else:
				Dados = authenticate(username=stNome, password=stSenha, is_active=1)
				login(request, Dados)
				return HttpResponseRedirect('/registros')
	return render(request, 'HTML/login.html')

def sair(request):
    logout(request)
    return HttpResponseRedirect('/')


def erro(request):
	return HttpResponseRedirect(reverse('erro'))	
	
	
