from django.shortcuts import render

def index(request):															# metodo index
	if request.method == 'POST':											# se for POST da pagina
		i = 12
	return render(request, 'HTML/notificacoes.html')								# retorna a pagina de cadastro
