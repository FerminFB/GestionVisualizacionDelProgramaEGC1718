# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from src import settings
from visualizacion.models import Programa, Charlas
import sqlite3
from io import BytesIO
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph, SimpleDocTemplate, Image, Spacer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect


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
    doc = SimpleDocTemplate(
        response,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=50,
        bottomMargin=18,
    )
    Story = []
    im = Image(settings.STATIC_ROOT+'/images/logoUS.png', 1 * inch, 1 * inch)
    Story.append(im)
    Story.append(Spacer(2, 24))
    estilos = getSampleStyleSheet()
    estilos.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    resultado = []
    bd = sqlite3.connect("programa.db")
    cursor = bd.cursor()
    sql_lunes = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, resumen from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Monday' order by  hora_fin asc;"
    sql_martes = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, resumen from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Tuesday' order by  hora_fin asc;"
    sql_miercoles = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, resumen from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Wednesday' order by  hora_fin asc;"
    sql_jueves = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, session_name from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Thursday' order by  hora_fin asc;"
    sql_viernes = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, session_name from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Friday' order by  hora_fin asc;"
    lunes = cursor.execute(sql_lunes)
    resultado.extend(lunes)
    martes = cursor.execute(sql_martes)
    resultado.extend(martes)
    miercoles = cursor.execute(sql_miercoles)
    resultado.extend(miercoles)
    jueves = cursor.execute(sql_jueves)
    resultado.extend(jueves)
    viernes = cursor.execute(sql_viernes)
    resultado.extend(viernes)
    bd.close()

    head = estilos["Heading4"]
    head.alignment = TA_CENTER
    Story.append(Paragraph('PROGRAMA DEL EVENTO', head))
    Story.append(Spacer(2, 24))


    primera_columna = ('Fecha', 'Hora Inicio', 'Hora Fin', 'Acciones', 'Titulo')

    datos = []
    a = ""
    for i in resultado:
        if i[5] is not None:
            a = i[5][:19]+"..."
        datos.append((i[0]+' '+i[1], i[2], i[3], i[4], a))

    detalle = Table([primera_columna] + datos, colWidths=[100, 60, 60, 100, 120])

    detalle.setStyle(TableStyle([
        ('GRID', (0, 0), (4, -1), 1, colors.black),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('FONTSIZE', (0, 0), (0, 0), 10, 'CENTER'),
    ]))
    Story.append(detalle)
    doc.build(Story)
    return response

