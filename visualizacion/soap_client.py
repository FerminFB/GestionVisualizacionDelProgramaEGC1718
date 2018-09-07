# soap_client.py
# coding=utf-8

from suds.client import Client
from suds.cache import NoCache

my_client = Client('http://127.0.0.1:8000/soap_service/?WSDL', cache=NoCache())
print my_client
print 'Function getEventos: ', my_client.service.getEventos()
print 'Function getCharlas: ', my_client.service.getCharlas()