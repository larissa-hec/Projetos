from rest_framework import viewsets
from Banco_digital.models import cliente
from Banco_digital.serializer import clienteSerializer


class clienteViewset(viewsets.ModelViewSet):

    queryset = cliente.objects.all()
    serializer_class = clienteSerializer