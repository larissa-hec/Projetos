#from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets
from Banco_digital.Models.models import cliente
from Banco_digital.Serializer.serializer import clienteSerializer


class clienteViewset(viewsets.ModelViewSet):

    queryset = cliente.objects.all()
    serializer_class = clienteSerializer
