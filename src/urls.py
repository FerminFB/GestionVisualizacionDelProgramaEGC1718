"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from visualizacion.views import *
from django.conf.urls import url
import visualizacion

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', programa_list, name="programa_listar"),
    url(r'^charlas$', charla_list, name="charla_listar"),
    url(r'^export_pdf$', export_pdf, name="export_pdf"),
    url(r'^soap_service/', visualizacion.views.my_soap_application),
]
