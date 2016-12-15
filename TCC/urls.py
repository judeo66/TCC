from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from pagPrincipal import views as objPri
from Calculadora import views as objCalc
from Configuracoes import views as objConf
from Graficos import views as objGraps
from Cadastro import views as objCad
from Registros import views as objRegs
from Relatorios import views as objRel
from Notificacoes import views as objNots
from recuperasenha import views as objSenha

admin.autodiscover()


urlpatterns = [
	url(r'^$', objPri.index),
	url(r'^registros/$', objRegs.index),
	url(r'^cadastro/$', objCad.index),
	url(r'^calculadora/$', objCalc.index),
	url(r'^configuracoes/$', objConf.index),
	url(r'^grafico/$', objGraps.index),
	url(r'^relatorios/$', objRel.index),
	url(r'^sair/$', objPri.sair),
	url(r'^admin/', admin.site.urls),
	url(r'^nots/$', objNots.index),
	url(r'^valida-email/$', objSenha.index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 