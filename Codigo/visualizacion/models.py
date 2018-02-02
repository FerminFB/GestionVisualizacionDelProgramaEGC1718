# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Charlas(models.Model):
    sessioncode = models.TextField(db_column='SESSIONCODE', unique=True, primary_key=True)  # Field name made lowercase. This field type is a guess.
    evento = models.TextField(db_column='EVENTO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    titulo = models.TextField(db_column='TITULO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ponentes = models.TextField(db_column='PONENTES', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    resumen = models.TextField(db_column='RESUMEN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    session_name = models.TextField(db_column='SESSION_NAME', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CHARLAS'



class Programa(models.Model):
    id = models.IntegerField(db_column='ID', unique=True, primary_key=True)  # Field name made lowercase.
    dia = models.TextField(db_column='DIA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fecha = models.TextField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sessioncode = models.TextField(db_column='SESSIONCODE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    hora_inicio = models.TextField(db_column='HORA_INICIO', blank=True, null=True)  # Field name made lowercase.
    hora_fin = models.TextField(db_column='HORA_FIN', blank=True, null=True)  # Field name made lowercase.
    titulo = models.TextField(db_column='TITULO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PROGRAMA'

