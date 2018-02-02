from django.conf.urls import url,include
from . import views
from visualizacion.views import programa_list, charla_list

urlpatterns = [
    url(r'^$',views.home),
    url(r'^programas$',programa_list, name="programa_listar"),
    url(r'^charlas$',charla_list, name="charla_listar"),

]