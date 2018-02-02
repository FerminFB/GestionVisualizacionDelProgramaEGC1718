# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from  visualizacion.models import Programa,Charlas

# Create your views here.

def home(request):

    return render(request, 'programa/principal.html')


def programa_list(request):

    programa = Programa.objects.all()
    contexto = {'programas' :programa}

    charla = Charlas.objects.all()
    contexto2 = {'charlas': charla}

    return render(request,'programa/principal.html',contexto)


def charla_list(request):
    charla = Charlas.objects.all()
    contexto2 = {'charlas': charla}
    return render(request, 'programa/principal2.html', contexto2)