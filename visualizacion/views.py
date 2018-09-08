# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from src import settings
from visualizacion.models import Programa, Charlas
import sqlite3
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph, SimpleDocTemplate, Image, Spacer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from reportlab.lib.pagesizes import A4, inch, landscape
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
from spyne.model.complex import *



def programa_list(request):
    programa_lista = Programa.objects.order_by('sessioncode')
    page = request.GET.get('page', 1)

    paginator = Paginator(programa_lista, 10)
    try:
        programas = paginator.page(page)
    except PageNotAnInteger:
        programas = paginator.page(1)
    except EmptyPage:
        programas = paginator.page(paginator.num_pages)

    return render(request, 'visualizacion/index.html', { 'programas': programas })


def charla_list(request):
    charla_lista = Charlas.objects.order_by('sessioncode')
    page = request.GET.get('page', 1)

    paginator = Paginator(charla_lista, 10)
    try:
        charlas = paginator.page(page)
    except PageNotAnInteger:
        charlas = paginator.page(1)
    except EmptyPage:
        charlas = paginator.page(paginator.num_pages)

    return render(request, 'visualizacion/charlas.html', { 'charlas': charlas })


def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=programa.pdf'
    doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30,
                            bottomMargin=18)
    doc.pagesize = landscape(A4)
    elements = []
    im = Image(settings.STATIC_ROOT + '/images/logoUS.png', 1 * inch, 1 * inch)
    elements.append(im)
    elements.append(Spacer(2, 24))
    estilos = getSampleStyleSheet()

    estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    datos = [
        ('Fecha', 'Hora Inicio', 'Hora Fin', 'Acciones', 'Titulo')
    ]
    data = []
    bd = sqlite3.connect("programa.db")
    cursor = bd.cursor()
    sql_lunes = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, resumen from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Monday' order by  hora_fin asc;"
    sql_martes = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, resumen from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Tuesday' order by  hora_fin asc;"
    sql_miercoles = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, resumen from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Wednesday' order by  hora_fin asc;"
    sql_jueves = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, session_name from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Thursday' order by  hora_fin asc;"
    sql_viernes = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, session_name from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Friday' order by  hora_fin asc;"
    lunes = cursor.execute(sql_lunes)
    data.extend(lunes)
    martes = cursor.execute(sql_martes)
    data.extend(martes)
    miercoles = cursor.execute(sql_miercoles)
    data.extend(miercoles)
    jueves = cursor.execute(sql_jueves)
    data.extend(jueves)
    viernes = cursor.execute(sql_viernes)
    data.extend(viernes)
    bd.close()

    head = estilos["Heading4"]
    head.alignment = TA_CENTER
    elements.append(Paragraph('PROGRAMA DEL EVENTO', head))

    elements.append(Spacer(2, 24))

    for i in data:
        a = i[4]
        b = i[5]
        if i[4] is None:
            a = " "
        if i[5] is None:
            b = " "
        datos.append([i[0] + " " + i[1], i[2],i[3], a, b])


    # TODO: Get this line right instead of just copying it from the docs
    style = TableStyle([
        ('GRID', (0, 0), (4, -1), 1, colors.black),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('FONTSIZE', (0, 0), (0, 0), 10, 'CENTER'),
    ])

    # Configure style and word wrap
    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    data2 = [[Paragraph(cell, s) for cell in row] for row in datos]
    t = Table(data2, colWidths=[100, 60, 60, 100, 375])
    t.setStyle(style)

    # Send the data and build the file
    elements.append(t)
    doc.build(elements)
    return response


class SoapService(ServiceBase):
    @rpc(_returns=Array(Array(Unicode)))
    def getEventos(ctx):
        res = []
        bd = sqlite3.connect("programa.db")
        cursor = bd.cursor()
        sql = "select dia, fecha, hora_inicio, hora_fin, titulo,sessioncode from programa"
        resultado = cursor.execute(sql)
        res.extend(resultado)
        return res

    @rpc(_returns=Array(Array(Unicode)))
    def getCharlas(ctx):
        res = []
        bd = sqlite3.connect("programa.db")
        cursor = bd.cursor()
        sql = "select evento, titulo, ponentes, resumen,sessioncode from charlas"
        resultado = cursor.execute(sql)
        res.extend(resultado)
        return res


soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)

