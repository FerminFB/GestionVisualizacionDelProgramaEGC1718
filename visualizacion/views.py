# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sqlite3
from io import BytesIO
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle


def export_pdf():
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=programa.pdf'
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    resultado = []
    bd = sqlite3.connect("programa.db")
    cursor = bd.cursor()
    sql_lunes = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, resumen from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Monday' order by  hora_fin asc;"
    sql_martes = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, resumen from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Tuesday' order by  hora_fin asc;"
    sql_miercoles = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, resumen from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Wednesday' order by  hora_fin asc;"
    sql_jueves = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, session_name from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Thursday' order by  hora_fin asc;"
    sql_viernes = "select dia, fecha, hora_inicio, hora_fin, programa.titulo, charlas.titulo, evento, ponentes, session_name from programa left outer join charlas on charlas.sessioncode = programa.sessioncode where dia= 'Friday' order by  hora_fin asc;"
    lunes = cursor.execute(sql_lunes)
    martes = cursor.execute(sql_martes)
    miercoles = cursor.execute(sql_miercoles)
    jueves = cursor.execute(sql_jueves)
    viernes = cursor.execute(sql_viernes)
    resultado.extend(lunes)
    resultado.extend(martes)
    resultado.extend(miercoles)
    resultado.extend(jueves)
    resultado.extend(viernes)
    bd.close()

    pdf.setFont("Helvetica", 16)
    pdf.drawString(230, 790, u"PROGRAMA DEL EVENTO")

    encabezados = ('Fecha', 'Hora Inicio', 'Hora Fin', 'Acciones', 'Titulo', 'Evento', 'Ponentes', 'Resumnen', 'Nombre Sesion')
    detalles = [(i[0]+' '+i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]) for i in resultado]
    detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
    detalle_orden.setStyle(TableStyle(
        [
            ('ALIGN', (0, 0), (3, 0), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
        ]
    ))
    detalle_orden.wrapOn(pdf, 800, 600)
    detalle_orden.drawOn(pdf, 60, 600)
    pdf.showPage()
    pdf.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response





