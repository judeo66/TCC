# -*- encoding: utf  -8 -*-
from django.shortcuts import render
from Registros.models import Registro
from reportlab.pdfgen import canvas
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from os import path
import mimetypes

# Create your views here.
def index(request):
   if request.method == 'POST':  
      contato_id = User.objects.get(id=request.user.id) 
      dt1 = request.POST.get('PrimeiraData')
      dt2 = request.POST.get('SegundaData')

      dt1 = dt1[6:]+'-'+dt1[:2]+'-'+dt1[3:5]
      dt2 = dt2[6:]+'-'+dt2[:2]+'-'+dt2[3:5]

      if dt1 > dt2:
         dt3 = dt1
         dt1 = dt2
         dt2 = dt3

      # Create the HttpResponse object with the appropriate PDF headers.
      response = HttpResponse(content_type='application/pdf')
      response['Content-Disposition'] = 'attachment; filename="registro.pdf"'

      # Create the PDF object, using the response object as its "file."
      objPDF = canvas.Canvas(response)

      # Draw things on the PDF. Here's where the PDF generation happens.
      # See the ReportLab documentation for the full list of functionality.
      objPDF.drawString(80, 800, "Paciente: "+contato_id.first_name)
      objPDF.drawString(400, 800, "Legenda Hora")
      objPDF.drawString(400, 785, "1- Antes do café")
      objPDF.drawString(400, 770, "2- Depois do café")
      objPDF.drawString(400, 755, "3- Antes do almoço")
      objPDF.drawString(400, 740, "4- Depois do almoço")
      objPDF.drawString(400, 725, "5- Antes do jantar")
      objPDF.drawString(400, 710, "6- Depois do jantar")
      objPDF.drawString(400, 695, "7- De madrugada")
      objPDF.drawString(200, 700, "Tabela com os registros")
      objPDF.drawString(80, 660, "Data")
      objPDF.drawString(150, 660, "Hora")
      objPDF.drawString(200, 660, "Glicose")
      objPDF.drawString(260, 660, "Carboidratos")
      objPDF.drawString(360, 660, "Comentario")

      dataset = Registro.objects.filter(IdUsuario = request.user.id)

      registros = dataset.filter(RegistroData__range=[dt1,dt2])
      for i, regs in enumerate(registros):
         objPDF.drawString(80, 640 - i *20, "%s" % (regs.RegistroData))
         objPDF.drawString(150, 640 - i *20, "%s" % (regs.Hora))                                        # coleta o horario do registro
         objPDF.drawString(200, 640 - i *20, "%s" % (regs.NivelGlicose))                                # coleta o nivel de glicose
         objPDF.drawString(260, 640 - i *20, "%s" % (regs.NivelCarb))                                   # coleta o nivel de Carboidratos
         objPDF.drawString(360, 640 - i *20, "%s" % (regs.Comentario))                                  # coleta o nivel de Comentario
      # p.drawString(100, 100, "registros ="+ registros)
      # Close the PDF object cleanly, and we're done.
      objPDF.showPage()
      objPDF.save()
      return response
   return render(request, 'HTML/relatorios.html')